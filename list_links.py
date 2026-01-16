
from bs4 import BeautifulSoup

filename = 'index.html'

try:
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
        for a in soup.find_all('a'):
            href = a.get('href')
            text = a.get_text(strip=True)
            print(f"Link: {text[:30]}... -> {href}")
except Exception as e:
    print(f"Error: {e}")
