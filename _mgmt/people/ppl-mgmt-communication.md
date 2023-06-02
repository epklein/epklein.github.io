---
title: Communication
permalink: /mgmt/people/communication
toc: true
toc_label: "Communication"
toc_sticky: true
---

Communication is **the ability to convey information clearly, listen actively, and adapt one's communication style to suit different situations and audiences**.

This page is a collection of resources I consider relevant about communication.

## Related Posts

{% for post in site.tags['Communication'] %}- {{ post.date | date: "%B %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{% if post.title and post.title != "" %}{{post.title}}{% else %}{{post.excerpt |strip_html}}{%endif%}</a>
{% endfor %}

## Learning

{% include learning/communication.md %}