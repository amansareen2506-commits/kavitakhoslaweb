import os
import shutil
from PIL import Image

src_dir = r'C:\Users\HP\OneDrive\Desktop\KKJ images\Lab Grown Diamonds'
local_sites_dir = r'C:\Users\HP\Local Sites'

def get_dhash(im, hash_size=8):
    try:
        if im.mode == 'P': im = im.convert('RGBA')
        im_gray = im.convert('L').resize((hash_size+1, hash_size), Image.Resampling.LANCZOS)
        pixels = list(im_gray.getdata())
        difference = []
        for row in range(hash_size):
            for col in range(hash_size):
                difference.append(pixels[row*(hash_size+1)+col] > pixels[row*(hash_size+1)+col+1])
        decimal_value = 0
        hex_string = []
        for index, value in enumerate(difference):
            if value: decimal_value += 2**(index % 8)
            if (index % 8) == 7:
                hex_string.append(hex(decimal_value)[2:].zfill(2))
                decimal_value = 0
        return ''.join(hex_string)
    except Exception as e:
        return None

def hamming_distance(h1, h2):
    b1 = bin(int(h1, 16))[2:].zfill(64)
    b2 = bin(int(h2, 16))[2:].zfill(64)
    return sum(c1 != c2 for c1, c2 in zip(b1, b2))

print("Scanning Lab Grown Diamonds directory...")
target_images = []
for f in os.listdir(src_dir):
    p = os.path.join(src_dir, f)
    if os.path.isfile(p) and f.lower().endswith(('.png', '.jpg', '.jpeg')):
        try:
            with Image.open(p) as img:
                h = get_dhash(img)
                if h:
                    target_images.append({'filename': f, 'path': p, 'hash': h, 'best_match': None, 'best_dist': 64})
        except Exception as e:
            print(f"Error opening target {f}: {e}")

print(f"Loaded {len(target_images)} target images to match.")

# Recursively scan WordPress public sites
print("Scanning local WordPress site directories...")
scanned_count = 0
for root, dirs, files in os.walk(local_sites_dir):
    for f in files:
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')) and 'app\\public' in root.lower():
            p = os.path.join(root, f)
            scanned_count += 1
            if scanned_count % 1000 == 0:
                print(f"  Scanned {scanned_count} files...")
            try:
                with Image.open(p) as img:
                    h = get_dhash(img)
                    if h:
                        for target in target_images:
                            dist = hamming_distance(target['hash'], h)
                            if dist < target['best_dist']:
                                target['best_dist'] = dist
                                target['best_match'] = p
            except Exception as e:
                pass

print(f"Scanning complete. Scanned {scanned_count} files total.")
print("Restoring files...")

restored_count = 0
for target in target_images:
    f = target['filename']
    best_match = target['best_match']
    best_dist = target['best_dist']
    
    print(f"Target: {f}")
    if best_match and best_dist <= 18:
        # Save backup of the current low-res file just in case
        backup_path = target['path'] + '.bak'
        if not os.path.exists(backup_path):
            shutil.copy2(target['path'], backup_path)
            
        # Overwrite with high-res original
        shutil.copy2(best_match, target['path'])
        print(f"  -> Restored from: {best_match} (dist: {best_dist})")
        restored_count += 1
    else:
        print(f"  -> No match found within distance threshold (closest dist: {best_dist})")

print(f"\nSuccessfully restored {restored_count} out of {len(target_images)} images.")
