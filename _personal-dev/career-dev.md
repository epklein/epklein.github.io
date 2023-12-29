---
title: Career Development
permalink: /personal-dev/career-dev
toc: true
toc_sticky: true
---

I firmly believe that we all should take ownership of our work and career. Ask yourself, what are your career aspirations? How can your manager and current company support these goals? You should not solely rely on your company or manager to shape your career trajectory. Take charge and own your career path.

## Job Hunting

Transitioning to a new position, or even a new company, may be the next step in your career development. In that case, you will do some job hunting, which is not just about interviewing well or doing great technical tests.

You can improve your chances of getting your next role by carefully searching for positions and companies, adapting your resume accordingly, and using your network to reach out to people from your desired next company.

[Don't Miss Your Next Role!](https://www.scarletink.com/using-your-brain-while-job-hunting/) is a great blog post by [Dave Anderson](https://www.linkedin.com/in/scarletink/), an ex-Amazon Tech Director, that I highly recommend. You may also take advantage of [reverse interviewing](https://github.com/viraptor/reverse-interview/tree/master) to understand the company, position, leadership, etc., to learn if a particular position fits your career goals.

## Related Posts

{% for post in site.tags['Career Development'] %}- <b>{{ post.date | date: "%b %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></b>. {{post.excerpt |strip_html}}
{% endfor %}

### Software Engineering Career

{% for post in site.tags['SWE Career'] %}- <b>{{ post.date | date: "%b %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></b>. {{post.excerpt |strip_html}}
{% endfor %}