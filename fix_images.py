import os
import re
import shutil

base_dir = '/Users/angelogarcia/Documents/PROJETOS ANTIGRAVITY/bloopi'
assets_dir = os.path.join(base_dir, 'assets')
landing_logos_dir = os.path.join(base_dir, 'landing', 'payment-logos')

os.makedirs(landing_logos_dir, exist_ok=True)

for filename in os.listdir(assets_dir):
    # Match imgi_NUMBER_realname
    match = re.match(r'imgi_\d+_(.+)', filename)
    if match:
        real_name = match.group(1)
        src = os.path.join(assets_dir, filename)
        dst = os.path.join(assets_dir, real_name)
        
        # Rename in assets folder (overwrite if exists)
        shutil.copy2(src, dst)
        print(f"Copied {filename} -> {real_name}")

# Now copy all image files from assets to landing/payment-logos
for filename in os.listdir(assets_dir):
    if filename.endswith(('.png', '.webp', '.jpg', '.jpeg', '.svg', '.gif')):
        src = os.path.join(assets_dir, filename)
        dst = os.path.join(landing_logos_dir, filename)
        shutil.copy2(src, dst)
        
print("All files organized!")
