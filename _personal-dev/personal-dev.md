---
title: Personal Development
permalink: /personal-dev
toc: true
toc_sticky: true
---

*The ongoing process of self-awareness and self-improvement in which we seek to enhance skills and knowledge, develop our careers, improve our quality of life, and more.*

## Personal Development Resources

In the ever-evolving journey of personal development, there are countless skills to be mastered and useful tools to be explored. Bellow is a collection of resources I share on this website, handpicked to support and inspire your growth journey.

- [Self-Management](/personal-dev/self-mgmt): It refers to our ability to manage our behavior and actions to achieve personal and professional goals;
- [Career Development](/personal-dev/career-dev): It encompasses the actions, decisions, and planning involved in managing our professional growth;
- [Mentoring](/personal-dev/mentoring): It is a collaborative process, a knowledge-sharing relationship where an experienced individual, the mentor, provides guidance, support, and wisdom to a less experienced individual, the mentee.

## Related Posts

{% for post in site.categories['Personal Development'] %}- <b>{{ post.date | date: "%b %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></b>. {{post.excerpt |strip_html}}
{% endfor %}

## Learning

{% include learning/personal-dev.md %}