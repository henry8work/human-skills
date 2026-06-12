# DESDOBRAR — full unfolding pipeline (zero-tech onboarding)

> Loaded by the `human-social` skill (see [SKILL.md](SKILL.md)). This file documents the **scripted Higgsfield path** of the pipeline. If the user chose a Magnific render path in the routing question, keep the same flow (master art, prompts, formats, safe zones, manifest) but render via `magnific-mcp` `images_generate` with `mode: "gpt-2"` and the master art as image reference, instead of calling the script's `generate` subcommand.

Usage:
```
/desdobrar /path/to/folder
```

**Important:** the user of this system IS NOT TECHNICAL. They are a photographer/art director. They do not know what `.env`, "API key", "endpoint", or "environment variable" means. Every interaction with them is in 100% human language. Technical errors turn into WhatsApp-style conversation, not a stack trace.

---

## Step 0 — Higgsfield CLI Pre-flight (CONVERSATIONAL — before anything else)

In the commands below, `$SKILL_DIR` is this skill's base directory — the path given as "Base directory for this skill" when it loads. Substitute it before running:

```bash
SOCIAL_SCRIPT="$SKILL_DIR/scripts/desdobrar.py"
test -f "$SOCIAL_SCRIPT"
```

Run:
```bash
python3 "$SKILL_DIR/scripts/desdobrar.py" check-cli
```

The output is JSON with `status`. Handle each case:

### `status: "ok"`
The Higgsfield CLI exists and is logged in. Don't drag it out. Jump straight to Step 1.

### `status: "missing"`
The Higgsfield CLI is not installed. Send in chat (human text, copy and adapt):

> Before we start, I need to connect Higgsfield here in Claude Code — it's what will generate the new images for each network.
>
> I'll install the CLI with `npm install -g @higgsfield/cli`. If Node.js is missing, I'll let you know and stop.
>
> Then I'll log in with you.

After installation, run `higgsfield auth login` and ask the user to complete login in the browser.

### `status: "login_required"`
The CLI exists, but needs login. Send:

> Higgsfield is installed, just need to connect the account. I'll open login with `higgsfield auth login`; finish it in the browser and let me know.

Use the real command:

```bash
higgsfield auth login
```

Then run:

```bash
python3 "$SKILL_DIR/scripts/desdobrar.py" check-cli
```

- If it returns `ok`: reply **"Higgsfield connected. Let's go."** and move to Step 1.
- If it stays `login_required`: ask to redo the login.

---

## Step 1 — Prep

Run:
```bash
python3 "$SKILL_DIR/scripts/desdobrar.py" prep "<folder>"
```

JSON output with:
- `texto_arquivo` — path of the `.txt` found
- `texto_conteudo` — content read
- `imagens` — absolute paths of the images
- `saida` — path of `desdobramento/`
- `output` — clean delivery folder at `desdobramento/output/`
- `manifest` — path of `manifest.json`

If `.txt` or images are missing, the script aborts with a clear message — relay it to the user in a friendly tone.

---

## Step 2 — Choose the master art

Use the **Read tool** on the original images and choose ONE master art.

Priority:
1. image already laid out with photo/visual + lettering;
2. image that most resembles a finished piece;
3. strongest main image, if no art with lettering yet exists.

This same master art goes to IG Feed, Stories, and LinkedIn. Don't choose a different base per network, because that creates pieces with different visual worlds.

Note only the essential:
- main photo/visual;
- font style;
- colors;
- graphic elements;
- logo/signature;
- composition and hierarchy.

Operational rule: every visual generation uses `gpt_image_2` and receives the master art via `--base`. The script uses `--reference-mode base-only` by default so other images don't confuse the model. Use `--reference-mode all` only if the user requests it or if the other images are clearly part of the same visual system.

A good prompt here is short. GPT Image 2 already sees the art. Don't write a long briefing or describe everything in the image: just state the target format, the text that goes in, and what may change. Usually 4 to 7 lines is enough. Reinforce that the visible elements of the master art remain: photo, background, font, logo, graphics, colors, and composition. For Stories, the focus shifts: preserve identity and character/product, but request real variation of background/scene between frames.

For a punctual adjustment to an already-generated piece, use the piece itself as `--base` and ask only for the swap:

```
Use the attached artwork.
Keep everything the same.
Only replace the headline with: "{NEW_HEADLINE}"
Preserve photo, background, font style, colors, logo and layout.
```

---

## Step 3 — Generate Instagram Feed (1 image, 3:4)

Write a short prompt in `<folder>/desdobramento/_prompts/ig-feed.txt`. Use the master art and request only the transformation:

