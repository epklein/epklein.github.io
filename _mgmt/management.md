---
title: Management
permalink: /mgmt
toc: true
toc_sticky: true
---

This page is a collection of resources about **management**. I don't cover everything about a broad discipline such as this. I would certainly fail trying to do so. I focus on relevant topics from my experience as a software engineering manager.

**Let's consider this as my playbook to management**; My best view so far of how to manage **people**, **processes** and **software development** inside tech companies.

## Components

I group management activities in a few components:

- [SWE Management](/mgmt/swe): The management practices focused on the development and maintenance of software.
<!-- Systems health / Technical Vision -->
- [People Management](/mgmt/people): The goal of managing people is to achieve results through other people. For that we need develop people, delegate activities, communicate effectively, etc.;
<!-- People Development / Stakeholder Management -->
- [Team Management](/mgmt/team): To manage teams and deliver results we need to hire, develop and grow; implement processes and measure performance; define strategies, give vision and purpose; etc.;
<!-- Team growth / Team Productivity / Business Impact -->
- [Self Management](/mgmt/self): To manage other people we need first learn to manage ourselves. Plan our goals, priorities, agenda, routines, development, etc.;

## Related Posts

{% for post in site.categories['Management'] %}- {{ post.date | date: "%B %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{% if post.title and post.title != "" %}{{post.title}}{% else %}{{post.excerpt |strip_html}}{%endif%}</a>
{% endfor %}

## Learning

{% include learning/management.md %}