# 01 — Brand Identity

> **Where to paste:** `🏷️ Brand Identity` page in Notion.
> This page is read by R2 on **every run** and its variables are interpolated into the editorial pipeline and into the render prompts.

---

## Paste the content below into the page

---

## Brand variables

| Variable | Value | Where it appears |
|---|---|---|
| `brand_name` | `Human Academy` | Cover (signature), slide 9 (logo), caption |
| `brand_handle` | `@humanacademy` | Brand bar of every slide, cover |
| `brand_slug` | `human-academy` | Local working folder (`~/human-academy/`), folder on Google Drive, Routine names |
| `brand_color_primary` | `#EC5E26` | Accent on every slide (keywords, progress, accent bar) |
| `brand_color_dark` | `#1B1411` | Dark slide background (default warm-dark) |
| `brand_color_light` | `#F1ECE3` | Light slide background (default warm-cream) |
| `brand_subject` | `AI for creatives` | Editorial triage, hashtags, source suggestion |
| `brand_audience_term` | `students` | How the pipeline may reference the audience |
| `brand_voice_anchor` | `Folha de S.Paulo` | Editorial reference outlet cited in the Editorial Manual |
| `brand_email_from` | `news@humanacademy.com.br` (optional) | When sending daily reports via email |
| `brand_has_logo` | `true` / `false` | Whether the brand has a logo PNG attached below. If `true`, R2 uses the logo on slides 1 and 9 |
| `cron_r1_hours` | `9,13,17` | R1's crontab |
| `cron_r2_time` | `08:00` | R2 target time. **The actual schedule is `*/30 8-22 * * *`** — the first tick of the day in which the app is open runs. Following ticks detect `.completed` and exit immediately (~2s, negligible cost). |

---

## Rule for displaying the brand on the slides

| Slide | What appears |
|---|---|
| **1 — Cover** | `BY {brand_name}` as signature + `{brand_handle}` in the brand bar + **small** logo in the corner (if `brand_has_logo=true`) |
| **2-8 — Internal** | `{brand_handle}` and a discreet detail signature. **No logo and no slide numbering.** |
| **9 — CTA** | **Large, centered** logo as the protagonist + short CTA (if `brand_has_logo=true`) — otherwise, large textual lockup with `{brand_name}` + short CTA |

Keeps the feed clean. Brand accumulates on the cover + CTA. Intermediate slides breathe. On slide 9, the text does not summarize the carousel: only a CTA of up to 8 words enters, with a discreet handle if necessary.

---

## Brand logo

If `brand_has_logo = true`, attach a **PNG of the logo** below (preferred: transparent background, minimum 800×800px, clean square or rectangular format). R2 downloads this file at the start of each run and uses it on slides 1 and 9.

> **Attach here:** _(drag the PNG of the brand logo into this page, below this line)_

To replace the logo at any time = replace the attachment here. The next run uses the new one.

If you do NOT have a logo (or prefer to use only typesetting with the brand name), set `brand_has_logo = false` in the table above and ignore the attachment — R2 falls back to a typographic lockup on slide 9 (`{brand_name}` in cover font + monogram).

---

## Voice and editorial identity

Describe in 3-5 sentences:

**Tone of voice** (Human Academy example):
> Provocative mentor. Direct, didactic, slightly sharp, culturally informed. Speaks with an intelligent adult. Does not talk about AI — talks about creative quality in the AI era. AI becomes context. Quality becomes the subject.

**Central editorial principle:**
> {brand_name} does not talk about {brand_subject}. It talks about [quality / method / criterion / decision] in the context of {brand_subject}.

**What the brand IS:**
- Direct · provocative · culturally informed · with criterion · method

**What the brand is NOT:**
- Excited · motivational · self-help guru · tech bro · tool salesperson

**How NOT to address the audience:**
- List terms that infantilize or genericize (Human Academy case: never "Human gang", always "Human students")

---

## How R2 uses this page

R2 reads this page at the start of each run and creates a **substitution dictionary**:

```python
brand = {
  "brand_name": "Human Academy",
  "brand_handle": "@humanacademy",
  "brand_color_primary": "#EC5E26",
  "brand_has_logo": True,
  "brand_logo_path": "./state/{TODAY}/logo.png",  # downloaded from the page attachment
  ...
}
```

Every prompt sent to GPT Image 2 (`gpt_image_2`) and to the `claude` CLI goes through interpolation:

```python
prompt = prompt_template.replace("{brand_name}", brand["brand_name"])
                        .replace("{brand_color_primary}", brand["brand_color_primary"])
                        ...
```

Swapping brands = editing this page. **Nothing in the R2 code needs to change.**

---

## Dedicated workspace (recommended)

To isolate tokens and permissions, it's recommended to create a **separate Notion workspace** for each brand. Advantages:

- The Integration Token has scope restricted to the workspace
- Does not mix with personal docs or docs from other brands
- Allows sharing with the brand team without exposing the rest

You can use a free Notion workspace — one brand per workspace.

---

## Setup wizard

The first time the agent runs the setup, it fills in this page asking one thing at a time. You do not fill it in by hand on the first run — you only **edit it here afterwards** if you want to tweak it.

For the wizard flow, see `02-Setup-Wizard.md`.
