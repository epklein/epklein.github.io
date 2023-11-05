---
title: Software Engineering Management
permalink: /mgmt/sem
toc: true
toc_sticky: true
---

On this page, I share resources about Software Engineering Management, which I see as **the application of [management](/mgmt) activities focused on the development and maintenance of software**.

## Resources

- [The Software Engineering Manager Role](/mgmt/sem/sem-role): I describe the responsibilities of the role and share resources to help SEMs to develop their skills.

## Related Posts

{% for post in site.categories['SWE Management'] %}- <b>{{ post.date | date: "%b %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></b>. {{post.excerpt |strip_html}}
{% endfor %}

## Learning

{% include learning/sem-mgmt.md %}