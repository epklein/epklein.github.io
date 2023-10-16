---
title: Delegation
permalink: /mgmt/people/delegation
toc: true
toc_sticky: true
---

Delegation is **the ability to assign tasks or responsibility to an individual or a group of people, empower them to make decisions, and trust them to complete work effectively**.

In [managing software engineering teams](/mgmt/swe), I favor a delegation approach focused on the desired results rather than on the specific methods and steps required to achieve them. It takes more time and energy to see results, but develops people abilities and scales in the long run.

A key concept I consider crucial is understanding that **delegating is not a binary process**; it's not simply something you do or don't do. Instead, it **it is multifaceted process that you can navigate in many levels**. Successfully steering through these levels can be transformative. It allows you to allocate more time to meaningful work without loosing control. Furthermore, it fosters expertise and autonomy in others, setting the stage to improve team performance and greater organizational impact.

The following are a few concepts that are useful to better navigate the delegation process.

## Responsibility x Accountability

**Responsibility is the obligation to complete specific tasks or projects**, typically based on the individual's role.

On the other hand, **accountability is the state of being answerable for the outcomes of those tasks and projects**. It encompasses the consequences, both positive and negative, for the outcomes.

The general principle is: **You can delegate responsibility, but you cannot delegate accountability**.

You cannot blame your team for the failure of a project for which you were held accountable by your management. Simply put, your team's failure is also your failure.

Thus, when delegating, keep the following in mind:

- **Set up for success**: Consider the maturity of your team. Determine the appropriate level of delegation to ensure their success and employ the right tools to facilitate it. In subsequent sections I will provide guidance on this.
- **Establish accountability**: While you retain overall accountability, clearly define the standards of performance for the delegated task or project. Communicate the expectations, and specify the consequences, both positive and negative, based on the evaluation of results.

## Maturity x Authority

In *[Management 3.0](https://www.goodreads.com/book/show/10210821-management-3-0)*, [Jurgen Appelo](https://jurgenappelo.com/) offers an approach to see delegation as a relationship of maturity and authority.

He brings the idea that delegating effectively to empower teams is a factor of understanding both the level of maturity of the person or group that the task is being delegated to, and the level of authority the manager may apply depending on the impact and risks of the task in hand.

![Delegation maturity and authority levels. How to Empower Teams: Management 3.0, by Jurgen Appelo](/images/mgmt-delegation-mgmg30.png "How to Empower Teams: Management 3.0, by Jurgen Appelo")

## Delegation Scales

Another way to see delegation is that of a process of many levels. You choose the appropriate level of responsibility you delegate to someone.

In *[Become an Effective Software Engineering Manager](https://www.goodreads.com/book/show/50363684-become-an-effective-software-engineering-manager)*, {% include people/james-stanier.md %} shares the following scale of delegation to understand where we are and where we can go in the delegation process.

![The scale of delegation. Become an Effective Software Engineering Manager, by James Stanier](/images/mgmt-delegation-james-stanier.png "Become an Effective Software Engineering Manager, by James Stanier")

From [The Situational Leadership model](https://en.wikipedia.org/wiki/Situational_leadership_theory) we have another scale that I like, in which we adjust the delegation style to the following four levels:

- **Telling**: Giving specific instructions and closely supervising performance.
- **Selling**: Providing direction and using persuasion.
- **Participating**: Sharing ideas and facilitating the decision-making process.
- **Delegating**: Turning over responsibility for decisions and execution.

## Tools and Approaches

There are many tools that support the delegation process. Some popular include:

- **SMART model**: A model to delegate tasks that are based on the five words that compose the acronym: Specific, measurable, agreed upon, realistic, and time-based.
- **RACI matrix**: A responsibility assignment matrix that helps in clarifying roles. It stands for responsible, accountable, consulted, and informed.
- **[Stewardship delegation](/stewardship-delegation)**: A delegation approach focused on results that establishes up-front mutual understanding and commitment regarding expectations in five areas: desired results, guidelines, resources, accountability, and consequences. <!-- This is the blog post excerpt -->

## Related Posts

There are much more to say about delegation, many techniques on how to delegate properly, and the best approach may depend on the context. You can read more about some techniques on how to delegate in the *blog*, under the [Delegation](/tags#delegation) tag.

{% for post in site.tags['Delegation'] %}- <b>{{ post.date | date: "%b %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></b>. {{post.excerpt |strip_html}}
{% endfor %}

## Recommended Reading

- [Management 3.0](https://www.goodreads.com/book/show/10210821-management-3-0), by Jurgen Appelo.
- [The 7 Habits of Highly Effective People](/book/the-7-habits-of-highly-effective-people) by Stephen Covey.