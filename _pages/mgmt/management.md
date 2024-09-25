---
title: Management
permalink: /mgmt
toc: true
toc_sticky: true
---

This page is a collection of resources about **management**. I won't cover everything about such a broad discipline; I would certainly fail to attempt to do so. Instead, I focus on relevant topics from my experience as a [software engineering manager](/mgmt/sem/sem-role).

**Consider this my management playbook:** my current, best understanding of how to manage **people**, **processes**, and **software development** within tech companies.

## Components

I've grouped management activities into the following components:

<!-- Systems health / Technical Vision -->
- [SWE Management](/mgmt/sem): The management practices focused on the development and maintenance of software.
<!-- People Development / Stakeholder Management -->
- [People Management](/mgmt/people): The goal of managing people is to achieve results through others. To do this, we must develop people, delegate tasks, communicate effectively, etc.
<!-- Team growth / Team Productivity / Business Impact -->
- [Team Management](/mgmt/team): To manage teams and deliver results, we need to hire, develop, and grow people; implement processes and measure performance; define strategies and give vision and purpose, etc.
- [Self-Management](/personal-dev/self-mgmt): Before managing others, we must learn to manage ourselves. This includes planning goals, priorities, schedules, routines, and [personal development](/personal-dev).

## What Managers Do

In his foundational book "[Management](https://www.goodreads.com/book/show/4900407-management-revised-edition)," [Peter Drucker](https://en.wikipedia.org/wiki/Peter_Drucker), who is considered the father of modern management by many, delineates the five fundamental operations that every manager must execute. These operations offer a valuable framework for understanding management. I will briefly explain these and exemplify them through my component arrangement. 

### 1. Set Objectives

Managers define clear objectives, determine the goals and actions required, and ensure communication to align efforts to achieve them.

- **SWE Management**: Establishing project goals, milestones, and deliverables.
- **People Management**: Setting career development goals and performance targets for individuals.
- **Team Management**: Defining team objectives to align efforts and foster collaboration.
- **Self-Management**: Personal goal setting to ensure continuous improvement.

### 2. Organize

Managers organize work by analyzing necessary activities, decisions, and relationships, then classifying and dividing the work into manageable tasks. This includes planning, delegating, and coordinating tasks.

- **SWE Management**: Structuring the development process, assigning tasks, and managing workflows.
- **People Management**: Planning workforce allocation and structuring teams.
- **Team Management**: Organizing team roles, responsibilities, and resources to enhance team effectiveness.
- **Self-Management**: Personal time and task management to stay on top of priorities.

### 3. Motivate and Communicate

Managers motivate and communicate by building cohesive teams and fostering solid relationships. They also ensure constant communication by integrating all parts of the organization.

- **SWE Management**: Encouraging developer engagement and ensuring clear, consistent communication within the development team.
- **People Management**: Motivating individuals through recognition, feedback, pay, promotion, and career growth opportunities.
- **Team Management**: Building team spirit, promoting collaboration, and resolving conflicts.

### 4. Measure

Managers establish crucial performance targets and standards for the organization and its individuals. They ensure everyone has access to relevant metrics, analyze and interpret performance, and communicate findings effectively.

- **SWE Management**: Tracking project progress, assessing performance metrics, and ensuring quality standards.
- **People Management**: Evaluating employee performance and providing constructive feedback.
- **Team Management**: Assessing team productivity, measuring success against goals, and identifying areas for improvement.

### 5. Develop People

Managers develop people, including themselves, which is increasingly vital in today's knowledge-driven era.

- **SWE Management**: Offering training and development opportunities to enhance technical skills.
- **People Management**: Focusing on individual career growth through targeted development plans.
- **Self-Management**: Pursuing self-improvement and continuous learning to stay relevant and effective.

## Related Posts

{% for post in site.categories['Management'] %}- <b>{{ post.date | date: "%b %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></b>. {{post.excerpt |strip_html}}
{% endfor %}

## Learning

{% include learning/management.md %}