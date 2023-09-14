---
title: Progressive Deployment
categories: [SWE Management, Software Engineering]
tags: [Delivery]
excerpt: "Strategies to execute progressive deployments"
---

Rolling out a product or improvement involves deploying and launching new features or updates to an existing user base. This is an integral part of operating any digital platform.

A well-designed rollout plan is essential for successfully launching these improvements without negatively affecting the operations of customers. A comprehensive rollout plan should address, at a minimum, the following key aspects:

- **Testing protocols**: Before rolling out to the entire user base, testing the new features or updates in a controlled environment (like staging) or with a smaller subset of users (beta testers) can help identify and fix issues.
- **A progressive deployment plan and rollback process**: A progressive deployment plan ensures that updates are introduced in phases, allowing for real-time feedback and adjustments, while a rollback process guarantees a swift return to the previous version if any issues arise, minimizing disruptions and potential risks.
- **A communication plan that addresses key stakeholders**: A well-structured communication plan is vital, ensuring that customers are informed and prepared for any changes, while also equipping customer support and technical support teams with the necessary information to address queries and resolve issues.
- **User documentation**: Providing comprehensive and updated user documentation helps users adapt to new features or changes.

## Progressive Deployment Strategies

From the above aspects, I want to delve into the progressive deployment plan.

A progressive deploy aims to minimize risk and improve customer's and developer's experience, by implementing change to a small group of users, which allow fast feedback and faster rollback in case of failures. There are a few strategies that we can adopt for a progressive deploy:

1. **Canary Deployments**: A new software version is partially rolled out to a small subset of users before a full rollout. The purpose is to test and monitor the new version in a real environment with actual users. If the canary deployment works well and no issues are identified, the new version can be rolled out to the entire user base. If issues are found, it's easier to roll back, preventing all users from being affected.
2. **Blue/Green Deployments**: Two identical production environments are maintained. The "blue" environment runs the current version of the software, while the "green" environment gets the new version. Once the new version is ready and tested in the "green" environment, traffic is switched over, making "green" the live environment. This allows for near-instant rollbacks in case of issues and ensures minimal downtime during deployments.
3. **Rolling Deployments**: The new software version is gradually rolled out to all users, replacing the old version incrementally. This is typically done server by server or container by container, ensuring that only a portion of the system is updated at any given time. If problems arise during the deployment, it affects only the portion being updated, allowing for easier rollbacks and reduced impact.
4. **Shadow Deployments**: The new version of the software runs alongside the old version, but without actual user traffic directed to it. Instead, real user requests are duplicated to the new version in real-time, allowing teams to monitor and test how the system behaves under realistic conditions without affecting the actual user experience.

## Feature Flags

Feature flags, also known as feature toggles, provides flexibility in the deployment process. They allow for specific features to be turned on or off at runtime without changing the code.

Instead of deploying a new version of the software to a subset of servers or containers, the feature is deployed everywhere but is enabled first for a small subset of users (eg. beta testers) and then progressively rolled to the entire user base in phases.

This ability supports various progressive deployment strategies.