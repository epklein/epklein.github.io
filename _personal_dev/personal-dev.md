---
title: Personal Development
permalink: /personal-dev
toc: true
toc_sticky: true
---

Personal Development is **the ongoing process of self-awareness and self-improvement** in which we seek to enhance skills and knowledge, develop our careers, improve our quality of life, etc.

This page is a collection of resources I consider relevant about personal development.

## Self-Management

Self-management is a key component of personal development. It refers to our ability to manage our behavior and actions to achieve personal and professional goals. I have a [page dedicated to self-management](/mgmt/self) under the [management](/mgmt) section of this website.

## Career Development

I firmly believe that we all should take ownership of our work and career. Ask yourself, what are your career aspirations? How can your manager and current company support these goals? You should not solely rely on your company or manager to shape your career trajectory. Take charge and own your career path.

A few important concepts:

- **Job Hunting**: Transitioning to a new position, or even a new company, may be the next step in your career development. In that case, you will do some job hunting, which is not just about interviewing well or doing great technical tests. You can improve your chances of getting your next role by carefully searching for positions and companies, adapting your resume accordingly, and using your network to reach out to people from your desired next company. [Don't Miss Your Next Role!](https://www.scarletink.com/using-your-brain-while-job-hunting/) is a great blog post by [Dave Anderson](https://www.linkedin.com/in/scarletink/), an ex-Amazon Tech Director, that I highly recommend. You may also take advantage of [reverse interviewing](https://github.com/viraptor/reverse-interview/tree/master) to understand the company, position, leadership, etc., to learn if a particular position fits your career goals.

## Related Posts

{% for post in site.categories['Personal Development'] %}- {{ post.date | date: "%B %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{% if post.title and post.title != "" %}{{post.title}}{% else %}{{post.excerpt |strip_html}}{%endif%}</a>
{% endfor %}

## Learning

{% include learning/personal-dev.md %}