---
title: Software Engineering
permalink: /swe
toc: true
toc_sticky: true
---

Software engineering is a branch of computer science that deals with the design, development, implementation, and maintenance of software systems.

It is a systematic, disciplined approach to applying engineering principles to the development, operation, and maintenance of software, with a focus on providing cost-effective software solutions that are reliable and work efficiently
 
## Culture and Practices

### DevOps

{% include def-swe-devops.md %}

## Software Architecture

- **Reactive Architecture**: {% include def-reactive-architecture.md %}

### Blog Posts

{% for post in site.tags['Software Architecture'] %}- {{ post.date | date: "%B %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{% if post.title and post.title != "" %}{{post.title}}{% else %}{{post.excerpt |strip_html}}{%endif%}</a>
{% endfor %}

## Learning

{% include learning/swe.md %}