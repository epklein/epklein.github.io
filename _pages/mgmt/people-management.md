---
layout: page
title: People Management
permalink: /mgmt/people
published: true
---

In my career I've seen in practice or studied many approaches and styles for managing people and teams. Some I trully believe are helpful as a manager. Some others are obsolete or may work in specific contexts, and some are a complete waste of time in my opinion.

But what is exactly people management? Well, my prefered definition is quite simple:

**People Management is the act of achieving results through other people.**

And to master this discipline, we need to develop many abilities, such as:

- **Skills**: [communication](/mgmt/people/communication), [delegation](/mgmt/people/delegation), [feedback](mgmt/people/feedback), conflict resolution, ...
- **Processes**: hiring, onboarding, developing, evaluating, engaging, ...

And many more important topics, such as driving outcomes, motivation, performance, one-on-one meetings, situational leadership, stakeholder management, upward management...

I try to cover the most important topics in detail in specific pages, and share my experiences about people management in the [blog](/blog).

## Related posts

{% for post in site.categories['People Management'] %}
- {{ post.date | date: "%B %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{% if post.title and post.title != "" %}{{post.title}}{% else %}{{post.excerpt |strip_html}}{%endif%}</a>
{% endfor %}