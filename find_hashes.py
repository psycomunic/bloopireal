import re
import os

js_path = '/Users/angelogarcia/Documents/PROJETOS ANTIGRAVITY/bloopi/assets/index-hMw7xmWY.js'
with open(js_path, 'r') as f:
    content = f.read()

# Find all asset paths in the JS file
matches = re.findall(r'/assets/([^"\'\\]+\.(?:png|jpg|jpeg|webp|svg))', content)

# Unique matches
unique_matches = sorted(list(set(matches)))

for m in unique_matches:
    print(m)
