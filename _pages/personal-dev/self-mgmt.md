---
title: Self Management
permalink: /personal-dev/self-mgmt
redirect_from: /mgmt/self
toc: true
toc_sticky: true
---

Managing oneself is essential for personal growth, career development, and effective leadership.

## Time Management

Time management is about mastering how to use our time effectively. It involves goal setting, prioritization, [delegation](/mgmt/people/delegation), and work-life balance, among other things.

Some useful methods and frameworks that can be used to boost productivity:

1. **[The Eisenhower Matrix](/eisenhower-matrix)**: A popular time management tool that can help you to get organized and execute around priorities. The main idea of this method is to categorize priorities around urgency and priority in a 2x2 matrix.
2. **The Ivy Lee Method**: A classic productive method designed by Ivy Lee and popularized by Charles M. Schwab. It consists of listing the six most crucial tasks to accomplish the next day, prioritizing them, and working through each in order of importance.
3. **The 3-3-3 method**: Yet another method to prioritize tasks to accomplish the next day: three hours on the most critical tasks, three shorter tasks, and three maintenance activities.
4. **Work batches**: An approach to organizing your schedule by proactively allocating longer periods of time (2+ hours) to focus on similar tasks to achieve flow and better performance. I've written about it on my [personal planning page](/personal-dev/self-mgmt/personal-planning).

## Other resources

- How do you get your work recognized? You may want to write a [brag document](https://jvns.ca/blog/brag-documents/).
- [How to set Priorities?](https://newsletter.techworld-with-milan.com/p/how-to-set-priorities) A great article by [Milan Milanovic](https://www.linkedin.com/in/milanmilanovic/).

## Related Posts

{% for post in site.categories['Self Management'] %}- <b>{{ post.date | date: "%b %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></b>. {{post.excerpt |strip_html}}
{% endfor %}