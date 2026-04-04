import sys
from PIL import Image, ImageDraw

def process(input_path, output_path):
    print(f"Loading '{input_path}'...")
    img = Image.open(input_path).convert("RGBA")
    
    # 1. Floodfill from all 4 corners to remove pure white background
    w, h = img.size
    for c in [(0, 0), (w-1, 0), (0, h-1), (w-1, h-1)]:
        if sum(img.getpixel(c)[:3]) > 700:
            ImageDraw.floodfill(img, xy=c, value=(255, 255, 255, 0), thresh=40)
            
    # 2. Halo removal (2 passes to catch 1px and 2px light-colored fringing)
    pixels = img.load()
    
    for pass_num in range(2):
        halo_pixels = []
        for y in range(h):
            for x in range(w):
                if pixels[x, y][3] > 0:  # If pixel is not transparent
                    # Check if it borders a transparent pixel
                    is_edge = False
                    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < w and 0 <= ny < h:
                            if pixels[nx, ny][3] == 0:
                                is_edge = True
                                break
                    
                    if is_edge:
                        r, g, b, a = pixels[x, y]
                        # Only dissolve the pixel if it is a light color (white/gray fringe)
                        if r > 120 and g > 120 and b > 120:
                            halo_pixels.append((x, y))
        
        # Clear the identified halo pixels
        for x, y in halo_pixels:
            pixels[x, y] = (255, 255, 255, 0)
            
    img.save(output_path, "PNG")
    print(f"Background successfully removed. Saved to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python remove_bg.py <input_img_path> <output_img_path>")
        sys.exit(1)
        
    process(sys.argv[1], sys.argv[2])
