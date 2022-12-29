---
title: Communication
permalink: /mgmt/people/communication
toc: true
toc_label: "Communication"
toc_sticky: true
---

<!-- This page is a WIP -->

For now this page is just a collection of useful resources about communication.

## Mediums of communication

- Spoken, Written, Nonverbal
- Sync x Assync

## Related Posts

{% for post in site.tags['Communication'] %}
- {{ post.date | date: "%B %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{% if post.title and post.title != "" %}{{post.title}}{% else %}{{post.excerpt |strip_html}}{%endif%}</a>
{% endfor %}

## Recommended Reading

- {% include books/how-to-win-friends-and-influence-people.md %}
- {% include books/radical-candor.md %}