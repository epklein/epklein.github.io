---
title: Software Engineering Strategy
permalink: /mgmt/sem/swe-strategy
toc: false
toc_sticky: true
---

A software engineering strategy is a high-level plan or approach designed to achieve specific objectives within software engineering teams and projects. This strategy outlines the challenges, methods, and actions required to overcome these challenges.

The development and implementation of such a strategy can vary. One popular starting point is Richard Rumelt's three pillars of effective strategies from *[Good Strategy, Bad Strategy](https://www.goodreads.com/book/show/11721966-good-strategy-bad-strategy)*. I was first introduced to this approach while reading the book *[An Elegant Puzzle](/book/an-elegant-puzzle)* by {% include people/will-larson.md %}.

According to this approach, a good strategy consists of the following components:

1. **Diagnosis**: The theory describing the challenge at hand, including its factors and constraints, alongwith a problem statement;
2. **Guiding Policies**: These are the policies that will be applied to address the challenge. They describe the general approach taken to tackle the problem;
3. **Actions**: These are the specific steps implemented to address the challenge.

## Applications

From my experience, I have found software engineering strategies useful in two contexts:

1. **Writing guides to help teams tackle specific operational challenges**: I have explored this in [Writing Guides to Support Your Teams](/writing-guides). The diagnosis usually identifies one specific challenge, and the guiding policies and actions are tailored to address that challenge;
2. **Developing mid or long-term software engineering strategies for my team or business unit**: In this context, the strategy explores multiple challenges, identifies the guiding policies and actions to tackle them, and aims to inspire and guide leaders and individual contributors in their work towards common goals.

## Related Posts

{% for post in site.tags['SWE Strategy'] %}- <b>{{ post.date | date: "%b %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></b>. {{post.excerpt |strip_html}}
{% endfor %}

## Learning

{% include learning/swe-strategy.md %}