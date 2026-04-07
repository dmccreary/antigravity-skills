---
name: story-image-generator
description: Automates the generation and processing of 16:9 story panels using 1:1 centered squares with vertical padding to prevent clipping. Optimized for Google Antigravity.
---

# Story Image Generator Skill

This skill formalizes a stable, high-quality workflow for generating graphic novel or textbook story panels without unintended framing or clipping of key visual elements. It is particularly designed for the Antigravity image generator's behavior.

## Core Methodology: The "Safe Zone" Workaround
Antigravity often crops native 16:9 images too tightly. To fix this, we generate **1:1 Square** images with **22% vertical padding** at the top and bottom, which are then center-cropped to a perfect **16:9 landscape**.

## Step-by-Step Instructions

### 1. Story Analysis 
- **Identify Panels**: Locate all panel placeholders in the project's `index.md`.
- **Extract Prompts**: Prompts are typically located in the `description` or wrapped in `<details>` tags near the image link.

### 2. Prompt Transformation (REQUIRED)
Wrap **every** panel description with the following **CRITICAL RULE** at both the **very beginning** and the **very end**.

> **CRITICAL: NO RELEVANT CONTENT, TEXT, OR CHARACTERS IN THE TOP 15% OR BOTTOM 15% of the image. All essential elements must be in the central 70% vertical area. DO NOT PUT WHITE EDGES ON THE LEFT OR RIGHT SIDES.**

- **No White Edges**: Ensure the illustration extends to the full width of the square frame.
- **Centering**: Instruct the model to center all primary action horizontally and vertically.

### 3. Specialized Cover Generator
For `cover.png`, the title text is the most critical element.
- **Prompt Modification**: Explicitly command the model to keep the title text within the **central 70% Safe Zone**.
- **Rule Placement**: Again, place the padding rule at the top and bottom of the prompt.

### 4. Image Generation Loop
- Call the `generate_image` tool for each panel.
- Save result as `panel-XX-sq.png` (e.g., `panel-01-sq.png`, `cover-sq.png`).

### 5. Automated Cropping
- Execute the `batch_crop.py` script from the skill's directory using Python 3:
  ```bash
  python3 /Users/dan/Documents/ws/antigravity-skills/skills/story-image-generator/scripts/batch_crop.py --dir [STORY_DIR]
  ```
- This will produce the final 16:9 `panel-XX.png` files.

### 6. Vision-Based Verification (OCR)
- **Cover Check**: Use `view_file` on the final `cover.png`.
- **Validation**: Confirm the title is:
  1.  Present and correctly spelled.
  2.  Legible and not too small.
  3.  **Not clipped** at the top or bottom boundaries of the 16:9 frame.

### 7. Metadata Preservation (CRITICAL)
- **DO NOT REMOVE** the `<details>`, `summary`, or HTML comment wrappers surrounding the image prompts in `index.md`.
- These elements are used to store the prompt metadata for future regeneration.
- Note: These tags are typically hidden in the production site via CSS, so they must remain in the source file for version control and iterative refinement.

## Verification Plan
- **File Exist Check**: Confirm both `*-sq.png` and `*.png` files exist for all panels.
- **Visual Consistency**: Ensure the character and art style remain stable across the entire sequence.
