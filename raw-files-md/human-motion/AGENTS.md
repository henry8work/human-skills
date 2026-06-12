<!-- IMAGE_GENERATION_ROUTE_RULE -->
> Image generation rule: always use `imageprompts.md` as the creative/prompt guide when present. Before rendering any image, ask the user to choose one of the **three render paths**: 1) **Magnific MCP direto** — `magnific-mcp` tools (`images_generate` with `mode: "imagen-nano-banana-2-flash"`, `resolution: "1k"`; video via `video_generate` with `mode: "kling-25"`). Costs plan credits (~75/image), no extra money. 2) **Magnific Híbrido (Run Unlimited)** — zero credits: build a Space (`spaces_create` + `spaces_edit`) with pre-filled generator nodes, share the `webUrl`, the user clicks **Run Unlimited** in the browser, then collect results via `creations_search`/`spaces_state`. 3) **Higgsfield** — paid, the user's Higgsfield account and credits (MCP/CLI). The model parameter on Magnific is `mode`, never `model`. Use `account_balance` only to check/measure credits.
<!-- /IMAGE_GENERATION_ROUTE_RULE -->

# Image Generation Defaults

- The official Magnific MCP is `magnific-mcp` at `https://mcp.magnific.com`; use `account_balance` to check credit balance before and after paid generations.
- "Nano Banana 2" on Magnific is `mode: "imagen-nano-banana-2-flash"` (the higher-fidelity sibling is `imagen-nano-banana-2`, "Nano Banana Pro"). On the Higgsfield CLI, the slugs are `nano_banana_flash` (Nano Banana 2) and `nano_banana_2` (Nano Banana Pro).
- Measured on 2026-05-31: `imagen-nano-banana-2-flash` at `1k` consumed 75 plan credits on a Business plan.
- Default image payload: `resolution: "1k"`; use `2k`/`4k` only for finals or on explicit request.
- Do not use `mystic`, upscaling, or video generation unless the user explicitly asks.
- Do not run test image generations just to verify configuration — generation calls consume credits.
