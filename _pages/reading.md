---
title: Reading
permalink: /reading
toc: true
toc_sticky: true
---

Here I share my currently reading list, as well as my book recommendations. I also put together the top blogs and newsletters I like to follow to keep up to date.

I have also separate reading lists in the main topics I write about in this blog, such as [leadership](/leadership), [management](/mgmt), and [software engineering management](/mgmt/swe), among others.

## Currently Reading

- {% include books/become-an-effective-swe-manager.md %}
- {% include books/an-elegant-puzzle.md %}
- *[Friend and Foe](https://www.goodreads.com/book/show/24388304-friend-foe)* by Adam Galinsky and Maurice Schweitzer
- *[Numbers don't Lie](https://www.goodreads.com/book/show/50705179-numbers-don-t-lie)* by Vaclav Smil
- *[Engineering Management for the Rest of Us](https://www.goodreads.com/book/show/58502800-engineering-management-for-the-rest-of-us)* by Sarah Drasner. A book we are reading in a *book club* at [VTEX](/about/vtex).

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

## Books I've Read

<ul>
{% for books in site.books reversed %}
  <li><!-- {% if books.date_read <> "" %}{{ books.date_read }} - {% endif %} --><a href="{{ books.permalink }}">{{ books.title }}</a>, by {{ books.author }}</li>
{% endfor %}
</ul>