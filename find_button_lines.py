
filename = 'index.html'
term = 'elementor-button'

try:
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if term in line:
                print(f"{i+1}:{line.strip()}")
except Exception as e:
    print(f"Error: {e}")
