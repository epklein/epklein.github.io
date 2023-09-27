---
title: Books I've read
permalink: /books-read
---

This is a chronological list of books I've read. For a collection of my currently reading list and reading recommendations, check [this page](/reading).

*You can also find a more complete list of books I've read on [Goodreads](https://www.goodreads.com/review/list/29886397-eduardo-klein?shelf=read)*.

<ul>
{% assign sorted_books = site.books | sort: 'date_read' | reverse %}
{% for book in sorted_books %}
  <li><!-- {% if book.date_read != nil %}{{ book.date_read }} - {% endif %} --><a href="{{ book.permalink }}">{{ book.title }}</a>, by {{ book.author }}</li>
{% endfor %}
</ul>