---
title: Deployment
permalink: /swe/sdlc/deployment
---

Consists in releasing software to a target environment, making it accessible to end users.

Rolling out a product or deploying an update may vary a lot in complexity. Digital platforms typically require [progressive deployment strategies](/progressive-deployment), which may be useful in many contexts.

Modern software development practices and tools also aim to simplify and streamline deployment processes. For more details, refer to [DevOps](/swe/devops), especially the [Continuous Delivery (CD)](/swe/devops/cd) capability.

## Related Posts

{% for post in site.tags['Deployment'] %}- <b>{{ post.date | date: "%b %e, %Y" }} - <a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></b>. {{post.excerpt |strip_html}}
{% endfor %}