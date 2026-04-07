from PIL import Image
import os
import argparse

def crop_image(image_path, output_path, target_ratio=16/9):
    """
    Crops a 1:1 square image into a 16:9 landscape version, 
    preserving the central composition by removing top and bottom padding.
    """
    try:
        img = Image.open(image_path)
        w, h = img.size
        
        if w != h:
            print(f"  [SKIPPED] {os.path.basename(image_path)} is not square.")
            return

        # Calculate height for the target aspect ratio
        new_h = w / target_ratio
        
        # Centered vertical crop
        top = (h - new_h) * 0.5
        bottom = top + new_h
        
        img_cropped = img.crop((0, top, w, bottom))
        img_cropped.save(output_path)
        print(f"  [SUCCESS] {os.path.basename(image_path)} -> {os.path.basename(output_path)} ({img_cropped.size})")
    except Exception as e:
        print(f"  [ERROR] {os.path.basename(image_path)}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Batch crop square story panels into landscape versions.")
    parser.add_argument("--dir", default=".", help="Directory containing the story folder (default: current)")
    parser.add_argument("--suffix", default="-sq.png", help="Suffix identifying square images (default: -sq.png)")
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.dir):
        print(f"Error: {args.dir} is not a valid directory.")
        return

    # Find all *-sq.png files in the directory
    files = [f for f in os.listdir(args.dir) if f.endswith(args.suffix)]
    
    if not files:
        print(f"No square images found with suffix '{args.suffix}' in {args.dir}")
        return

    print(f"Found {len(files)} square images. Cropping to 16:9...")
    for f in sorted(files):
        sq_path = os.path.join(args.dir, f)
        # Output filename: panel-01-sq.png -> panel-01.png
        out_name = f.replace(args.suffix, ".png")
        out_path = os.path.join(args.dir, out_name)
        crop_image(sq_path, out_path)

if __name__ == "__main__":
    main()
