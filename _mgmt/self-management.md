---
title: Self Management
permalink: /mgmt/self
toc: true
toc_sticky: true
---

Managing oneself is essential for personal growth, career development, and effective leadership.

## Time Management

Time management is about mastering how to use our time effectively. It involves goal setting, prioritization, [delegation](/mgmt/people/delegation), and work-life balance, among other things. Check my [personal planning page](/mgmt/self/personal-planning) for more information on this topic.

## Other resources

- How to get your work recognized? You may want to write a [brag document](https://jvns.ca/blog/brag-documents/).

## Related Posts

{% for post in site.categories['Self Management'] %}- {{ post.date | date: "%B %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{% if post.title and post.title != "" %}{{post.title}}{% else %}{{post.excerpt |strip_html}}{%endif%}</a>
{% endfor %}