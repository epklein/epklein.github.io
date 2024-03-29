---
title: Communication
permalink: /mgmt/people/communication
toc: true
toc_label: "Communication"
toc_sticky: true
---

*The ability to convey information clearly, listen actively, and adapt one's communication style to suit different situations and audiences.*

This page is a collection of resources I consider relevant to effective communication.

## Neuro-linguistic programming

Neuro-linguistic programming (NLP) is a psychological approach that focuses on analyzing strategies employed by successful individuals and applying these strategies to communication, [personal development](/personal-dev), and psychotherapy. It was first developed by [Richard Bandler](https://en.wikipedia.org/wiki/Richard_Bandler) and [John Grinder](https://en.wikipedia.org/wiki/John_Grinder).

It's important to note that NLP has faced criticism and is often labeled as pseudoscience due to a lack of scientific validation.

Despite this, I have an NLP background (holding an NLP Practitioner certification) and believe that it offers valuable tools to enhance communication. This is the reason I explore it on the site.

{% assign sorted_posts = site.tags['NLP'] | sort: "title" %}
{% for post in sorted_posts %}- <b><a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></b>. {{post.excerpt |strip_html}}
{% endfor %}

## Mediums of Communication

Communication can occur through several mediums, and its choice can significantly influence the effectiveness of the communication.

### Verbal

This is the most common medium for us as human beings. **It refers to using words and speaking to convey information between individuals synchronously**. It can be face-to-face, over the telephone, or even over a video call.

It is a natural and effective form of communication, allowing for real-time feedback and exchange of ideas. **Its effectiveness depends on many aspects, including listening skills, oratory, emotional intelligence, and interpersonal skills**.

I already wrote about verbal communication in the blog, such as in [Enjoy Better Conversations](/enjoy-better-conversations).

### Written

**This involves any type of interaction that uses the written word**. It is a fundamental method in business and personal settings and includes formats like documents, letters, e-mails, text messages, etc.

Written communication provides a permanent record of information, effective for complex instructions or information that needs to be referenced over time.

**In many modern businesses, written communication is critical to allowing distributed and asynchronous work to happen effectively**. In the Tech industry, we are used to working asynchronously in teams by communicating over instant messaging apps and e-mail, iterating over documents and source code, managing projects through digital documents, etc.

### Non-Verbal

**It involves conveying messages without the use of words**. It may include body language, gestures, vocal variety, etc.

**Non-verbal communication usually accompanies verbal communication and can reinforce or contradict the spoken message**. Understanding and effectively using non-verbal cues is crucial for effective communication.

Watch the video I shared in a blog post about [Effective Communication](/effective-communication) to see an example of non-verbal communication effectively used.

## Related Posts

{% for post in site.tags['Communication'] %}{% unless post.tags contains 'NLP' %}- <b>{{ post.date | date: "%b %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></b>. {{post.excerpt |strip_html}}{% endunless %}
{% endfor %}

## Learning

{% include learning/communication.md %}