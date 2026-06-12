---
name: human-social
description: Unfolds a folder containing text + images into native pieces for Instagram Feed, Instagram Stories, and LinkedIn Feed — not a resize, creates new images per platform with platform-native captions. Image render asks the user to choose one of three render paths — Magnific direct (plan credits), Magnific Hybrid Run Unlimited (zero credits), or Higgsfield (paid). Use whenever the user asks to "unfold this folder", "adapt for Instagram and LinkedIn", "create versions for feed/stories/linkedin", "make a post from this material", or points at a folder path asking for social content. Triggers (EN/PT) — unfold content, social adaptation, feed/stories/linkedin from folder, desdobrar pasta, adaptar pra Instagram e LinkedIn, criar versões pra redes, post a partir de pasta. Can be triggered as a sub-flow from any other skill that needs to unfold material into social pieces.
---

# Human Social

Takes a folder containing text + images and generates **native** pieces (not resize) for:
- Instagram Feed
- Instagram Stories (multi-card)
- LinkedIn Feed

Each platform gets a fresh image referencing the original material + its own caption.

## Preflight — confirm the render provider is ready (first run)

Before the first render in a session, confirm the chosen provider is actually connected. Do not assume it is.

- Magnific: verify the `magnific-mcp` tools respond (call `account_balance` — the cheapest probe; it also shows remaining plan credits). If they do not respond, the MCP is not set up — route the user to human-setup.
- Higgsfield (paid): verify the higgsfield CLI is installed and logged in (e.g. higgsfield account status). If the command is missing or not authenticated, it is not set up.

If the required provider is NOT ready:
1. Tell the user plainly which dependency is missing.
2. Route them to the human-setup skill for step-by-step, OS-specific setup (Mac/Windows).
3. Never hard-fail: meanwhile deliver the final English prompt ready to copy plus the exact provider command, so the user has something actionable immediately.

Only proceed to render once the provider is confirmed ready.

## Visual generation routing

<!-- IMAGE_GENERATION_ROUTE_RULE -->
> Image generation rule: always use `imageprompts.md` as the creative/prompt guide when present. Before rendering any image, ask the user to choose one of the **three render paths**: 1) **Magnific MCP direto** — `magnific-mcp` tools (`images_generate` with `mode: "imagen-nano-banana-2-flash"`, `resolution: "1k"`; video via `video_generate` with `mode: "kling-25"`). Costs plan credits (~75/image), no extra money. 2) **Magnific Híbrido (Run Unlimited)** — zero credits: build a Space (`spaces_create` + `spaces_edit`) with pre-filled generator nodes, share the `webUrl`, the user clicks **Run Unlimited** in the browser, then collect results via `creations_search`/`spaces_state`. 3) **Higgsfield** — paid, the user's Higgsfield account and credits (MCP/CLI). The model parameter on Magnific is `mode`, never `model`. Use `account_balance` only to check/measure credits.
<!-- /IMAGE_GENERATION_ROUTE_RULE -->

**Always ask the render path.** At the start of each unfold run, present the three options and wait for an explicit choice — never assume; the choice applies to all three platforms. Ask it as: *"Como você quer renderizar? 1) Magnific direto (créditos do plano), 2) Híbrido Run Unlimited (zero créditos, você clica no navegador), 3) Higgsfield (pago)."* **Never silently render on Higgsfield.**

## Language

Mirror the user's language. **Captions are written in the audience language** — ask if not obvious from the briefing.

## Complete intelligence

- [CLAUDE.md](CLAUDE.md) — skill overview
- [DESDOBRAR.md](DESDOBRAR.md) — full unfolding pipeline, step by step (read it before executing)
- [scripts/desdobrar.py](scripts/desdobrar.py) — Python infra (Higgsfield path; needs `reportlab` only for the fancy PDF, falls back gracefully without it)
- [origem/](./origem) — synthetic example input (fictional brand)

## Expected input

A folder containing:
- 1 `.txt` file with caption/briefing
- 1+ images (`.png`, `.jpg`, `.jpeg`, `.webp`)

## Mandatory flow

1. **Confirm the input folder path**.
2. **Validate** that it has `.txt` + at least one image.
3. **Ask the routing question** (the three render paths) per the rule above.
4. **Validate** the chosen provider is logged in.
5. **Generate** Instagram Feed (1:1 or 4:5) with its own caption.
6. **Generate** Instagram Stories (9:16, multi-card with script).
7. **Generate** LinkedIn Feed (1.91:1 or 1:1) with a professional caption.
8. **Save** inside the input folder itself.

## Default output (EXCEPTION to the global rule)

Unlike other skills, Human Social writes **inside the input folder**, not under `human-output/`:

```
<input-folder>/desdobramento/
├── instagram-feed.png
├── instagram-feed.txt
├── instagram-stories/
│   ├── story-01.png
│   ├── story-02.png
│   └── roteiro.txt
├── linkedin-feed.png
├── linkedin-feed.txt
└── manifest.json
```

## Non-negotiable rules

- **No resize** — always create a fresh image per platform with a reference chain.
- Always ask the routing question before rendering.
- Per-platform caption strategy:
  - IG Feed: visual, emotional, light CTA
  - IG Stories: conversational, can break into cards
  - LinkedIn: professional, strong hook, no excessive hashtags
- `manifest.json` always present for traceability.

## Shared sub-flow

If another skill needs to unfold a material it produced into IG Feed/Stories/LinkedIn, it can trigger `human-social` as a sub-flow pointing to the source folder.

## Final delivery

`desdobramento/` folder as clickable link + all generated PNGs/JPGs/JSONs/captions as clickable links.
