---
title: One-on-Ones
permalink: /mgmt/people/one-on-ones
---

This is a valuable individual meeting that a manager keeps to connect regularly to everyone that directly reports to him. Some benefits of running one-on-ones include:

- Connect and build trust with your team. Provide a safe space for them to address difficult conversations in private with you;
- Coach your team towards self-improvement and a successful career;
- Foster organizational culture and your own leadership style;
- Proactively follow-up on goals and KPIs, and address issues.

How you effectively run your one-on-ones may vary, and managers may succeed using different approaches. Even the same manager may use different approaches for different people. But there are some ground rules that usually are applicable:

- It is their meeting, not yours. Practice active listening and let them do most of the talking;
- You may support and challenge them, but do not solve their problems. Use the power of questions to help them arrive at conclusions by themselves;
- Keep a regular schedule, preferably weekly, and avoid rescheduling it;
- It is not a status update meeting, although once in a while you may use for it, to address issues and follow-up on goals.

What you need to get started? Not much, you just need:

- To book a weekly one-to-one
- To have a shared document to keep track of agenda, notes and actions


Running it effectively needs practice, and some guidelines or tips may be of great help. What to talk about during one-one-ones? How to take notes and keep track of it? I'll regularly share in the [blog](/blog) my experience and resources I use to conduct one-on-one meetings.

## Related Posts

{% for post in site.tags['One-on-one'] %}
- {{ post.date | date: "%B %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{% if post.title and post.title != "" %}{{post.title}}{% else %}{{post.excerpt |strip_html}}{%endif%}</a>
{% endfor %}

## Recommended Reading

- {% include book-ref-become-an-effective-swe-manager.md %}