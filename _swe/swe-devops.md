---
title: DevOps
permalink: /swe/devops
toc: true
toc_sticky: true
---

DevOps is a combination of culture, practices, and tools that integrates and automates software development and operational processes so that companies can plan, develop, deliver, and operate faster and reliably.

It is not by definition, but usually DevOps involves the adoption of [cloud computing](/swe/cloud-computing). By the way, some cloud computing providers offer a good definition of what is DevOps, its practices and benefits. And of course their toolkit to implement DevOps. If you want to delve deeper into it, you may refer to [AWS](https://aws.amazon.com/devops/what-is-devops/), [Azure](https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-devops/), and [Google Cloud](https://cloud.google.com/devops/) definitions.

## Key Performance Metrics

Research from [DORA](https://www.devops-research.com) (DevOps Research & Assessment) have validated four metrics that measure software delivery performance. According to the research, companies that exhibit exceptional organizational performance excel in these metrics:

- **Deployment Frequency**: How often does your team and your organization release code to end users?
- **Lead Time for Changes**: How long does it take to go from code committed to code successfully running into production?
- **Time to Restore Service**: How long does it take to restore service when an incident or a defect that impact users occurs?
- **Change Failure Rate**: What percentage of releases to production result in degraded service, and subsequently require remediation?

You can explore the results in the [*State of DevOps Reports*](https://www.devops-research.com/research.html). In [this blog](/software-delivery-performance-metrics) post I also share some data on how teams are performing according to the research.

## DevOps capabilities

- Communication and collaboration
- Configuration management
- Infrastructure as code
- Version control
- Trunk-based development
- Continuous integration (CI)
- [Automated testing](#automated-testing)
- Deployment automation
- Monitoring and logging
- [Continuous delivery](/swe/devops/cd) (CD)

### Automated testing

Improve quality without loosing speed by building reliable automated test suites.

Two great articles I read from Azure DevOps, about testing approaches in developing and delivering services: [shift testing left with unit tests](https://docs.microsoft.com/en-us/devops/develop/shift-left-make-testing-fast-reliable) and [shift right to test in production](https://docs.microsoft.com/en-us/devops/deliver/shift-right-test-production)

## Related Posts

{% for post in site.categories['DevOps'] %}- {{ post.date | date: "%B %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{% if post.title and post.title != "" %}{{post.title}}{% else %}{{post.excerpt |strip_html}}{%endif%}</a>
{% endfor %}

## Recommended Reading

### Books

- {% include books/accelerate.md %}

### Articles

- [Azure DevOps](https://docs.microsoft.com/en-us/azure/devops). A broad documentation of how Azure sees DevOps. 