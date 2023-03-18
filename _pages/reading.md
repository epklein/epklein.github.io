---
title: Reading
permalink: /reading
toc: true
toc_sticky: true
---

Here I share my currently reading list, as well as my book recommendations. I also put together the top blogs and newsletters I like to follow to keep up to date.

I have also separate reading lists in the main topics I write about in this blog, such as [Leadership](/leadership), [management](/mgmt), and [software engineering management](/mgmt/swe), among others.

## Currently reading

- {% include books/accelerate.md %}
- {% include books/an-elegant-puzzle.md %}
- {% include books/become-an-effective-swe-manager.md %}
- {% include books/engineering-management-for-the-rest-of-us.md %}

## Reading recommendations

### Books

- {% include books/how-to-win-friends-and-influence-people.md %}
- {% include books/the-drunkards-walk.md %}

### Blogs & Newsletters

- {% include blogs/the-pragmatic-engineer.md %}
- {% include blogs/scarlet-ink.md %}
- {% include blogs/irrational-exuberance.md %}
- {% include sites/paul-graham-essays.md %}

## Reading list

Books thar are next in my reading list

- [The Manager's Path](https://www.amazon.com.br/Managers-Path-Leaders-Navigating-English-ebook/dp/B06XP3GJ7F): A Guide for Tech Leaders Navigating Growth and Change, by Camille Fournier

## Books I've read

<ul>
{% for books in site.books %}
  <li><!-- {% if books.date_read <> "" %}{{ books.date_read }} - {% endif %} --><a href="{{ books.permalink }}">{{ books.title }}</a>, by {{ books.author }}</li>
{% endfor %}
</ul>