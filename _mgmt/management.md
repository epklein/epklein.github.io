---
title: Management
permalink: /mgmt
toc: true
toc_sticky: true
---

Management is a broad discipline. On this page I share resources and references covering a variety of management branches.

I have a special page dedicated to [Software Engineering Management](/mgmt/swe), the main focus of my career.

## Management Branches

- [People Management](/mgmt/people): {% include def-people-mgmt.md %}
- [SWE Management](/mgmt/swe): {% include def-swe-mgmt.md %}

## Related Posts

{% for post in site.categories['Management'] %}- {{ post.date | date: "%B %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{% if post.title and post.title != "" %}{{post.title}}{% else %}{{post.excerpt |strip_html}}{%endif%}</a>
{% endfor %}

## Learning

{% include learning/management.md %}