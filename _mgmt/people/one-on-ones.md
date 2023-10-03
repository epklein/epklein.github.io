---
title: One-on-one Meetings
permalink: /mgmt/people/one-on-ones
toc: true
toc_label: "One-on-one Meetings"
toc_sticky: true
# an old blog post that was expanded on this page
redirect_from: /one-on-one-meetings
redirect_from: /one-on-one-meetings/
---

A one-on-one is an individual meeting that a manager keeps to connect regularly to everyone that directly reports to him. It is a powerful tool for professional development. Some benefits of running one-on-ones include:

- Connect and build trust with your team. Provide a safe space for them to address difficult conversations in private with you;
- Coach your team toward self-improvement and a successful career; Help each individual with what they need for short-term performance and long-term growth;
- Foster organizational culture and your own leadership style;
- Proactively follow-up on goals and KPIs;
- Address issues.

## How to get Started

What you need to get started? Not much, you just have to:

- Book a weekly one-on-one;
- Have a [shared document](/mgmt/people/template-one-on-one-shared-document) to keep track of agenda, notes and actions.

## Running the Meeting

How you run your one-on-ones may vary, and managers may succeed using different approaches. Even the same manager may use different approaches for different people. But there are some ground rules that usually are applicable:

- It is their meeting, not yours. Practice active listening and let them do most of the talking;
- You may support and challenge them, but do not solve their problems. Use elicitation techniques to help them arrive at conclusions by themselves;
- Keep a regular schedule, preferably weekly, and avoid rescheduling it;
- It is not a status update meeting, although once in a while you may use it for that, to address issues and follow-up on goals.

You may consider the following when running your one-on-ones:

- Start it with a question such as "*How are you feeling this week?*" or another alternative from [the list of questions below](#questions-to-ask). That's a good start because you want them to talk after all;
- Some status updates may be a bit inevitable in the first minutes but, unless really necessary, try to move away from it as quickly as possible;
- Focus on what they are saying, and move forward with questions that will develop their thoughts. Concentrate to do this effectively, because being a great listener is not easy;
- Have a couple of prepared talking points, if the conversation stagnates, to take the best of this moment. Choose wisely from [the list of topics below](#topics-for-discussion).

### Questions to Ask

It is nice to ask questions that stimulates the conversation. Some questions that you may ask during one-on-ones:

- How are you feeling this week?
- What's on your mind?
- What went well this week/cycle?
- What are your priorities for the next week/cycle?
- What challenges or roadblocks do you need help with?
- How can I help you?

### Topics for Discussion

There are many relevant topics to cover during one-one-ones. Some of them will be discussed more frequently than others.

Remember that you will usually let your direct report prepare the agenda but, depending on the context (a big new project, the end of a cycle, a performance issue, etc.), you may bring some topics to the conversation.

Some interesting topics you may consider exploring during one-on-ones:

**Personal Life**

- Talk about family, children, hobbies, and dreams; life outside work;
- It's essential to connect personally with your team, as we are all human beings;

**Individual Performance**

- Review results delivered and feedback received; provide your feedback on their results;
- Set goals together for the next cycle;

**Teamwork**

- Discuss team performance and work processes;
- *Do you understand your role within the team?*
- *How would you describe the team's meetings and rituals?*

**Career Development**

- Discuss short, medium and long-term career goals; challenge their career aspirations;
- Help them explore learning opportunities;
- *Do you enjoy what you do?*
- *What comes next in your development?*

**Organizational Culture, Strategy and Objectives**

- Share the company's vision and strategy;
- Discuss values and culture;
- *Do you find meaning in what you do?*
- *Do you feel safe at work?*

**For Software Engineers**

- Challenge them to assess and develop relevant hard and soft skills to grow in their careers;
- You may use frameworks and tips from my [SWE career](/mgmt/swe/swe-career) page;

## Taking Notes

Having a shared document is essential to keep track of your one-on-ones and don't get lost.

Some benefits include:

- To prepare the agenda of your next one-on-ones. Both parties should have a document to write down something they don't want to miss the next time they meet;
- Keep track of decisions you made and assigned actions;
- Keep a record of deliveries and achievements;
- Provide your direct reports a source of information that will help them write their *self review* during [performance review cycles](/performance-review-cycle);

I've written a blog post about [taking notes of one-on-ones](/taking-notes-of-one-on-ones) that I highly recommend you reading.

### Templates

- [One-on-one shared document](/mgmt/people/template-one-on-one-shared-document);
- [One-on-one private notes](/mgmt/people/template-one-on-one-private-notes).

## Related Posts

{% for post in site.tags['One-on-one'] %}- {{ post.date | date: "%B %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{% if post.title and post.title != "" %}{{post.title}}{% else %}{{post.excerpt |strip_html}}{%endif%}</a>
{% endfor %}

## Recommended Reading

- {% include books/become-an-effective-swe-manager.md %}
- [HBR: Make the Most of Your One-on-One Meetings](https://hbr.org/2022/11/make-the-most-of-your-one-on-one-meetings)