```
Use the attached master artwork.
Convert it to Instagram Feed portrait 3:4 (1080x1440).
Keep the same photo/background, font style, colors, graphic elements, logo and composition.
Change only crop, spacing, hierarchy and text. Keep all important visual elements.
Text: "{SHORT_HEADLINE}" / "{optional SHORT_SUPPORT}"
No redesign. No new photo. No new style.
```

Then run:
```bash
python3 "$SKILL_DIR/scripts/desdobrar.py" generate "<folder>" ig-feed "<folder>/desdobramento/_prompts/ig-feed.txt" --base <master-art.png>
```

The script uploads the images with `higgsfield upload create`, calls `higgsfield generate create gpt_image_2`, waits with `higgsfield generate wait`, downloads the resulting PNG to `<folder>/desdobramento/instagram-feed.png`. Returns JSON with `output_path`, `higgsfield_url`, `base_reference`, and `reference_files`.

After the render, compare with the master art. If the photo, font, palette, or language changed too much, reject and regenerate with an even more direct prompt: "make it much closer to the attached master artwork; only change the format and text".

---

## Step 4 — Generate Instagram Stories (always 3 frames, 1080×1920)

Stories are also born from the same master art. Always generate 3 frames. Don't use a different base image per story, unless the user requests a sequence based on multiple images.

Each story must carry different information and a different image/background. The pitfall to avoid is xerox with swapped text. The image behind the text cannot remain the same across all three frames. You may vary crop, extended background, solid area for text, layout breathing, angle, pose, lighting, nearby situation, derived scenery, or character/product in another framing; you cannot change brand, font, logo, palette, or main language.

Before writing the prompts, define a variation plan:

- Story 01: frame closest to the master art, but with adjusted crop, depth, background extension, or lighting. Cannot just be the same photo with new text.
- Story 02: the clearest visual variation of the trio: another angle, pose, derived scenery, different background, or strong solid area with brand color.
- Story 03: closing/CTA with another background, different composition, different lighting, or solid text area; still within the same campaign.

Write `<folder>/desdobramento/_prompts/story-NN.txt` with a short prompt:

```
Use the attached master artwork.
Convert it to Instagram Stories 9:16 (1080x1920).
Keep the same campaign identity: brand/logo, font style, colors and graphic language.
Create a derivative variation, not a copy. The background/image must be visibly different from the other Stories.
Change vertical crop/extension, safe area, text placement, background/image and text.
Use one: alternate angle, pose, related setting, changed lighting, background extension or solid brand-color field.
Text: "{STORY_HEADLINE}" / "{optional MICROCOPY}"
No unrelated new objects. No new brand style. Do not keep the exact same background photo with only new text.
```

Run in parallel for each story, always with the same master art:
```bash
# in parallel
for N in 01 02 03; do
  python3 "$SKILL_DIR/scripts/desdobrar.py" generate "<folder>" ig-stories "<folder>/desdobramento/_prompts/story-$N.txt" --base "<master-art.png>" --output "story-$N.png" &
done
wait
```

If any fails, continue with the others — record in the manifest.

---

## Step 5 — Generate LinkedIn Feed (1 image, 16:9)

LinkedIn does not get a different visual direction. It is an adaptation of the same master art into a more editorial/sober register, keeping photo, font, colors, and recognizable elements. Write the prompt in `<folder>/desdobramento/_prompts/linkedin-feed.txt`:

```
Use the attached master artwork.
Convert it to LinkedIn Feed landscape 16:9 (1920x1080).
Keep the same photo/background, font style, colors, graphic elements, logo and composition.
Change only crop, horizontal canvas, spacing, readability and text. Keep all important visual elements.
Text: "{optional TAG}" / "{LINKEDIN_HEADLINE}" / "{optional LINKEDIN_SUPPORT}"
No redesign. No new photo. No new style.
```

Run:
```bash
python3 "$SKILL_DIR/scripts/desdobrar.py" generate "<folder>" linkedin-feed "<folder>/desdobramento/_prompts/linkedin-feed.txt" --base <master-art.png>
```

Saved at `<folder>/desdobramento/linkedin-feed.png`.

---

## Step 6 — Write all final copies

Read the original `texto_conteudo` (from Step 1). Write **all final delivery texts**, not just images:

### `<folder>/desdobramento/instagram-feed.txt`
- Hook in the first 2 lines (before the "...see more")
- Short sentences, short paragraphs, space between them
- 60-120 words
- Light CTA (1 line)
- 3-7 hashtags at the end, after a blank line
- Oral, rhythmic, social tone

