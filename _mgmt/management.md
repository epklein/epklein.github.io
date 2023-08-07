---
title: Management
permalink: /mgmt
toc: true
toc_sticky: true
---

This page is a collection of resources about **management**. I don't cover everything about such a broad discipline; I would certainly fail to attempt to do so. Instead, I focus on relevant topics from my experience as a software engineering manager.

**Consider this my management playbook**; my current, best understanding of how to manage **people**, **processes**, and **software development** within tech companies.

## Components

I've grouped management activities into the following components:

<!-- Systems health / Technical Vision -->
- [SWE Management](/mgmt/swe): The management practices focused on the development and maintenance of software.
<!-- People Development / Stakeholder Management -->
- [People Management](/mgmt/people): The goal of managing people is to achieve results through others. To do this, we must develop people, delegate tasks, communicate effectively, etc.
<!-- Team growth / Team Productivity / Business Impact -->
- [Team Management](/mgmt/team): In order to manage teams and deliver results, we need to: hire, develop, and grow people; implement processes and measure performance; define strategies and give vision and purpose, etc.
- [Self Management](/mgmt/self): Before we can manage others, we must first learn to manage ourselves. This includes planning our goals, priorities, schedules, routines, and [personal development](/personal-dev).

## Related Posts

{% for post in site.categories['Management'] %}- {{ post.date | date: "%B %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{% if post.title and post.title != "" %}{{post.title}}{% else %}{{post.excerpt |strip_html}}{%endif%}</a>
{% endfor %}

## Learning

{% include learning/management.md %}