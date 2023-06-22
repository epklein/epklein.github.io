---
title: Self Management
permalink: /mgmt/self
toc: true
toc_sticky: true
---

Managing oneself is essential for personal growth, career development, and effective leadership.

On this page, I'm gathering a list of skills and practices that I consider not only relevant but also extremely beneficial when it comes to managing oneself.

## Skills and Practices

1. **Time Management**: This is about mastering how to use your time effectively. It involves goal setting, prioritization, [delegation](/mgmt/people/delegation), and work-life balance, among other things. Check my [personal planning page](/mgmt/self/personal-planning) for more information on this topic.
2. **Career Development**: I am a firm believer that we all should take ownership of our work and career. Ask yourself, what are your career aspirations? How can your manager and current company support these goals? Remember, you should not solely rely on your company or manager to shape your career trajectory. Take charge and own your career path.

Stay tuned, as more will be added to this list sooner than later.

## Other resources

- How to get your work recognized? You may want to write a [brag document](https://jvns.ca/blog/brag-documents/).

## Related Posts

{% for post in site.categories['Self Management'] %}- {{ post.date | date: "%B %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{% if post.title and post.title != "" %}{{post.title}}{% else %}{{post.excerpt |strip_html}}{%endif%}</a>
{% endfor %}