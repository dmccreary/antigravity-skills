---
name: mascot-image-generator
description: Generates mascot images from prompts and cleanly removes the underlying background using floodfill logic.
---

# Mascot Generator Skill

The current version of Google's Antigravity does NOT support generating images with a real transparent background.  This is a HUGE problem for mascot generation, as the fake transparency checkerboard pattern is often mistaken for an actual background, and the white background is not removed at all.  This skill provides a workaround by generating the image with a solid white background and then using a custom flood fill script to remove the background while preserving the integrity of the mascot's features.  This is a TOTAL hack and it is crazy that Google does not use the powerful Nano Banana image processing library to do this natively, but it is what it is.  At least this way we can get the results we need until Google hopefully adds real transparency support in the future.

This skill allows you to reproducibly generate mascot images using the `generate_image` tool, while avoiding fake transparency checkerboards and removing white backgrounds perfectly.

## Poses

Each mascot has seven poses that can be used.  They are:

1. **Neutral** - both hands at sides, facing camera
2. **Welcome** - both arms outstretched in a welcoming gesture, facing camera
3. **Thinking** - hands clasped in front, chin resting on hands, thoughtful expression, facing camera
4. **Tip** - one hand at the side and one hand pointing up to a star above the hand with the pointer finger extended, looking up at the star, facing camera with a happy expression
5. **Warning** - both arms out with palms forward with a STOP gesture, stern expression, facing camera
6. **Encouragment** - one hand extended with a thumbs up gesture, happy expression, facing camera
7. **Celebration** - jumping up with both arms outstretched above head, facing camera with confetti and stars falling around, happy expression

## Step-by-step Instructions

1. **Modify the User's Image Prompt**:
   - Ensure "transparent background" is in the prompt, in addition to the style instructions and if not, add "transparent background" to the prompt.
   - Specify the output must be PNG format with an alpha channel (RGBA)
   - Inject the instruction: `Ensure the character has strong, continuous outlines.` (This helps the flood fill stop optimally).

2. **File Structure**:
   - Each pose will be in a file named after the pose:
   1. neutral.png
   2. welcome.png
   3. thinking.png
   4. tip.png
   5. warning.png
   6. encouragement.png
   7. celebration.png

3. If multiple mascots are being generated, the file name will be named after the animal name. (butterfly, dog, bee, etc.). If only one mascot is being generated the enclosing directory name is `mascot` such as `docs/img/mascot`

3. **Generate the Image**:
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
