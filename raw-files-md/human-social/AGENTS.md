# Human Social

You are operating **Human Social**, a white label system to unfold a folder with text and images into native pieces for Instagram Feed, Instagram Stories, and LinkedIn Feed.

## Required paths

Before acting, resolve these paths:

- `SKILL_DIR`: this skill's base directory — the path given as "Base directory for this skill" when it loads.
- `SCRIPT`: `${SKILL_DIR}/scripts/desdobrar.py`.
- `INPUT_FOLDER`: folder passed by the user in the command.

Never assume that the current directory is the skill folder. The user can trigger the unfold from any project, so all script commands must use the absolute path:

```bash
python3 "$SKILL_DIR/scripts/desdobrar.py" ...
```

## Required reading

1. `${SKILL_DIR}/CLAUDE.md`
2. `${SKILL_DIR}/DESDOBRAR.md`

## Main rules

- The flow is white label. Do not use old examples, texts, images, or brands as default.
- Every visual unfolding uses the GPT Image 2 model family — `gpt_image_2` via Higgsfield CLI on the scripted path, or Magnific `images_generate` with `mode: "gpt-2"` when the user chose a Magnific render path (see the routing rule in SKILL.md).
- Unfolding is not redesign: preserve the visual identity, font, colors, graphic elements, the user's logo/signature, and the composition logic of the master art.
- Every visual generation receives the same master art via `--base`, which enters as the first reference sent to GPT Image 2.
- Use `--reference-mode base-only` as default. Only use `--reference-mode all` when the other images are deliberately part of the same visual system.
- The visual prompt should be short: target format, exact text, and allowed adjustments. GPT Image 2 already understands the submitted image.
- The visible elements of the master art must remain in Feed and LinkedIn: photo/background, font, palette, logo, graphics, and composition. Varying format and text cannot turn into a new visual direction.
- Stories are a controlled exception: the 3 frames use the master art as identity, but must have different texts and images/backgrounds. The background image cannot be the same across all 3. You can vary crop, scene, background, angle, pose, lighting, and text area, while keeping campaign, brand, font, palette, and language.
- The final images must be born integrated: image + design + lettering + text in the same render.
- The agent must write all the final copies: Instagram Feed, Stories script, and LinkedIn.
- Every completed execution generates `desdobramento/apresentacao-desdobramento.pdf`.
- Every completed execution also syncs `desdobramento/output/`, a clean folder with only the finals for the user.
- The user's output goes in `INPUT_FOLDER/desdobramento/`, never inside the central Human Social folder.

## Minimum flow

1. Validate that `${SCRIPT}` exists.
2. Run `python3 "${SCRIPT}" check-cli`.
3. Run `python3 "${SCRIPT}" prep "${INPUT_FOLDER}"`.
4. Visually analyze the input images and choose a master art.
5. Create short prompts: target format + exact text + what to preserve.
6. Run `generate` for IG Feed, 3 Stories, and LinkedIn using the same master art in `--base`; in the Stories, ask for real variation of image/background/scene between the 3 frames.
7. Update `manifest.json`.
8. Run `python3 "${SCRIPT}" presentation-pdf "${INPUT_FOLDER}"`.
9. Respond with absolute paths of the final files and the clean folder `desdobramento/output/`.
