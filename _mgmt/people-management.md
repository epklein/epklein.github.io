---
title: People Management
permalink: /mgmt/people
toc: true
toc_sticky: true
---

In my career I've seen in practice or studied many approaches and styles for managing people and teams. Some I truly believe are helpful for a manager. Some others are obsolete or may work in specific contexts, and some are a complete waste of time in my opinion.

My goal with this page is to share well known people management tools, as well as resources that I've learned along the way and that work for me, in my context as a software engineering manager.

The resources available in this page are being classified informally as I collect and organize data. I'm not following any formal framework or structure.

I try to cover the most important topics in detail in specific pages, and share my experiences about people management in the [blog](/blog).

## Definition

So, first things first: What is people management? Well, my preferred definition is quite simple:

> The act of achieving results through other people.

To achieve that, in any circumstance, you need to influence people to have their cooperation.

## Skills

We hear a lot about *soft skills* in businesses. These are skills not related to the work to be done itself, but social skills needed to connect to other people, to work effectively with them. By developing such skills, you can influence other people and expand your circle of influence, impacting more people to achieve greater results.

Skills I believe are important for a manager to develop include:

- [Communication](/mgmt/people/communication);
- [Delegation](/mgmt/people/delegation);
- Feedback;
- Conflict resolution;

## Processes

Inside a business there are a variety of processes a manager needs to get involved when managing people, such as:

**Recruiting**

The process of attracting, selecting, and hiring the best-suited candidates for open positions within the organization.

**Onboarding**

A comprehensive integration program for new employees, aimed at making them feel welcome, informed, and prepared for their new roles.

**Developing**

Fostering employee growth and skill enhancement through training, mentorship, and professional development opportunities.

Conducting regular [one-on-one meetings](/mgmt/people/one-on-ones) is a widely recognized management practice that nurtures meaningful connections with employees and facilitates their ongoing growth and development.

**Evaluating**

Continuously monitoring, assessing, and providing feedback on an employee's performance, goals, and skills to ensure alignment with organizational objectives.

A [performance review cycle](/performance-review-cycle) is a periodic evaluation of an employee's work performance, aimed at promoting growth, development, and alignment with organizational goals.

**Engaging**

Creating a positive work environment that fosters employee commitment, motivation, and connection to the organization.

## Other Resources

Many more topics may be addressed in the discipline of people management, such as driving outcomes, motivation, performance, situational leadership, stakeholder management, upward management...

In this section I'll try to share resources about other people management topics, and create new pages when I need to delve into any of them.

### Career Development

- [progression.fyi](https://progression.fyi/): As defined in the **/about** page, *progression.fyi is currently a collection of open source and public ‘progression frameworks’, examples of the tools that thousands of managers in tech are building for their teams to ensure that they feel valued at work.*

## Related Posts

{% for post in site.categories['People Management'] %}- {{ post.date | date: "%B %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{% if post.title and post.title != "" %}{{post.title}}{% else %}{{post.excerpt |strip_html}}{%endif%}</a>
{% endfor %}