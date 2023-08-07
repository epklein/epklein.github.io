---
title: Personal Development
permalink: /personal-dev
toc: true
toc_sticky: true
---

Personal Development is **the ongoing process of self-awareness and self-improvement** in which we seek to enhance skills and knowledge, develop our careers, improve our quality of life, etc.

This page is a collection of resources I consider relevant about personal development.

## Dimensions

There are many tools & skills to consider for Personal Development:

- [Self-Management](/personal-dev/self-mgmt): It refers to our ability to manage our behavior and actions to achieve personal and professional goals
- [Career Development](/personal-dev/career-dev): It encompasses the actions, decisions, and planning involved in managing our professional growth
- [Mentoring](/personal-dev/mentoring): It is a collaborative process, a knowledge-sharing relationship where an experienced individual, the mentor, provides guidance, support, and wisdom to a less experienced individual, the mentee

## Related Posts

{% for post in site.categories['Personal Development'] %}- {{ post.date | date: "%B %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{% if post.title and post.title != "" %}{{post.title}}{% else %}{{post.excerpt |strip_html}}{%endif%}</a>
{% endfor %}

## Learning

{% include learning/personal-dev.md %}