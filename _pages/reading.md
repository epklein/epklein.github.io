---
title: Reading
permalink: /reading
toc: true
toc_sticky: true
---

Here I share my currently reading list, as well as my book recommendations. I also put together the top blogs and newsletters I like to follow to keep up to date.

I have also separate reading lists in the main topics I write about in this blog, such as [leadership](/leadership), [management](/mgmt), and [software engineering management](/mgmt/swe), among others.

## Currently Reading

- {% include books/an-elegant-puzzle.md %}
- *[The Manager's Path](https://www.goodreads.com/book/show/33369254-the-manager-s-path)* by Camille Fournier
- *[Numbers don't Lie](https://www.goodreads.com/book/show/50705179-numbers-don-t-lie)* by Vaclav Smil
- *[The Principles of Product Development Flow](https://www.goodreads.com/book/show/6278270-the-principles-of-product-development-flow)* by Donald G. Reinertsen

## Reading Recommendations

### Books

- {% include books/how-to-win-friends-and-influence-people.md %}

### Blogs & Newsletters

- {% include blogs/the-pragmatic-engineer.md %}
- {% include blogs/scarlet-ink.md %}
- {% include blogs/irrational-exuberance.md %}
- {% include sites/paul-graham-essays.md %}

## Reading List

Books thar are next in my reading list

- [The Manager's Path](https://www.amazon.com.br/Managers-Path-Leaders-Navigating-English-ebook/dp/B06XP3GJ7F): A Guide for Tech Leaders Navigating Growth and Change, by Camille Fournier
- {% include books/become-an-effective-swe-manager.md %} Deprioritized due to priority changes for the quarter. Great reading indeed, I hope to get back on track soon.

## Books I've Read

<ul>
{% assign sorted_books = site.books | sort: 'date_read' | reverse %}
{% for book in sorted_books limit:5 %}
  <li><!-- {% if book.date_read <> "" %}{{ book.date_read }} - {% endif %} --><a href="{{ book.permalink }}">{{ book.title }}</a>, by {{ book.author }}</li>
{% endfor %}
</ul>

Check the full list of books I've read [here](/books-read).