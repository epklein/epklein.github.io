---
title: Software Engineering Career Ladders
permalink: /mgmt/sem/swe-career
toc: true
toc_sticky: true
---

In the tech industry, we use progression frameworks (or '*career ladders*') to guide the development of engineers' careers.

A **career ladder** usually consists of **Designations** (Software Engineer, Product Manager, etc.), **Levels**, and **Expectations**, to measure, develop, and evaluate performance.

A typical Software Engineering (SWE) career ladder:

- SWE, SWE II and Sr. SWE: The first three, and most common, levels in Software Engineering;
- Staff: They lead deep, complex, or high-risk technical projects;
- Principal: They guide the technical direction of the company;
- Distinguished and Fellow: Such levels may exist in large organizations. Like Principals, they guide the technical vision of the organization. Usually, there is no standardized way to achieve this.

For each level in the ladder, companies define a set of expectations. Engineers may take them as a reference for [personal development](/personal-dev), and those expectations are usually evaluated in [performance review cycles](/performance-review-cycle).

## Progression Frameworks

Some interesting resources covering career ladders in the tech industry:

- [progression.fyi](https://progression.fyi/): *progression.fyi is currently a collection of open source and public ‘progression frameworks’, examples of the tools that thousands of managers in tech are building for their teams to ensure that they feel valued at work*.
- [Engineering Career Paths at Big Tech and High-Growth Startups](https://newsletter.pragmaticengineer.com/p/engineering-career-paths): An Issue of the Pragmatic Engineer Newsletter, by {% include people/gergely-orosz.md %}, covering the most common levels and career paths for engineers at big tech.
- [Designations, levels and calibration](https://lethain.com/perf-management-system): An interesting article about career ladders and performance management by {% include people/will-larson.md %}.

## Climbing the Ladder

There are tons of references online on how to develop yourself as a software engineer. Here I share a few posts and articles that I think are valuable to help engineers progress in their careers.

- [StaffEng](https://staffeng.com/): A collection of [stories](https://staffeng.com/stories) from folks who reached a Staff-plus engineering role, and [guides](https://staffeng.com/guides/) for reaching and succeeding at such roles
- [What makes an effective software engineer?](https://leaddev.com/personal-development/what-makes-effective-software-engineer) by [Addy Osmani](https://addyosmani.com), published at [LeadDev](https://leaddev.com)
- [The product-minded Software Engineer](https://blog.pragmaticengineer.com/the-product-minded-engineer), by {% include people/gergely-orosz.md %}
- [Becoming a go-to person gets you promoted. Here's how to do it as a software engineer.](https://careercutler.substack.com/p/becoming-a-go-to-person-gets-you) by [Jordan Cutler](https://careercutler.substack.com/)

## Related Posts

{% for post in site.tags['SWE Career'] %}- <b>{{ post.date | date: "%b %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></b>. {{post.excerpt |strip_html}}
{% endfor %}