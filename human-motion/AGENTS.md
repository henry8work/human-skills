<!-- IMAGE_GENERATION_ROUTE_RULE -->
> Image generation rule: always use `imageprompts.md` as the creative/prompt guide when present. Before rendering any image, ask the user to choose: **Magnific** via direct MCP/API (`nano-banana-pro-flash`, `resolution: "1K"`, intended free/default) or **Higgsfield** via MCP/CLI (paid). Do not use `mcp__magnific_oauth.images_generate` for routine Magnific image generation unless explicitly requested; use `magnific-oauth.account_balance` only to check/measure credits.
<!-- /IMAGE_GENERATION_ROUTE_RULE -->

# Global Instructions

## Repository Policy

- **NEVER** clone, download, or use external GitHub repositories unless the user explicitly asks for it.
- Use only the local repo files and the skills/agents already installed locally.
- If a task could involve fetching external code, ask the user first before proceeding.

## Image Generation Defaults

- The official Magnific OAuth MCP is configured as `magnific-oauth` at `https://mcp.magnific.com`; use its account/balance tools when available to check credit balance before and after generations.
- When the user asks to generate images with the Magnific MCP, use `mcp__magnific_full.magnific_generate_image` by default.
- Interpret "Nano Banana 2" / "nanobanana_2" as Magnific model `nano-banana-pro-flash`.
- Measured on 2026-05-31: official OAuth model `imagen-nano-banana-2-flash` at `1k` consumed 75 credits on the current Business plan; `account_balance.plan.isUnlimitedMode` was `false`.
- Default image payload:
  - `resolution`: `"1K"`
  - `use_google_search_tool`: `false`, unless the prompt needs current or real-world grounding.
- Do not use `mystic`, `nano-banana-pro`, `2K`, `4K`, upscaling, or video generation unless the user explicitly asks.
- Do not run test image generations just to verify configuration, because generation calls may consume account/API credits depending on the plan.
