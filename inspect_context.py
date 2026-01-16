
filename = 'index.html'
search_str = 'r$5,99'

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()
    idx = content.find(search_str)
    if idx != -1:
        start = max(0, idx - 100)
        end = min(len(content), idx + 200)
        chunk = content[start:end]
        print(f"Match found at index {idx}")
        print("--- CONTEXT START ---")
        print(chunk.replace('\n', '\\n'))
        print("--- CONTEXT END ---")
    else:
        print("String not found in file content.")
