---
title: Software Engineering Management
permalink: /mgmt/swe
toc: true
toc_sticky: true
---

On this page I share resources about **Software Engineering  Management**. But what is is it exactly? Well, I don't have a formal definition for it, but I see it as:

> {% include def-swe-mgmt.md %}
 
Do you have a better definition for it? Please let me know!

## Responsibilities

A Software Engineering Manager typically:

- Manages the design and development of software applications or services;
- Directs or supports the work of **Software Engineers** to promote the best practices and foster improvement;
- Has a good comprehension of software development, including topics such as programming, testing, building, deploy & delivery, software architecture & design, and many more.

**There are a variety of software development concepts, practices, tools, etc., important to understand**. I intend to write about some of them, such as:

- [DevOps](/swe/devops), [cloud computing](/swe/cloud-computing), microservices, etc.

## Related Posts

{% for post in site.categories['SWE Management'] %}
- {{ post.date | date: "%B %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{% if post.title and post.title != "" %}{{post.title}}{% else %}{{post.excerpt |strip_html}}{%endif%}</a>
{% endfor %}

## Learning

{% include learning/swe-mgmt.md %}