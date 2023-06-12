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