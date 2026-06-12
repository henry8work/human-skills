# Project Instructions

## Image Generation

- Always use `imageprompts.md` in this directory as the creative and prompt-structure guide for image generation.
- Treat `imageprompts.md` as the cinematography/prompt guide, not as a hard requirement to always render with Higgsfield.
- Before any image generation, always ask the user which of the **three render paths** to use (full rule in SKILL.md):
  1. **Magnific MCP direto** — `images_generate` with `mode: "imagen-nano-banana-2-flash"`, `resolution: "1k"`. Costs plan credits (~75/image), no extra money.
  2. **Magnific Híbrido (Run Unlimited)** — zero credits: pre-filled Space, the user clicks Run Unlimited in the browser, collect via `creations_search`/`spaces_state`.
  3. **Higgsfield** — paid, the user's Higgsfield account and credits (MCP/CLI).
- The model parameter on Magnific is `mode`, never `model`.
- Use `account_balance` only for measuring/checking credit balance when needed.
- Do not run image-generation tests without user approval.
