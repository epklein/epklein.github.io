---
title: Leadership
permalink: /leadership
---

This page is a collection of resources I consider relevant about leadership. I understand leadership as **the ability of an individual to influence and guide other people**.

## Related Posts

{% for post in site.tags['Leadership'] %}
- {{ post.date | date: "%B %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{% if post.title and post.title != "" %}{{post.title}}{% else %}{{post.excerpt |strip_html}}{%endif%}</a>
{% endfor %}

## Recommended Reading

### Books

- {% include book-ref-how-to-win-friends-and-influence-people.md %}
- {% include book-ref-radical-candor.md %}

### Podcasts

- **[The Radical Candor Podcast](https://www.radicalcandor.com/candor-podcast/)**: A podcast from the author of the book **Radical Candor**, with practical tips about giving candid feedback.