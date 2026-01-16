
filename = 'index.html'
term = 'upgrade-vestidos-2'

try:
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if term in line:
                print(f"{term}::{i+1}")
                print(line.strip())
except Exception as e:
    print(f"Error: {e}")
