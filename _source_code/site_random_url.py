# written with the help of ChatGPT

import sys
import requests
from xml.etree import ElementTree as ET
import random

def get_random_url_from_sitemap(sitemap_url):

    response = requests.get(sitemap_url)
    tree = ET.fromstring(response.content)

    ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    urls = [elem.text for elem in tree.findall('.//ns:loc', ns)]

    return random.choice(urls)

sitemap_url = sys.argv[1] if len(sys.argv) > 1 else "https://eduklein.com.br/sitemap.xml"

print(get_random_url_from_sitemap(sitemap_url))