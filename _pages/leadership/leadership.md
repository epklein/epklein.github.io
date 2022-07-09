---
layout: page
title: Leadership
permalink: /leadership
---

This page is a collection of resources I consider relevant about leadership. I understand leadership as **the ability of an individual to influence and guide other people**.

## Related posts

{% for post in site.categories['Delegation'] %}
- {{ post.date | date: "%B %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{% if post.title and post.title != "" %}{{post.title}}{% else %}{{post.excerpt |strip_html}}{%endif%}</a>
{% endfor %}

## Recommended reading

### Books

- **[How to win friends and influence people](https://www.amazon.com/How-Win-Friends-Influence-People/dp/0671027034)**, by [Dale Carnegie](https://en.wikipedia.org/wiki/Dale_Carnegie). It is one of the best-selling books of all time, first published almost a century ago. It is still a relevant reading about influence. A must read for people that want to develop better personal and professional relationships.
- **[Radical Candor](https://www.amazon.com/Radical-Candor-Revised-Kick-Ass-Humanity/dp/1250235375)**, by [Kim Scott](https://kimmalonescott.com/). A reference for managers who want to improve their ability in giving feedback. The book is a collection of ideas on how to give candid feedback, by caring personally and challenging directly.

### Podcasts

- **[The Radical Candor Podcast](https://www.radicalcandor.com/candor-podcast/)**: A podcast from the author of the book **Radical Candor**, with practical tips about giving candid feedback.