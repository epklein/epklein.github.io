---
title: Leadership
permalink: /leadership
toc: true
toc_sticky: true
---

Leadership is **the ability of an individual to inspire, influence, and guide others toward the accomplishment of common goals and objectives**.

This page is a collection of resources I consider relevant to leadership. 

## Resources

- [Communication](/leadership/communication): A key leadership skill. It is the primary means through which leaders inspire and influence others.
- [Leadership Styles](/leadership/styles): The distinct approaches to guiding, motivating, and managing teams, which are characterized by varying degrees of authority, [delegation](/mgmt/people/delegation), collaboration, and communication strategies.

## Related Posts

{% for post in site.categories['Leadership'] %}- <b>{{ post.date | date: "%b %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></b>. {{post.excerpt |strip_html}}
{% endfor %}

## Learning

{% include learning/leadership.md %}