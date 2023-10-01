---
title: People Management
permalink: /mgmt/people
toc: true
toc_sticky: true
---

The goal of people management is to achieve results through others. To accomplish this we must lead and develop people. While it may sound simple, it requires a broad skill set that includes effective communication, leadership, and influence.

Throughout my career I've seen in practice or studied various approaches and styles for managing people and teams. Some I believe are helpful for managers, while others I don't. On this page I share what I've learned along the way that has worked for me in my context as a software engineering manager.

The resources available on this page are informally classified as I gather and organize information. I strive to cover the most important topics in detail on specific pages and share my experiences about people management in the [blog](/blog).

## People Skills

We hear a lot about *soft skills* in businesses. These are interpersonal or people skills needed to connect to other people, to interact effectively and harmoniously with them. By developing such skills, you can influence others and expand your circle of influence, impacting more people to achieve greater results.

Skills I believe are important for a manager to develop include:

- [Leadership](/leadership): the ability to inspire, influence and guide other people towards the accomplishment of common goals and objectives;
- [Communication](/mgmt/people/communication): the ability to convey information clearly, listen actively, and adapt one's communication style;
- [Delegation](/mgmt/people/delegation): the ability to assign tasks or responsibility to individuals, and to empower and trust them to complete work effectively;
- Emotional Intelligence;
- Feedback;
- Conflict resolution;

## People Processes

Inside a business there are a variety of processes a manager needs to get involved when managing people, such as:

- **Recruiting**: The process of attracting, selecting, and hiring the best-suited candidates for open positions within the organization.
- **Onboarding**: A comprehensive integration program for new employees, aimed at making them feel welcome, informed, and prepared for their new roles.
- **Developing**: Fostering employee growth and skill enhancement through training, mentorship, and professional development opportunities.
    - Conducting regular [one-on-one meetings](/mgmt/people/one-on-ones) is a widely recognized management practice that nurtures meaningful connections with employees and facilitates their ongoing growth and development.
- **Evaluating**: Also known as [Performance Management](/mgmt/people/performance), it is the process of continuously monitoring, assessing, and providing feedback on an employee's performance, goals, and skills to ensure alignment with organizational objectives.
- **Engaging**: Creating a positive work environment that fosters employee commitment, motivation, and connection to the organization.

## Other Resources

Many more topics may be addressed in the discipline of people management, such as driving outcomes, motivation, performance, stakeholder management, upward management...

In this section I'll try to share resources about other people management topics, and create new pages when I need to delve into any of them.

### Career Development

- [progression.fyi](https://progression.fyi/): As defined in the **/about** page, *progression.fyi is currently a collection of open source and public ‘progression frameworks’, examples of the tools that thousands of managers in tech are building for their teams to ensure that they feel valued at work.*

## Related Posts

{% for post in site.categories['People Management'] %}- {{ post.date | date: "%B %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{% if post.title and post.title != "" %}{{post.title}}{% else %}{{post.excerpt |strip_html}}{%endif%}</a>
{% endfor %}