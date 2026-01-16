
import os

filename = 'index.html'
search_terms = ['Fernanda', '1d18ea9d', 'fbevents.js', 'latest.js', '</head>']

if not os.path.exists(filename):
    print(f"File {filename} not found.")
else:
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            line_num = i + 1
            for term in search_terms:
                if term in line:
                    print(f"MATCH [{term}] LINE {line_num}:")
                    print(line.strip())
                    print("-" * 20)
