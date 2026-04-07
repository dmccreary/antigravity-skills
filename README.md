# Antigravity Skills Collection

> [!WARNING]
> **Token Cost Warning**: As reported on r/google_antigravity, the IDE currently feeds every file in the skills folder into the context window for every prompt. Large skill folders can significantly increase token usage. Use with caution.

## Supported Skills (Experimental)

1. **[Story Image Generator](skills/story-image-generator/)**: Automates 16:9 story panel production using centered square padding and batch cropping. Optimized for Antigravity-specific clipping workarounds.
2. **[Cover Image Generator](skills/cover-image-generator/)**: Social preview (1200x630) asset generation.
3. **[Mascot Image Generator](skills/mascot-image-generator/)**: Character asset generation with transparency workflows.

---

> [!NOTE]
> **Image‑generation quota**: The Antigravity image service currently allows **only 12 images per five‑hour window**. This limit is insufficient for many educational use‑cases. We are actively researching low‑cost alternatives to support teachers worldwide who need higher‑volume image generation.

---

## Publishing Documentation

This repository includes a GitHub Actions workflow (`.github/workflows/publish.yml`) that automatically builds and deploys the documentation site to GitHub Pages on every push to the `main` branch when documentation files change.

### How it works
- **Trigger**: Push to `main` affecting `docs/**` or `mkdocs.yml`.
- **Steps**:
  1. Checkout the repository.
  2. Configure Git user for the automated commit.
  3. Commit any generated documentation changes.
  4. Push the commit back to the repository.
  5. Install `mkdocs` and `mkdocs-material`.
  6. Deploy the site with `mkdocs gh-deploy --force`.

### Manual Deployment
If you need to deploy locally, run:
```bash
pip install mkdocs mkdocs-material
mkdocs gh-deploy --force
```

### Badges
[![Publish](https://github.com/dmccreary/antigravity-skills/actions/workflows/publish.yml/badge.svg)](https://github.com/dmccreary/antigravity-skills/actions/workflows/publish.yml)

---

Request a Quota Reset: Contact Google Cloud Support or use the "Feedback" tool if you encounter Bug AG-859 (IDE capacity usage without work).