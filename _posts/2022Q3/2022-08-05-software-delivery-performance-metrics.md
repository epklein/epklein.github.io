---
title: Software Delivery Performance Metrics
categories: [DevOps]
tags: [Delivery]
---

Research from [DORA](https://www.devops-research.com) (DevOps Research & Assessment) have validated four metrics that measure software delivery performance. According to the research, companies that exhibit exceptional organizational performance excel in these metris:

- **Deployment Frequency**: How often does your team and your organization release code to end users?
- **Lead Time for Changes**: How long does it take to go from code committed to code successfully running into production?
- **Time to Restore Service**: How long does it take to restore service when an incident or a defect that impact users occurs?
- **Change Failure Rate**: What percentage of releases to production result in degraded service, and subsequently require remediation?

You can explore the results in the [*State of DevOps Reports*](https://www.devops-research.com/research.html). To give you a bit of data, the following table summarizes how teams are doing in those four metris (from the 2021 report).

| Metric | Elite | High | Medium | Low |
| ---| --- | --- | --- |
| **Deployment frequency** | On-demand (multiple deploys per day) | Between once per week and once per month | Between once per month and once every 6 months | Fewer than once per six months |
| **Lead time for changes** | Less than one hour | Between one day and one week | Between one month and six months | More than six months |
| **Time to restore service** | Less than one hour | Less than one day | Between one day and one week | More than six months |
| **Change failure rate** | 0%-15% | 16%-30% | 16%-30% | 16%-30% |

Notice that *deployment frequency* and *lead time for changes* plays for **Throughput**, while *time to restore service* and *change failure rate* accounts for **Stability**. The research also reports a fifh metric, **Reliability**, as of operational performance.