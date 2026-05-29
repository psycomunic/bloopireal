import re
js_path = '/Users/angelogarcia/Documents/PROJETOS ANTIGRAVITY/bloopi/assets/index-hMw7xmWY.js'
with open(js_path, 'r') as f:
    content = f.read()

print("Videos:")
print(re.findall(r'[^"\'\\]+\.(?:mp4|webm)', content))
print("Lottie/JSON:")
print(re.findall(r'[^"\'\\]+\.json', content))
