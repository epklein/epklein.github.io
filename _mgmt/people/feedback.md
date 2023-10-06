---
title: Feedback
permalink: /mgmt/people/feedback
published: false
---

WIP

Radical Candor concept

Traits to avoid

## Related Posts

{% for post in site.tags['Feedback'] %}- <b>{{ post.date | date: "%b %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></b>. {{post.excerpt |strip_html}}
{% endfor %}

## Recommended Reading

- {% include book-ref-radical-candor.md %}