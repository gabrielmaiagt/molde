
filename = 'index.html'
search_str = 'r$5,99'

with open(filename, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if search_str in line:
            print(f"Line {i+1} found:")
            # Print a chunk around the match
            start = line.find(search_str) - 100
            end = line.find(search_str) + 300
            if start < 0: start = 0
            print(line[start:end])
