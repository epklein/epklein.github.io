---
title: Reading
permalink: /reading
toc: true
toc_sticky: true
---

I share my current reading list and book recommendations on this page. I also put together the top blogs and newsletters I like to follow to stay up to date.

I have separate reading lists for the main topics I write about in the [blog](/). Just access a section from the top menu and navigate to the Learning section.

## Currently Reading

- *[Numbers Don't Lie](https://www.goodreads.com/book/show/50705179-numbers-don-t-lie)* by Vaclav Smil
- *[The Principles of Product Development Flow](https://www.goodreads.com/book/show/6278270-the-principles-of-product-development-flow)* by Donald G. Reinertsen

*You can also find my updated list on [Goodreads](https://www.goodreads.com/review/list/29886397-eduardo-klein?shelf=currently-reading)*.

## Recommendations

### Books

- {% include books/how-to-win-friends-and-influence-people.md %}
- {% include books/the-managers-path.md %}
- {% include books/an-elegant-puzzle.md %}

*You can also find my reading recommendations on [Goodreads](https://www.goodreads.com/review/list/29886397-eduardo-klein?shelf=recommended-books)*.

### Blogs and Newsletters

- {% include blogs/the-pragmatic-engineer.md %}
- {% include blogs/scarlet-ink.md %}
- {% include blogs/irrational-exuberance.md %}
- {% include sites/paul-graham-essays.md %}

## Reading List

Books that are next on my reading list:

- {% include books/become-an-effective-swe-manager.md %}
- {% include books/effective-remote-work.md %}

## Books I've Read

The following are the last five books I've read. Check the full list [here](/books-read).

<ul>
{% assign sorted_books = site.books | sort: 'date_read' | reverse %}
{% for book in sorted_books limit:5 %}
  <li><!-- {% if book.date_read <> "" %}{{ book.date_read }} - {% endif %} --><a href="{{ book.permalink }}">{{ book.title }}</a>, by {{ book.author }}</li>
{% endfor %}
</ul>