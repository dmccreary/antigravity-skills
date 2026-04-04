---
name: mascot-image-generator
description: Generates mascot images from prompts and cleanly removes the underlying background using floodfill logic.
---

# Mascot Generator Skill

The current version of Google's Antigravity does NOT support generating images with a real transparent background.  This is a HUGE problem for mascot generation, as the fake transparency checkerboard pattern is often mistaken for an actual background, and the white background is not removed at all.  This skill provides a workaround by generating the image with a solid white background and then using a custom flood fill script to remove the background while preserving the integrity of the mascot's features.  This is a TOTAL hack and it is crazy that Google does not use the powerful Nano Banana image processing library to do this natively, but it is what it is.  At least this way we can get the results we need until Google hopefully adds real transparency support in the future.

This skill allows you to reproducibly generate mascot images using the `generate_image` tool, while avoiding fake transparency checkerboards and removing white backgrounds perfectly.

## Step-by-step Instructions

1. **Modify the User's Image Prompt**:
   - Strip any requests for a "transparent background".
   - Inject the instruction: `Style must include a solid pure white background (#FFFFFF).`
   - Inject the instruction: `Ensure the character has strong, continuous outlines.` (This helps the flood fill stop optimally).

2. **Generate the Image**:
   - Use the `generate_image` tool with the modified prompt.
   - Note the absolute path of the generated `.png` artifact.

3. **Process with the Script**:
   - Use `run_command` to execute the automated background removal tool included in this skill's `scripts` folder.
   - Command pattern:
     ```bash
     python3 /Users/dan/.gemini/antigravity/skills/mascot-generator/scripts/remove_bg.py "<ARTIFACT_IMAGE_PATH>" "<DESTINATION_PATH>"
     ```
   - *Note: This script uses a flood fill from the corners and anti-aliasing halo reduction, which ensures white interior sections (eyes, teeth) stay intact while outer fringes are erased.*

4. **Response**: Let the user know the file has been successfully exported with a real transparent background to their final location!
