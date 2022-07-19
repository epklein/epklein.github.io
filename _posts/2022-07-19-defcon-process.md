---
layout: post
title: DEFCON process
categories: [VTEX Way, Delivery]
---

At VTEX, teams have autonomy in the execution of their deployments into production. Teams also have different deployment cadences. Some may deploy many times a day, while others may deploy less frequently. **In order to provide stability to the whole VTEX platform, there are some processes and tools implemented to support the teams. One of those being the DEFCON process.**

The **DEFCON process** comprises a set of rules and measures that impacts deployment routines at VTEX. Those are widely communicated across the whole engineering team.

DEFCON is short for *defense rediness condition*. The process name is based in the US military [DEFCON alert state](https://en.wikipedia.org/wiki/DEFCON).

The DEFCON stages range from 1 to 5, where DEFCON 5 is the least severe. VTEX goes automatically to DEFCON 1 during a platform outage.

## DEFCON 5

A normal day, teams usually have to announce their changes and rollback in case of increased number of errors.

## DEFCON 3 and 4

When triggered, teams are in a more vigilant state. More control is needed, so usually in those stages engineers can't deploy solo or in parallel.

## DEFCON 2

Strategic conditions trigger DEFCON 2, where basically teams are not allowed to deploy unless they get authorization from leadership.

## DEFCON 1

It is a crisis condition, where only maneuvers to end it may be executed during this stage.

<br />

Those are just a brief description of the stages, of course. Each have specific conditions to trigger and to end, and also specific measures teams have to follow during it.

But I think the most important aspect of such a process is to have a clear communication processes to give teams clarity over the situation. This way empowered and autonomous teams can effectivelly help to solve the crisis to stabilize the platform.