---
layout: page
title: Delegation
permalink: /mgmt/people/delegation
published: true
---

Delegation is the act of giving someone else, or a group of people, authority or responsibility for something. There are many techniques on how to delegate properly, and the best approach may depend on the context.

In [managing software engineering teams](/mgmt/swe), I prefer a delegation approach focused on the results instead of methods. Which takes more time and energy to see results, but develops people abilities and scales in the lon run.

## Related posts

{% for post in site.categories['Delegation'] %}
- <a href="{{ site.baseurl }}{{ post.url }}">{% if post.title and post.title != "" %}{{post.title}}{% else %}{{post.excerpt |strip_html}}{%endif%}</a>
{% endfor %}

## Recommended reading

- [The 7 Habits of Highly Effective People](/books/the-7-habits-of-highly-effective-people) by Stephen Covey.