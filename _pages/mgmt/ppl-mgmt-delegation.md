---
layout: page
title: Delegation
permalink: /mgmt/people/delegation
published: true
---

Delegation is **the act of giving someone else, or a group of people, authority and responsibility for something**.

<!-- Write about responsibility x accountability.  The first you may delegate, but the second you don't -->
<!-- Write about some frameworks for leveling delegation. Delegation x Control -->

In [managing software engineering teams](/mgmt/swe), I prefer a delegation approach focused on the results instead of methods. Which takes more time and energy to see results, but develops people abilities and scales in the long run.

At a higher level, I think it is important to understand that **delegating is not a binary process**, that you do or you don't do. In fact **it is a process that you can navigate in many levels**, as you can see in the following two models.

In [Management 3.0](https://amzn.to/3OtbXdZ), [Jurgen Appelo](https://jurgenappelo.com/) brings the idea that delegating effectivelly to empower teams is a factor of understanding both the level of maturity of the person or group that the task is being delegated to, and the level of authority the manager may apply depending on the impact and risks of the task in hand.

![Delegation maturity and authority levels. How to Empower Teams: Management 3.0, by Jurgen Appelo](/images/mgmt-delegation-mgmg30.png "How to Empower Teams: Management 3.0, by Jurgen Appelo")

In [Become an Effective Software Engineering Manager](https://amzn.to/3IVcnsl), [James Stanier](https://www.linkedin.com/in/jstanier) shares the following scale of delegation to understand where we are and where we can go in the delegation process.

![The scale of delegation. Become an Effective Software Engineering Manager, by James Stanier](/images/mgmt-delegation-james-stanier.png "Become an Effective Software Engineering Manager, by James Stanier")

<br />

There are much more to say about delegation, many techniques on how to delegate properly, and the best approach may depend on the context. You can read more about some techniques on how to delegate in the [blog](/blog). For that, check the related posts section below.

## Related posts

{% for post in site.categories['Delegation'] %}
- {{ post.date | date: "%B %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{% if post.title and post.title != "" %}{{post.title}}{% else %}{{post.excerpt |strip_html}}{%endif%}</a>
{% endfor %}

## Recommended reading

- [Management 3.0](https://amzn.to/3OtbXdZ), by Jurgen Appelo.
- [The 7 Habits of Highly Effective People](/books/the-7-habits-of-highly-effective-people) by Stephen Covey.