### `<folder>/desdobramento/instagram-stories/roteiro.txt`
Exactly 3 sections, one per story, with on-screen copy, suggested sticker, and micro-CTA:
```
STORY 01 — story-01.png
Headline on image: "WHOEVER NEEDS PERFECTION DIES"
Suggested sticker: question box
Micro-CTA: "reply here ↓"

STORY 02 — story-02.png
Headline: "They stopped having ideas in 2018"
Sticker: (none)

... etc

STORY {N} — story-NN.png  (last)
Headline: "Full carousel on the feed →"
Sticker: link sticker pointing to the feed post
```

### `<folder>/desdobramento/linkedin-feed.txt`
- Substantive insight on the first line (NOT clickbait hook)
- 1st person or direct declarative voice
- 160-320 words
- Articulated paragraphs (3-5 lines each)
- Includes at least 1 number / quote / concrete example
- Editorial CTA (open question) or none
- 2-4 hashtags at the end
- Substantive-editorial tone

**Critical:** after writing the 3, compare. The copies can have different registers, but the images must still look like unfoldings of the same master art.

---

## Step 7 — Update manifest

Read `<folder>/desdobramento/manifest.json`, fill `outputs` with paths and Higgsfield URLs (that came from the `generate` JSON), mark `status: "pronto"` or `"parcial"`. Save.

---

## Step 8 — Generate presentation PDF

After generating images and copies, run:

```bash
python3 "$SKILL_DIR/scripts/desdobrar.py" presentation-pdf "<folder>"
```

The final file lands at:

```text
<folder>/desdobramento/apresentacao-desdobramento.pdf
```

The PDF must show:
- received base text;
- base images used as reference;
- generated Instagram Feed + caption;
- generated Stories + script;
- generated LinkedIn Feed + caption;
- model used (`gpt_image_2`) and references sent.

The PDF must not list filenames on the page. It should look like a simple and beautiful presentation: 16:9 layout, large images, breathing room, typographic hierarchy, correct accents, and readable text. Each page must make clear whether it is Base, Instagram Feed, Instagram Stories, Stories script, LinkedIn, or clean delivery.

The script also creates/syncs:

```text
<folder>/desdobramento/output/
```

This is the user-friendly folder: it gathers only final files, with no logs, prompts, or technical manifest.

If a piece failed, the PDF should still be generated with what exists, and the manifest stays `parcial`.

---

## Step 9 — Chat summary

```
✅ Unfolding ready. Everything is at:
   <folder>/desdobramento/

📱 Instagram Feed:    instagram-feed.png + instagram-feed.txt
📲 Instagram Stories: 3 frames in instagram-stories/ + roteiro.txt
💼 LinkedIn Feed:     linkedin-feed.png + linkedin-feed.txt
📄 Presentation PDF:  apresentacao-desdobramento.pdf
📦 Clean delivery:    output/

Cost: check credits in Higgsfield.
```

Show absolute paths so the user can copy/open in Finder.

---

## Inviolable rules

- **CLI/login pre-flight is conversational, doesn't block.** Never tell the user "edit file Y". Lead installation/login with human language.
- **The user never sees the term `.env`, "API key", "endpoint", or "FAL_KEY".** For them: "Higgsfield connected".
- **Vision ALWAYS on original images.** Never guess palette/mood — open the file and look.
- **GPT Image 2 ALWAYS (the model family).** Visual unfoldings are `higgsfield generate create gpt_image_2` on the scripted path, or Magnific `images_generate` with `mode: "gpt-2"` when the user chose a Magnific path.
- **Unfolding, not redesign.** If Feed or LinkedIn look like a new art inspired by the original, it's wrong.
- **Base image ALWAYS attached.** Each `generate` must use `--base <master-art>`; the script uploads this image as first reference and passes it along with `--image`.
- **Base-only as default.** Don't send all images if they aren't needed. Multiple competing refs cause visual drift.
- **Short prompt.** GPT Image 2 already reads the art. Ask for the transformation, format, exact copy, and only what needs to change.
- **Stories always in 3.** Generate three variations of the same master art, with different texts and different images/backgrounds. The trio must vary scene/crop/background/lighting without inventing a new visual direction.
- **Reference chain is `generate`.** It already uploads the master art and uses the Higgsfield UUID. Don't try to chain manually.
- **Each format is independent.** Stories failing doesn't stop Feed/LinkedIn.
- **Complete copies, from scratch.** Instagram Feed, Stories script, and LinkedIn must have their own final texts. No lazy adaptation.
- **Final PDF mandatory.** Every execution ends with `presentation-pdf`.
- **Clean output mandatory.** Every completed execution must leave `desdobramento/output/` organized for the user.
- **Stateless.** Each `/desdobrar` is a fresh execution. No cache, no state.
