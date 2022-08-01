---
title: Feedback
permalink: /mgmt/people/feedback
published: false
---

WIP

Radical Candor concept

Traits to avoid

## Related Posts

{% for post in site.tags['Feedback'] %}
- <a href="{{ site.baseurl }}{{ post.url }}">{% if post.title and post.title != "" %}{{post.title}}{% else %}{{post.excerpt |strip_html}}{%endif%}</a>
{% endfor %}

## Recommended Reading

- {% include book-ref-radical-candor.md %}