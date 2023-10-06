---
title: Software Engineering Management
permalink: /mgmt/swe
toc: true
toc_sticky: true
---

On this page I share resources about Software Engineering Management, which I see as **the application of [management](/mgmt) activities focused on the development and maintenance of software**.

## Responsibilities

A Software Engineering Manager typically:

- Manages the design and development of software applications or services;
- Directs or supports the work of **Software Engineers** to promote the best practices and foster improvement;
- Has a good comprehension of software development, including topics such as programming, testing, building, deploy & delivery, software architecture & design, and many more.

**There are a variety of software development concepts, practices, tools, etc., important to understand**. I intend to write about some of them, such as:

- [DevOps](/swe/devops), [cloud computing](/swe/cloud-computing), microservices, etc.

## Related Posts

{% for post in site.categories['SWE Management'] %}- <b>{{ post.date | date: "%b %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></b>. {{post.excerpt |strip_html}}
{% endfor %}

## Learning

{% include learning/swe-mgmt.md %}