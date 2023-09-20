---
title: Software Engineering
permalink: /swe
toc: true
toc_sticky: true
---

Software engineering is a branch of computer science that deals with the design, development, implementation, and maintenance of software systems.

It is a systematic, disciplined approach to applying engineering principles to the development, operation, and maintenance of software, with a focus on providing cost-effective software solutions that are reliable and work efficiently

## Software Development Lifecycle (SDLC)

The Software Development Lifecycle (SDLC) is a systematic process that guides teams and organizations in delivering high-quality software.

There are several methodologies and models that fall under the SDLC umbrella, each with its distinct tasks and activities. Broadly, these can be classified as traditional models like the Waterfall and its variations, and contemporary agile, adaptive, or iterative models, with Scrum being the most popular among them.

The choice of a particular SDLC model depends on many factors, but the main goal of them is to organize the following phases of software development:

- **Planning**: Consists in identifying the need for a new product or feature, defining its scope and constraints, and creating a roadmap.
- **[Design](/swe/sdlc/design)**: Consists in conceiving the system's architecture, user interfaces, and user experiences to fulfill the defined requirements.
- **Development**: Consists in writing, integrating and revising code to transform the design into a functional software application.
- **Testing**: Consists in evaluating the software against specified requirements to identify and fix defects and ensure quality.
- **[Deployment](/swe/sdlc/deployment)**: Consists in releasing the software to a target environment, making it accessible to end users.

## Practices and Approaches

Some key practices and approaches to software engineering include:

- [DevOps](/swe/devops): It is a combination of culture, practices, and tools that integrates and automates software development and operational processes so that companies can plan, develop, deliver, and operate faster and reliably.

## Software Architecture

- **Reactive Architecture**: {% include def-reactive-architecture.md %}

**On the blog**

{% for post in site.tags['Software Architecture'] %}- {{ post.date | date: "%B %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{% if post.title and post.title != "" %}{{post.title}}{% else %}{{post.excerpt |strip_html}}{%endif%}</a>
{% endfor %}


## Learning

{% include learning/swe.md %}