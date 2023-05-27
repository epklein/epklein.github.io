---
title: Team Management
permalink: /mgmt/team
toc: true
toc_sticky: true
---

Team management refers to the coordination of a group of individuals in order to achieve common goals. This process involves various functions, such as communication, delegation, motivation, and conflict resolution to ensure that team members work together effectively and efficiently.

## Practices

A set of practices I believe are helpful for manager to support their teams.

### Keep Track of Achievements

There is much debate about the best way to measure a team's performance. Should we assess individual outputs or focus solely on team-level outcomes? Should we rely on specific metrics (which individuals may learn to manipulate) or should we avoid them? If we do use them, how many should we use?

This is an ongoing discussion with valid points on all sides. People's views will undoubtedly continue to diverge, and that's okay. I, too, have my own beliefs about what needs to be measured — a topic I plan to address in a future blog post.

Regardless of these debates, I firmly believe that nothing beats delivered results. Therefore, I advise managers to keep track of their teams' achievements. Maintaining a public record of these accomplishments can serve as a useful resource in a variety of contexts.

### Write Guides

Writing guides for my teams has proven to be a useful and scalable strategy to tackle specific challenges. This procedure scales as it prevents team members from having to reinvent solutions for known problems, and it ensures that we have a consistent approach to addressing these issues. I've written about this practice in a blog post titled [Writing Guides to Support Your Teams](/writing-guides).

It's important to note that writing guides may not be the best approach for every situation. If you're dealing with a non-specific problem that requires your team to brainstorm and explore creative solutions, a prescriptive guide may limit their approach. Remember, being overly specific for an open-ended problem can potentially stifle your team's ability to innovate.

## Related Posts

{% for post in site.categories['Team Management'] %}- {{ post.date | date: "%B %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{% if post.title and post.title != "" %}{{post.title}}{% else %}{{post.excerpt |strip_html}}{%endif%}</a>
{% endfor %}