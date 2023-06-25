---
title: Random Website Links using Chat GPT-4
categories: [Coding]
tags: [Chat GPT, LLM, Python]
excerpt: How I built a simple Python script using Chat GPT-4 to get random pages of my website.
---

I write this website and blog as a personal project to practice writing in English. So far, I have written more than 20 blog posts and more than 60 pages in total.

I feel confident I'm improving over time, making me think I'm leaving many poor texts behind, which I'm not proud of. But reviewing everything is arduous and time-consuming.

So **I had this idea of randomly selecting a page from my website to review** to see if it was good enough and to determine whether I should fix it, improve it, or even write an updated version.

## Writing a Python Script with Chat GPT

I wanted something straightforward, so my first approach would be to write a Python script myself. That would be an easy and quick task. Some experienced developers would take a few minutes, while others would take one hour or two; Few would take more than that. Not sure how long I'd take to write it, anyway.

**Nowadays, we hear a lot about Large Language Models (LLMs) and Chat GPT from OpenAI. So I thought it would be an excellent opportunity to write this script faster using Chat GPT.**

In the end, it was really straightforward. I got a functional piece of code right from my first prompt!

In case this experience, and even this code, could be interesting for you, I share the process below.

## My Prompt

> I would like a Python Script that, given a sitemap.xml url, it gives back a random url from that sitemap. I want the script to receive a sitemap url from the command line, and this argument also defaults to https://eduklein.com.br/sitemap.xml when not informed.

It may not be the best prompt for the task, but it gave me the proper code anyway. By the way, Prompt Engineering has been considered a future profession since the advent of LLMs.

### Chat GPT's output

*Sure, here's how you can modify the script to take a command-line argument, which defaults to https://eduklein.com.br/sitemap.xml if no argument is provided:*

~~~ python
import sys
import requests
from xml.etree import ElementTree as ET
import random

def get_random_url_from_sitemap(sitemap_url):
    # Make a GET request to the sitemap URL
    response = requests.get(sitemap_url)

    # Parse the XML content of the sitemap
    tree = ET.fromstring(response.content)

    # The namespace dictionary
    ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

    # Get all the <loc> elements in the XML document
    urls = [elem.text for elem in tree.findall('.//ns:loc', ns)]

    # Return a random URL
    return random.choice(urls)

# Get the sitemap URL from the command line arguments
sitemap_url = sys.argv[1] if len(sys.argv) > 1 else "https://eduklein.com.br/sitemap.xml"

print(get_random_url_from_sitemap(sitemap_url))
~~~

You can now run the script from the command line as follows:

~~~ bash
python random_url_from_sitemap.py
~~~

This will default to using https://eduklein.com.br/sitemap.xml as the sitemap URL. If you want to provide a different sitemap URL, you can do so as a command-line argument:

~~~ bash
python random_url_from_sitemap.py "https://www.example.com/sitemap.xml"
~~~

Just replace "https://www.example.com/sitemap.xml" with your actual sitemap URL.

## Executing the Script

I tested the script, which gave me the desired results.

~~~ bash
python3 site_random_url.py
https://eduklein.com.br/finance/value-investing
~~~

~~~ bash
python3 site_random_url.py https://eduklein.com.br/sitemap.xml
https://eduklein.com.br/book/how-the-world-really-works
~~~

---

**Well done Chat GPT!**