---
title: Leadership
permalink: /leadership
toc: true
toc_sticky: true
---

This page is a collection of resources I consider relevant about leadership. I understand leadership as **the ability of an individual to influence and guide other people**.

## Related Posts

{% for post in site.categories['Leadership'] %}
- {{ post.date | date: "%B %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{% if post.title and post.title != "" %}{{post.title}}{% else %}{{post.excerpt |strip_html}}{%endif%}</a>
{% endfor %}

## Learning

{% include learning/leadership.md %}