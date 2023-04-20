---
title: Software Engineering
permalink: /swe
toc: true
toc_sticky: true
---

<!-- This page is a WIP -->

For now this page is just a collection of useful resources.

## Culture and Practices

- **DevOps**: {% include def-swe-devops.md %}

## Software Architecture

{% for post in site.tags['Software Architecture'] %}- {{ post.date | date: "%B %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{% if post.title and post.title != "" %}{{post.title}}{% else %}{{post.excerpt |strip_html}}{%endif%}</a>
{% endfor %}

## Learning

{% include learning/swe.md %}