---
title: Continuous Delivery
permalink: /swe/devops/cd
---

Continuous Delivery (CD) is at the heart of [DevOps](/swe/devops) and is one of the fundamental software engineering practices that modern companies use to deliver software *quickly* and *reliably*. 

It comprises of a set of principles and foundations that creates many feedback loops in the development process, to ensure we are building high-quality software that gets delivered *frequently* and *reliably*.

## Principles

There are five key principles at the heart of CD:

1. **Build quality in**: We invest in people and tools, to detect issues quickly, and fix them in earlier stages, where they are cheap to resolve;
2. **Work in small batches**: The goal is to work in smaller chunks to deliver business outcomes quickly for a small part of our target audience to collect feedback;
3. **Computers perform repetitive tasks; people solve problems**: By automating repetitive work that takes a long time, we reduce the cost of pushing out changes and we free up people for higher-value work;
4. **Relentlessly pursue continuous improvement**: High-performing teams are never satisfied. They make improvement a daily routine;
5. **Everyone is responsible**: System-level outcomes (throughput, quality, stability, etc.) are well aligned with business outcomes. Everyone works towards measurable, achievable, time-bound goals to achieve them.

## Foundations

To implement CD, we must create the following foundations:

- **Comprehensive configuration management**: It should be possible to build, test, and deploy our software, and provision our environments, in a fully automated way, from data stored completely in version control;
- **Continuous Integration (CI)**: Each change in the codebase should trigger a build process that includes running unit tests;
- **Continuous testing**: We should be testing all the time as an integral part of the development process. Developers should be able to run all automated tests on their workstations; Automated tests should be run against every change in the codebase to give developers fast feedback.

## Related Posts

{% for post in site.tags['Continuous Delivery'] %}- {{ post.date | date: "%B %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{% if post.title and post.title != "" %}{{post.title}}{% else %}{{post.excerpt |strip_html}}{%endif%}</a>
{% endfor %}

## Recommended Reading

- {% include books/accelerate.md %}