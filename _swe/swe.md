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

## Design Documents

Design Documents and Request for Comments (RFCs) are tools used by engineering teams to plan non-trivial projects. They are great tools to provide a clear specification and help clarifying the project vision, direction and assumptions across the organization. They facilitate communication and feedback, create documentation, among other benefits. They also work pretty well for asynchronous teams.

A few references:

- [DesignDocs.dev](https://www.designdocs.dev)
- [https://blog.pragmaticengineer.com/rfcs-and-design-docs](https://blog.pragmaticengineer.com/rfcs-and-design-docs)

## Software Architecture

- **Reactive Architecture**: {% include def-reactive-architecture.md %}

### Blog Posts

{% for post in site.tags['Software Architecture'] %}- {{ post.date | date: "%B %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{% if post.title and post.title != "" %}{{post.title}}{% else %}{{post.excerpt |strip_html}}{%endif%}</a>
{% endfor %}

## Learning

{% include learning/swe.md %}