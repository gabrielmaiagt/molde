
filename = 'index.html'
terms = ['grupo-educa-abc', 'mycartpanda']

try:
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            for term in terms:
                if term in line:
                    print(f"{term}::{i+1}:{line.strip()[:200]}")
except Exception as e:
    print(f"Error: {e}")
