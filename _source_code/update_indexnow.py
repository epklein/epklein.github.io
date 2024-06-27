import requests
import json
import sys
import xml.etree.ElementTree as ET

def fetch_sitemap(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.content

def parse_sitemap(xml_content):
    urls = []
    root = ET.fromstring(xml_content)
    for url in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
        loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text
        urls.append(loc)
    return urls

def generate_body(urls, host, key):
    key_location = f"https://{host}/{key}.txt"
    content = {
        "host": host,
        "key": key,
        "keyLocation": key_location,
        "urlList": urls
    }
    json_data = json.dumps(content, indent=4)
    
    return json_data

def submit_to_indexnow(data):
    url = 'https://api.indexnow.org/indexnow'
    headers = {
        "Content-Type": "application/json; charset=utf-8"
    }
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()

    return response.status_code

def main():
    host = sys.argv[1] if len(sys.argv) > 1 else 'eduklein.com.br'
    indexnow_key = sys.argv[2] if len(sys.argv) > 2 else '6fbf82e925ef458ca0ef4641519b794c'
    sitemap_url = f"https://{host}/sitemap.xml"
    
    try:
        sitemap_content = fetch_sitemap(sitemap_url)
        urls = parse_sitemap(sitemap_content)
        json_data = generate_body(urls, host, indexnow_key)
        status_code = submit_to_indexnow(json_data)
        print(f"Response from IndexNow API was {status_code}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()