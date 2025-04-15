Title: Reading List
Slug: reading
Save_as: reading.html

# 📚 Engineering Reading List

<style>
.book-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: 1.5rem;
  margin-top: 2rem;
}
.book-item {
  text-align: center;
}
.book-item img {
  max-width: 100%;
  height: auto;
  border-radius: 0.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  transition: transform 0.2s ease;
}
.book-item img:hover {
  transform: scale(1.05);
}
.book-title {
  margin-top: 0.5rem;
  font-weight: bold;
  font-size: 1rem;
}
</style>

<div class="book-grid">
{% for article in articles if article.category == "Reading List" %}
  <div class="book-item">
    <a href="{{ SITEURL }}/{{ article.url }}">
      <img src="{{ SITEURL }}/{{ article.metadata.Book_Cover }}" alt="{{ article.title }} cover">
      <div class="book-title">{{ article.title }}</div>
    </a>
  </div>
{% endfor %}
</div>
