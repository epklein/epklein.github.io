---
title: Self Management
permalink: /personal-dev/self-mgmt
redirect_from: /mgmt/self
toc: true
toc_sticky: true
---

Managing oneself is essential for personal growth, career development, and effective leadership.

## Time Management

Time management is about mastering how to use our time effectively. It involves goal setting, prioritization, [delegation](/mgmt/people/delegation), and work-life balance, among other things. Check my [personal planning page](/personal-dev/self-mgmt/personal-planning) for more information on this topic.

## Other resources

- How to get your work recognized? You may want to write a [brag document](https://jvns.ca/blog/brag-documents/).

## Related Posts

{% for post in site.categories['Self Management'] %}- <b>{{ post.date | date: "%b %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></b>. {{post.excerpt |strip_html}}
{% endfor %}