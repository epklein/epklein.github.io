---
title: Software Engineering
permalink: /swe
toc: true
toc_sticky: true
---

Software engineering is a branch of computer science that deals with the design, development, implementation, and maintenance of software systems.

It is a systematic, disciplined approach to applying engineering principles to the development, operation, and maintenance of software, with a focus on providing cost-effective software solutions that are reliable and work efficiently

## Resources

- [Software Development Lifecycle (SDLC)](/swe/sdlc): A systematic process that guides teams and organizations in delivering high-quality software.
- [DevOps](/swe/devops): A combination of culture, practices, and tools that integrates and automates software development and operational processes so that companies can plan, develop, deliver, and operate faster and reliably.
- [Cloud Computing](/swe/cloud-comuting): The on-demand availability of computer resources online, through the internet, without the need of management of physical infrastructure by the consumer.

## Software Architecture

- [Reactive Architecture](/reactive-architecture): A paradigm that focuses on building highly responsive, resilient, and scalable systems. It is designed to handle the challenges of modern distributed systems, such as taking care of a large number of users while ensuring low latency and maintaining high availability.

### Related Posts

{% for post in site.tags['Software Architecture'] %}- <b>{{ post.date | date: "%b %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></b>. {{post.excerpt |strip_html}}
{% endfor %}

## Learning

{% include learning/swe.md %}