---
title: Reading
permalink: /reading
toc: true
toc_sticky: true
author_profile: true
---

I share my current reading list and book recommendations on this page. I also put together the top blogs and newsletters I like to follow to stay up to date.

I have separate reading lists for the main topics I write about in the [blog](/). Just access a section from the top menu and navigate to the Learning section.

## Currently Reading

- *[Numbers Don't Lie](https://www.goodreads.com/book/show/50705179-numbers-don-t-lie)* by Vaclav Smil
- *[Designing Data-Intensive Applications](https://www.goodreads.com/book/show/23463279-designing-data-intensive-applications)* by Martin Kleppmann
- *[Thinking in Systems](https://www.goodreads.com/book/show/3828902-thinking-in-systems)* by Donella H. Meadows
- *[The Intelligent Investor](https://www.goodreads.com/book/show/106835.The_Intelligent_Investor)* by Benjamin Graham
- {% include books/the-engineering-executives-primer.md %}

*You can also find my updated list on [Goodreads](https://www.goodreads.com/review/list/29886397-eduardo-klein?shelf=currently-reading)*.

### Reading List

Books that are next on my reading list:

- {% include books/become-an-effective-swe-manager.md %}
- {% include books/effective-remote-work.md %}

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

## Books I've Read

The following are the last five books I've read. Check the full list [here](/books-read).

<ul>
{% assign sorted_books = site.books | sort: 'date_read' | reverse %}
{% for book in sorted_books limit:5 %}
  <li><!-- {% if book.date_read <> "" %}{{ book.date_read }} - {% endif %} --><a href="{{ book.permalink }}">{{ book.title }}</a>, by {{ book.author }}</li>
{% endfor %}
</ul>