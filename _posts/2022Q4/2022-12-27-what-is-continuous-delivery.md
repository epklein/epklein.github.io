---
title: What is Continuous Delivery?
categories: [DevOps]
tags: [Delivery, Continuous Delivery]
excerpt: Continuous Delivery is a DevOps technical practice that let us make changes into production, quickly and reliably. Let's recap its principles and foundations.
---

[Continuous Delivery](/swe/devops/cd) (CD) is one of the fundamental software engineering practices that modern companies use to deliver software *quickly* and *reliably*.

By "deliver software", I mean not just new features, but any sort of change, such as bug fixes, configuration changes, and experiments.

To deliver high-quality software quickly and reliably, let's recapitulate CD's main principles and foundations (according to *[Accelerate: The Science of Lean Software and DevOps](/books/accelerate)*).

## Principles

There are five key principles at the heart of CD:

1. **Build quality in**: We invest in people and tools, to detect issues quickly and fix them in earlier stages, where they are cheap to resolve;
2. **Work in small batches**: The goal is to work in small chunks to deliver business outcomes quickly for a small part of our target audience as a means of collecting frequent feedback;
3. **Computers perform repetitive tasks; people solve problems**: By automating repetitive work that takes a long time, we reduce the cost of rolling out changes and we free up people for higher value work;
4. **Relentlessly pursue continuous improvement**: High-performing teams are never satisfied. They make improvement a daily routine;
5. **Everyone is responsible**: System-level outcomes (throughput, quality, stability, etc.) are well aligned with business outcomes. Everyone works towards measurable, achievable, time-bound goals to reach them.

## Foundations

To implement CD, we must create the following foundations:

- **Comprehensive configuration management**: It should be possible to build, test, and deploy our software and provision our environments, in a fully automated way, from data stored completely in version control;
- **Continuous Integration (CI)**: Each change in the codebase should trigger a build process that includes running unit tests;
- **Continuous testing**: We should be testing all the time as an integral part of the development process. Developers should be able to run all automated tests on their workstations. Automated tests should be run against every change in the codebase to give developers fast feedback.

The bottom line is that, to implement CD, we create many feedback loops to ensure we are building high-quality software that gets delivered frequently and reliably.