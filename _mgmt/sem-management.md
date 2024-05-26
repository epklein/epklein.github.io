---
title: Software Engineering Management
permalink: /mgmt/sem
toc: true
toc_sticky: true
---

On this page, I share resources about *Software Engineering Management*, which I see as the application of [management](/mgmt) activities focused on the development and maintenance of software.

These resources are valuable for understanding the critical aspects of managing software engineering teams and projects.

## Resources

- [The Software Engineering Manager Role](/mgmt/sem/sem-role): I describe the responsibilities of Software Engineering Managers (SEMs) and provide resources to help SEMs develop their skills.
- [Software Engineering Strategy](/mgmt/sem/swe-strategy): I gather key learnings, insights, and resources that I find useful for developing effective software engineering strategies.

## Related Posts

{% for post in site.categories['SWE Management'] %}- <b>{{ post.date | date: "%b %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></b>. {{post.excerpt |strip_html}}
{% endfor %}

## Learning

{% include learning/sem-mgmt.md %}