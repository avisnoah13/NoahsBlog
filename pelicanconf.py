AUTHOR = 'Noah Avis'
SITENAME = "Noah's Blog"
SITEURL = "https://avisnoah13.github.io/NoahsBlog/"
PATH = "content"

TIMEZONE = 'EST'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['images', 'icons']


# Blogroll
"""
LINKS = (
    ("About", "https://www.linkedin.com/in/noahavis13/"),
    ("Contact", "https://github.com/avisnoah13")
)
"""

# Social widget
SOCIAL = (
    ('github', 'https://github.com/avisnoah13'),
    ('linkedin', 'https://linkedin.com/in/noahavis13')
)

DEFAULT_CATEGORY = 'Blog'
DISPLAY_CATEGORIES_ON_MENU = True
HIDE_FROM_INDEX = ["Reading List"]





DEFAULT_PAGINATION = False

#Set Theme
THEME = "./pelican-themes/Flex"
FAVICON = "https://avisnoah13.github.io/NoahsBlog/icons/favicon.ico"

DISPLAY_PAGES_ON_MENU = True
PAGE_PATHS = ['pages']



#Sidebar Flex Setting
SITETITLE = ("Noah Avis")
SITESUBTITLE = ("Electrical Engineering Student @ Princeton University")
SITEDESCRIPTION = ("Personal blog for Noah Avis listing engineering projects and reading list")
COPYRIGHT_NAME = "Noah Avis"
COPYRIGHT_YEAR	= "2025"


# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
