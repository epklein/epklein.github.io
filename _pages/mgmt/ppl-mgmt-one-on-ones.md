---
layout: page
title: One-on-Ones
permalink: /mgmt/people/one-on-ones
published: false
---

WIP

Considering "Become an Effective Software Engineering Manager"

What you need

- Book a weekly one-to-one
- Have a shared document to keep track of agenda

Questions for first one-one-ones

1. Which Areas Would You Like the Most Support With?
2. How Would You Like to Receive Feedback and Support?
3. What Could Be a Challenge of Us Working Together?
4. How Might We Know if the Support I’m Offering Isn’t Going Well?
5. How Confidential Is the Content of Our Meetings?

What to talk about?

- Observations from the past week
- A deep dive
- Updates
- Coaching

Leading questions

- “How has your work been going this week?”
- “What are you working on today?”
- “Tell me about those production issues we had last week.”
- “Do you think that we’re measuring our uptime well enough?”
- “How are you feeling about our deadline in June?”
- “How best could we ensure that we’ve got all of the right metrics being logged ahead of time?”

Ideas for topics

- Architecture deep dives
- Process deep dives
- A relevant article you've seen
- Teaching
- The department or company direction
- Collecting feedback
- Sharing a task you're working on

How to take notes

- Prepare notes ahead of meeting
- Put actions in to-do list

## Related posts

{% for post in site.categories['One-on-Ones'] %}
- <a href="{{ site.baseurl }}{{ post.url }}">{% if post.title and post.title != "" %}{{post.title}}{% else %}{{post.excerpt |strip_html}}{%endif%}</a>
{% endfor %}

## Recommended reading

- 