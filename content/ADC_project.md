Title: Resurrecting an old ADC - Motorola MC10319
Date: 2025-6-25 2:00
Category: Project
summary: Building a circuit to teach myself how a flash ADC works

### Description:

The Motorola MC10319 was a high speed parallel 8-bit flash ADC developed in the 1990s. I could not find direct examples of what this chip was used for online, but the datasheet claims the chip was designed for video broadcast, radar processing, and video display. In my case, this chip was taken out of a broken oscilloscope. A PhD student gave me this chip and told me that I would learn a lot about electronics on my journey to making it function again. He was right. 


### Project Overview

I broke this project down into three main systems I needed to get working: the main supplies VCC(D) and VCC(A), resistor ladder supplies VRT and VRB, and the parallel data output. 


### Power Supplies

For the +5V rails, I used my bench supply for simple smooth power. However, I needed -5V to power the comparators and -1.25V for the bottom of the resistor ladder to accommodate negative signal inputs. I settled on using a buck-boost converter to convert my +5V bench supply to -5V.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdkdGFHhVP9pxTN_s6gdyzKNivC43Os9wuMrsgRnBnlJ_LZXgpvyb5xZshSVOFwXR4U-GVZ3JUPXQZ3Nh-bPGoV-MmKf8IKNOXLj42XnCCjqLSKXs5Zy2zcrPqyDkfUiKo72z8KUA?key=W7Y8bPEHQgTMy58XeudftQ)

The datasheet provided this example and I decided to mostly follow it. It uses an MC34063A switching IC to invert the voltage. I tested this circuit with a 330 ohm resistor to simulate a load while staying under the 20mA maximum output current. However, the output voltage never went below -3V. I adjusted the feedback resistor values (1k and 3k) but could only get -5V with a very small load. I determined that there was some sort of load regulation problem due to a parasitic source inductance caused by terrible breadboard wiring. I re-routed the circuit using less wires and shorter loops, fixing the problem.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd-irGEP3YYvhffiIF4WVHWk-mjIWoz6urCBTqEnvMXcztUKVtjr8z5Fpk-lzA0Y37DwxvJew27DS88SH7SuQ2F1yyUL3dk1Jz8Wp2G66EBOb4BeMejN6XL4i1woHTmKxEqC5vyMw?key=W7Y8bPEHQgTMy58XeudftQ)

At this point the VRT and VRB supplies were trivial; I just used +1.25V and -1.25V linear regulators respectively to create the stable voltages required by the resistor ladder.


### Data Output

To process the output of the ADC, I settled on a Teensy 3.2 since it is what I had around. The teensy had to process the 8bit output and also provide the clock signal, since I wanted to keep my oscilloscope free to measure waveforms (it has an integrated signal generator). 

To get the fastest read possible, I connected pins D0-D7 on the MC10319 to the first 8 pins on PORT C on the Teensy. This will enable me to read the port register all at once instead of reading each pin sequentially. To find the first 8 pins of PORT C, I used the core\_pins.h file located in Arduino15/packages/teensy/hardware/avr/1.59.0/cores/teensy3. 

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcyS0bA3m5ARJiZD-kzNO_AEdzAHMKcchavnP5jFsByyOD-LT7N3nuJvFN1cswpvaHE1HXyP4TcQTaHHjQVuCYZD18iFE5JGhCiLgp1JNpiZV0Sc6LVI3uBUScdSCTU7kQPEqd3ZA?key=W7Y8bPEHQgTMy58XeudftQ)

Using this, I connected D0-D7 to Teensy Pins 15, 22, 23, 9, 10, 13, 11, 12 in order. Then I could use `uint8_t adc_value = GPIOC_PDIR & 0xFF `to get the first byte of the PORT C register corresponding to the adc output value.


### Quick Test

I hooked up a potentiometer to VRT and VRB and made the input to the ADC (VIN) the wiper of the potentiometer. This allows me to sweep the complete range of the ADC. And it works! The ADC values were 255 with VIN = VRT and 2 when VIN = VRB. I thought that I should get 0, but even with VIN shorted to VRT I still get 2. I did more testing and found that when VIN = 0 = VRM, I get a value of 130 instead of 128. So it seems there is an offset of 2. I troubleshooted this, and attributed it to the breadboard wiring. This is a very sensitive IC after all, and I am very happy with the accuracy I am getting, even with decoupling capacitors inches away from the IC. 

### ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe733NBMRiLdKlsD2sop-dhgqFGTqAIM5zkZiQzlgJKRpocOov4738C-U6UTueyGqVP7bg2Ba_luclAy39Nh5ImxcsvzGlbIOQaKWXs8C2a0bOCGRxaGcuTvNR49MhWE9-liLzW?key=W7Y8bPEHQgTMy58XeudftQ)

I also tested my understanding of the clock cycle. On the rising edge, the data output latches receive old data and output it to the data bus. During the high time, the comparators follow VIN but do not latch any data. On the falling edge, the comparator outputs the data taken right before the edge, and this data is latched to the data outputs. During the low time, everything remains latched and the chip waits for the rising edge again.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe7_Ad1zkVjOjr9JaLCiTBUdW1xpQYTl47SrhBukXyy5YyOwpsAACkjgxI3lF7Un7ty6MO0eB_L0X-bMf80m4wMm-9VFwq7DtLU06bgImkrLv5NrxSUaFjbRd4U9M-vuk-_Hy3z0w?key=W7Y8bPEHQgTMy58XeudftQ)

I tested this by using a button as a clock signal so I could manually advance the system timing. I got clean edges with a 6.8k pull down resistor on VIN and a button connecting VIN to +5V. When the clock was low, I adjusted VIN using the potentiometer and the ADC output did not change. This is because the data output is still latched with old data, and the comparators are not free to follow VIN. When I press the button, old data is latched and I see the ADC value change. While I hold the button, I adjust the potentiometer to allow the comparators to follow the changing VIN, but my ADC value doesn’t change since the output latches still have the old data. When I release the button, the ADC value changes to a value representing the last known position of the potentiometer, latching the last value of the comparators prior to the falling edge. Makes sense! 


### Future Plans

Now that I really understand how a flash ADC functions, I want to process a real analog signal, not just a potentiometer. I am planning to make a simple guitar tuner, by processing the raw output from a guitar.

I also want to de-cap this chip and examine it at the silicon die level. I plan to label the resistor ladder and the comparator network, find the binary encoder, and all of the data latches. 
