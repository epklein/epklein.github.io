---
title: Communication
permalink: /leadership/communication
toc: true
toc_sticky: true
redirect_from: /mgmt/people/communication
---

*The ability to convey information clearly, listen actively, and adapt one's communication style to suit different situations and audiences.*

This page is a collection of resources I consider relevant to effective communication.

## Resources

- [Mediums of Communication](/leadership/communication/mediums): Communication can occur through several mediums, and its choice can significantly influence the effectiveness of the communication.
- [Neuro-Linguistic Programming](/leadership/communication/nlp): A psychological approach that explores connections between neurological processes, language, and behavioral patterns to improve communication.

## Related Posts

{% for post in site.tags['Communication'] %}{% unless post.tags contains 'NLP' %}- <b>{{ post.date | date: "%b %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></b>. {{post.excerpt |strip_html}}{% endunless %}
{% endfor %}

## Learning

{% include learning/communication.md %}