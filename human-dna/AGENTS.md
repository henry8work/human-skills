# Project Instructions

## Image Generation

- Always use `imageprompts.md` in this directory as the creative and prompt-structure guide for image generation.
- Treat `imageprompts.md` as the cinematography/prompt guide, not as a hard requirement to always render with Higgsfield.
- Before any image generation, always ask the user which render path to use:
  - Magnific, using the MCP/API direct path, intended as the free/default option.
  - Higgsfield, using MCP/CLI, paid.
- For Magnific image generation, use the direct Magnific API/MCP call with `nano-banana-pro-flash` and `resolution: "1K"` unless the user explicitly chooses another model or size.
- Do not use `mcp__magnific_oauth.images_generate` for routine Magnific image generation unless the user explicitly asks for that route, because it was observed debiting credits.
- Use `magnific-oauth.account_balance` only for measuring/checking credit balance when needed.
- Do not run image-generation tests without user approval.
