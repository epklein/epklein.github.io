---
title: DEFCON Process
categories: [Software Engineering]
tags: [Deployment, VTEX Way]
---

At VTEX, teams have autonomy in the execution of their deployments into production. Teams also have different deployment cadences. Some may deploy many times a day, while others may deploy less frequently. **In order to provide stability to the whole VTEX platform, there are some processes and tools implemented to support the engineering team. One of those being the DEFCON process.**

The **DEFCON process** comprises a set of rules and measures that impacts deployment routines at VTEX. Those are widely communicated across the whole engineering team.

DEFCON is short for *defense readiness condition*. The process name is based on the US military [DEFCON alert state](https://en.wikipedia.org/wiki/DEFCON).

The DEFCON stages range from 1 to 5, where DEFCON 5 is the least severe. VTEX goes automatically to DEFCON 1 during a platform outage.

## DEFCON 5

It is just a typical day, and teams must announce their changes. In case of an increased number of errors, teams must roll back changes.

## DEFCON 3 and 4

When triggered, teams are in a more vigilant state. More control is needed, so engineers usually cannot deploy solo or in parallel in those stages.

## DEFCON 2

Strategic conditions trigger DEFCON 2, where, basically, teams are not allowed to deploy unless they get authorization from leadership.

## DEFCON 1

It is a crisis condition, where only maneuvers to end it may be executed during this stage.

<br />

Those are just brief descriptions of the stages, of course. Each has specific conditions to trigger their beginning and end, and specific measures teams must follow during it.

But I think the most important aspect of such a process is to have a clear communication process to give teams clarity over the situation. This way, empowered and autonomous teams can effectively help to solve the crisis and to stabilize the platform.