import os
js_path = '/Users/angelogarcia/Documents/PROJETOS ANTIGRAVITY/bloopi/assets/index-hMw7xmWY.js'
with open(js_path, 'r') as f:
    content = f.read()

idx = content.find('apple-pay')
if idx != -1:
    print(content[max(0, idx-100):min(len(content), idx+100)])
else:
    print("Not found")
