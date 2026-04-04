---
name: cover-image-generator
description: Generates a professional book cover image for intelligent textbooks using Antigravity's text-to-image generator.
---

# Cover Image Generator Skill

This skill generates a professional book cover image (1200x630 pixels) optimized for social media previews (Open Graph). It creates a composite design with the project's mascot on the left, a thematic montage in the background, and the book title in the center.

## Design Requirements

- **Dimensions**: 1200x630 pixels (1.91:1 aspect ratio).
- **Layout**:
    - **Left 20%**: The project mascot (e.g., a robot, animal, or character).
    - **Background**: A high-quality, professional montage of images/icons related to the course description topics.
    - **Center**: The book title in bold, clean, white sans-serif typography.
- **Style**: Modern, educational, "alive," and polished.

## Step-by-step Instructions

1. **Extract Project Context**:
   - Read `mkdocs.yml` to get the `site_name` (Book Title).
   - Read `docs/course-description.md` to identify key themes, topics, and visual metaphors for the background montage.
   - Check `CLAUDE.md` or `docs/img/mascot/` to identify the mascot character's description or name.

2. **Construct the Image Prompt**:
   - Use the following template to build the prompt for Antigravity's `generate_image` tool:
     ```text
     A professional book cover for a textbook titled "[BOOK_TITLE]". 
     Layout: On the far left (20% of the width), a [MASCOT_DESCRIPTION] is standing heroically. 
     Background: A sophisticated and dense montage of [TOPIC_KEYWORDS] including [VISUAL_METAPHORS]. 
     Center: The title "[BOOK_TITLE]" is prominently displayed in the center in bold, elegant white sans-serif typography. 
     Style: Professional, high-resolution, 1.91:1 aspect ratio, clean composition, vibrant colors, educational theme. 
     Dimensions: 1200x630.
     ```
   - **Important**: Ensure the aspect ratio (1.91:1) and dimensions (1200x630) are explicitly requested.

3. **Generate the Image**:
   - Call the `generate_image` tool with the constructed prompt.
   - Save the output to `docs/img/cover.png`.

4. **Update Project Metadata**:
   - Ensure `docs/index.md` includes the cover in its frontmatter:
     ```yaml
     image: /img/cover.png
     og:image: /img/cover.png
     ```
   - Update `mkdocs.yml` if necessary to include the social preview plugin configuration.

5. **Verification**:
   - Confirm the file exists at `docs/img/cover.png`.
   - Verify that the title is legible and the mascot/montage are correctly positioned.
