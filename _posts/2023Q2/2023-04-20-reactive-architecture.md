---
title: Reactive Architecture
categories: [Software Engineering]
tags: [Software Architecture]
excerpt: "Building Responsive, Resilient, and Scalable Systems."
---

{% include def-reactive-architecture.md %}

The [Reactive Manifesto](https://www.reactivemanifesto.org) was published in 2014 as a guiding document outlining the principles and characteristics of reactive systems, providing a framework for building responsive, resilient, elastic, and message-driven software applications.

Large, distributed systems that require designs addressing these challenges are no longer exclusive to big tech. Many data-driven businesses now face these practical challenges, as modern companies are essentially technology-driven.

Understanding and applying the principles of Reactive Architecture is an essential skill. Let's review the main principles of this paradigm:

1. **Responsiveness**: The system should consistently respond to requests promptly. Responsiveness lies at the heart of usability and utility;
2. **Resilience**: The system is designed to be fault-tolerant. It should recover gracefully from failures and continue to function, which involves implementing strategies to isolate failures and establish self-healing mechanisms;
3. **Elasticity**: A reactive system should scale up and down based on workload, ensuring efficient resource utilization. This entails dynamically allocating and deallocating resources across multiple instances;
4. **Message-driven**: A reactive system relies on asynchronous message passing to establish boundaries between components, enabling loose coupling, isolation, and location transparency.

The following diagram illustrates the relationships between these principles, with message-driven serving as the paradigm's foundation and responsiveness as the high-level outcome.

![Reactive Architecture](/images/posts/2023-04-20-reactive-architecture/reactive-architecture.png "Reactive Architecture")

Large systems usually comprise smaller ones, commonly adopting a microservices strategy. The principles of Reactive Architecture apply to all scale levels, making them composable.

When I joined [VTEX](/about/vtex), I faced such challenges for the first time in my career. Our digital commerce platform serves the needs of thousands of users worldwide and experiences increased load during major e-commerce events. The world's largest systems serve billions of people daily.

If you haven't yet consciously applied these design principles, it's worth considering. The [Reactive Manifesto](https://www.reactivemanifesto.org) is an excellent starting point, as it links to many helpful online resources.