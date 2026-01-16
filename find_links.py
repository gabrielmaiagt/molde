
import re

filename = 'index.html'

try:
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        links = re.findall(r'href=["\'](http[^"\']+)["\']', content)
        for link in links:
            print(link)
except Exception as e:
    print(f"Error: {e}")
