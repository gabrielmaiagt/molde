
filename = 'index.html'
terms = ['PLANO BÁSICO', 'upgrade-vestidos-2', 'R$5,99']

try:
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            for term in terms:
                if term in line: # simplistic check
                    print(f"{term}::{i+1}")
except Exception as e:
    print(f"Error: {e}")
