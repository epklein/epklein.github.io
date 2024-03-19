# written with the help of Gemini

import sys
import requests
from lxml import etree
import random

sitemap_url = "https://eduklein.com.br/sitemap.xml" if len(sys.argv) == 1 else sys.argv[1] 

response = requests.get(sitemap_url)
tree = etree.fromstring(response.content)

urls = tree.xpath("//*[local-name()='loc']/text()")
random_url = random.choice(urls)

print(random_url)