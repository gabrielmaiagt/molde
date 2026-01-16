
filename = 'index.html'
search_terms = ['Fernanda Sanchez', '1d18ea9d', 'latest.js', 'fbevents.js']

with open(filename, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        for term in search_terms:
            if term in line:
                print(f"[{term}] found at line {i+1}:")
                # print snippet
                print(line.strip()[:200])
