from PIL import Image
import os

def process():
    src = "/Users/dan/.gemini/antigravity/brain/df6f04c1-5ac4-4803-ba92-67828ec495f5/thinking_mountain_cover_sq_png_1775565844104.png"
    dst_dir = "/Users/dan/Documents/ws/antigravity-skills/story-assets"
    dst_sq = os.path.join(dst_dir, "cover-sq.png")
    dst_crop = os.path.join(dst_dir, "cover.png")

    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    img = Image.open(src)
    img.save(dst_sq)
    print(f"Saved original square to {dst_sq}")

    w, h = img.size
    target_ratio = 16/9
    new_h = w / target_ratio
    
    top = (h - new_h) * 0.5
    bottom = top + new_h
    
    img_cropped = img.crop((0, top, w, bottom))
    img_cropped.save(dst_crop)
    print(f"Saved cropped 16:9 to {dst_crop}")

if __name__ == "__main__":
    process()
