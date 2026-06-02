# 03 — Notion Template (V2.5)

> **Do not paste manually.** This page describes the structure that the **setup agent creates via the REST API** using your Notion Integration Token. You only need to understand it for debugging or customizing.
>
> V2.5 hardened this procedure against the errors that appeared in the first real runs. Following the steps below in order, setup runs **without error** — important since it ships to many users.

---

## Structure automatically created by the agent

Main page: `🚀 {brand_name} — News-to-Carrossel`

Inside:
- 2 inline databases
- 10 sub-pages

---

## Database 1: 🗞️ News Feed

> **Created FIRST** — the Carrosséis database has a relation that points to it.

| Property | Type | Configuration |
|---|---|---|
| Nº | Unique ID | **prefix `NF`** (prefix must be ≥ 2 characters — `N` alone is rejected by the API) |
| Title | Title | — |
| Source | Text | — |
| Link | URL | — |
| Summary | Text | 2–3 sentences |
| Relevance | Select | `1`, `2`, `3`, `4`, `5` |
| Collection date | Date | — |
| Time slot | Select | `Morning`, `Afternoon`, `End of afternoon` |
| Status | Select | `Pending`, `Pinned`, `Used`, `Discarded` |
| Images | Files & Media | Optional — R2 can attach the hero here |
| Original URLs | Text | Candidate image URL discovered by R1 (without downloading) |
| Has hero? | Checkbox | R1 marks the attempt; R2 confirms after local extraction |
| Visual hint | Text | Textual description of the ideal image — **R1 always fills this in**. It is what allows R2 to generate a coherent image when there is no real photo |
| Extraction level | Select | Filled in by R2 after Step 1.5: `og:image`, `twitter:image`, `json-ld`, `social-bot`, `google-cache`, `url-from-R1`, `ai-generated` |

> **V2.5 change:** R1 runs Remote (sandbox blocks direct HTTP) — it **does not download images**, it only discovers the candidate URL (best-effort) and writes the `Visual hint`. The one that actually extracts/downloads the image is R2 (Local, open network), in Step 1.5, only for the chosen news item. Details in `12-R1-News-Scout.md` and `13-R2-Routine-Local.md`.

**Views:** "Today" (Table, filter `Collection date = Today`, order `Relevance` desc — default), "Pinned" (Gallery, filter `Status = Pinned`), "Archive" (Table, order `Collection date` desc).

---

## Database 2: 🎨 Carrosséis

> **Created AFTER** the News Feed (the relation needs the target database to already exist).

| Property | Type | Configuration |
|---|---|---|
| Nº | Unique ID | **prefix `CR`** (≥ 2 characters) |
| Headline | Title | Main sentence chosen |
| Date | Date | — |
| Source news | Relation | → `🗞️ News Feed` |
| Hook pattern | Select | `Brazil/Context`, `Rupture`, `Generational`, `Investigating`, `Brand+Reveal`, `Two-Dots`, `Data`, `Contrast`, `Question` |
| Axis | Select | `Market`, `Cases`, `News`, `Culture`, `Product` |
| Caption | Text | Instagram-ready caption |
| Status | Select | `Draft`, `Approved`, `Posted`, `Discarded` |
| Performance | Select | `Excellent`, `Average`, `Poor` (filled in after posting) |
| Render attempts | Number | How many times it was re-rendered |
| Last render | Date | Timestamp of the last render |

> **About the slides (images):** R2 embeds the 9 images **in the body of the page** of each entry (image-type blocks). The "Slides" property (Files & Media) **does not reliably accept external URLs via MCP** — that's why R2 uses the body. The canonical backup of the slides is the local folder + Google Drive.

**Views:** "Gallery" (Gallery, order `Date` desc — default), "Calendar" (Calendar, date `Date`), "By status" (Board, group by `Status`).

---

## The 10 sub-pages created

In order (exact emojis — the agent creates them via API):

1. `🏷️ Brand Identity` — content of `01-Brand-Identity.md`, populated with the wizard variables. **The PNG logo is attached here by the user afterwards.**
2. `🔐 Configuration` — environment page (see section below). Created with the Higgsfield CLI checklist; the user does not paste a generation key.
3. `📋 News Sources` — content of `04-Fontes-noticias.md`, populated with the sources-wizard list
4. `📚 Editorial Manual` — content of `05-Manual-Editorial.md`, with `{brand_*}` interpolated
5. `🎯 Headline Engine` — content of `06-Engine-de-Headlines.md`
6. `🧭 Narrative Architecture` — content of `07-Arquitetura-Narrativa.md`
7. `🎨 Design System` — content of `08-Design-System.md`, with colors interpolated
8. `⚙️ Render Engine` — content of `09-Render-Engine.md` (no API key, just method)
9. `📐 Quality References` — content of `10-Referencias-de-Qualidade.md`
10. `🖼️ Visual References` — content of `11-Referencias-Visuais.md` (you attach images later)

---

## `🔐 Configuration` page — detailed

Private page that centralizes the environment checklist. R2 does not read an external generation key. It validates the local Higgsfield CLI login with `higgsfield account status`.

The agent creates the page with this content:

```
# 🔐 Configuration

⚠️ PRIVATE PAGE — do not share. Keep this Notion workspace
restricted to you. Whoever has access to this page has your API keys.

## Higgsfield CLI (required for R2)

Checklist:

​```
HIGGSFIELD_CLI=installed
HIGGSFIELD_LOGIN=done
HIGGSFIELD_IMAGE_MODEL=gpt_image_2
​```

Login is done locally with `higgsfield auth login`. We do not use Higgs MCP.

## Optional keys (R1 — news fetching)

​```
NEWSAPI_KEY=
MICROLINK_API_KEY=
​```

Leave empty if you don't have them. R1 works without them — it just skips those levels of the cascade.
```

**How R2 reads it:** uses this page as a human checklist, but the actual validation happens in the shell with `higgsfield account status`. If it fails, R2 stops with a clear error asking for installation or login.

> **Security note:** do not store a generation token in Notion. Higgsfield stays authenticated locally by the CLI.

---

## Error-proof creation procedure

> The agent follows **exactly this order**. Each step embeds the gotchas that caused errors in the first runs.

### Step 0 — Pre-check
- `GET /v1/users/me` with the token → confirms valid token (401 → wrong token)
- `GET /v1/pages/{id}` of the received page → confirms that the integration was shared (404/403 → user needs to do ••• → Add connections)
- **Only proceeds if both pass.** No point in creating anything with a token that has no access.

### Step 1 — Rename main page
- `PATCH /v1/pages/{id}` with the new title `🚀 {brand_name} — News-to-Carrossel`

### Step 2 — Create News Feed database
- `POST /v1/databases`, `parent.type = page_id`
- Property `Nº`: `type: unique_id` with `prefix: "NF"` — **1-character prefix is rejected**, use 2+
- Create with ALL properties at once
- **If it returns "Unexpected error" (known transient API error):**
  1. `sleep 2` and retry the call once
  2. If it persists: create the minimal database (just `title` + `Nº`), then add the other properties via `PATCH /v1/databases/{id}`
- Save `db_news_feed` (the returned ID)

### Step 3 — Create Carrosséis database
- Same as Step 2, `prefix: "CR"`
- The `Source news` (relation) property points to `db_news_feed` — that's why News Feed comes first
- Same retry/fallback strategy
- Save `db_carrosseis`

### Step 4 — Create the 10 sub-pages (empty)
- `POST /v1/pages` with `parent.page_id`, **one at a time, sequential, in foreground**
- ⚠️ **NEVER run creation in background + foreground at the same time, or in parallel** — that duplicates pages. Always serial, foreground, a single pass.
- Each page is created with only the title (emoji + name). Blocks come later.
- `sleep 0.4` between calls (rate limit 3 req/s)
- Save each `page_id` in a dictionary

### Step 5 — Parser smoke test
- Take ONE sub-page (`🏷️ Brand Identity`) and populate it with `md_to_notion.py`
- `GET /v1/blocks/{page_id}/children` → confirm that the blocks landed
- If it fails → debug the parser **before** populating the other 9 (don't propagate the error)

### Step 6 — Populate the 9 remaining sub-pages
- For each: `PATCH /v1/blocks/{page_id}/children` adding the blocks
- Blocks in batches of at most 100 per call
- Sequential, foreground, `sleep 0.4` between calls
- `🔐 Configuration` is populated with the placeholders template (no need for the .md parser)

### Step 7 — Connector verification (critical — see section below)

### Step 8 — Save `notion-ids.json`
- Writes all IDs to the working folder `~/{brand-slug}/notion-ids.json`
- Full schema in the "Setup output" section below

### Step 9 — Final checklist
- [ ] 2 databases created (News Feed with prefix NF, Carrosséis with prefix CR)
- [ ] Relation Carrosséis → News Feed working
- [ ] 10 sub-pages created and populated
- [ ] `🔐 Configuration` created with placeholders
- [ ] Views created in the databases
- [ ] Notion + Drive connectors tested and OK
- [ ] `notion-ids.json` saved in the working folder
- [ ] No duplicated pages

---

## Connector verification (Step 7)

> Runs **before** finalizing setup. Ensures that when R2 first runs, Notion and Drive are already working — avoids R2 silently failing on backup.

### Notion
OK by construction — the agent just created the entire structure via API. If you got here, Notion works.

### Google Drive
Real write test:
1. Via Google Drive MCP, create test folder `{brand_slug}/_setup_test/`
2. Upload a dummy file (`test.txt` with "ok")
3. Read it back to confirm
4. Delete the file and the test folder
5. **If it passes:** Drive confirmed. R2 will be able to back up the slides.
6. **If it fails:** the agent STOPS and instructs the user:
   ```
   ⚠️ Google Drive is not connected.
   Open Claude Desktop → Settings → Connectors → Google Drive → Connect.
   Authorize access. Then tell me "drive connected" so I can test again.
   ```
   It does not finalize setup until Drive passes — because R2 needs it to back up the carousels.

---

## Notion API endpoints used

| Action | Endpoint | Method |
|---|---|---|
| Validate token | `/v1/users/me` | GET |
| Validate access to page | `/v1/pages/{id}` | GET |
| Rename main page | `/v1/pages/{id}` | PATCH |
| Create inline database | `/v1/databases` (`parent.type=page_id`) | POST |
| Add property to database | `/v1/databases/{id}` | PATCH |
| Create sub-page | `/v1/pages` (`parent.page_id`) | POST |
| **Add blocks to a page** | `/v1/blocks/{id}/children` | **PATCH** (not POST) |
| Read blocks of a page | `/v1/blocks/{id}/children` | GET |

---

## Notion API gotchas (all already handled in the procedure)

- **`unique_id` prefix ≥ 2 characters** — 1-char prefix (`N`) returns 400. Use `NF`, `CR`.
- **`/blocks/{id}/children` is PATCH**, not POST. Getting the method wrong returns 405.
- **Never run creation in background + foreground** — duplicates pages. Always serial, foreground, single pass.
- **Empty page first, blocks later** — create the page with only the title, then `PATCH .../children`. More robust.
- **Transient "Unexpected error"** — the API sometimes fails for no reason. Retry 1x after `sleep 2`; if it persists, use the fallback (minimal database + PATCH of properties).
- **2000 char chunk** — `rich_text.content` has a 2000-char limit per segment. Larger strings are broken up by the parser.
- **Batch of 100 blocks** — `PATCH .../children` accepts at most 100 children per call. Parser paginates.
- **Code block languages** — Notion accepts only a specific set. Normalize `sh`→`bash`, `js`→`javascript`, `console`→`bash`.
- **Rate limit 3 req/s** — `sleep 0.4` between calls in loops.
- **Relation: target database before source** — News Feed created before Carrosséis.

---

## Markdown → Notion blocks parser

Used by the **CLI setup agent** (once only, when creating the structure). Lives in `~/{brand-slug}/md_to_notion.py` (generated by the agent). API:

```bash
python3 md_to_notion.py docs/05-Manual-Editorial.md {page_id}
```

Supports: H1-H3 headings, paragraphs, lists (bullet/numbered), code blocks (normalized language), tables, quotes, inline code, bold, links.

---

## Setup output — `notion-ids.json`

At the end, the agent saves `~/{brand-slug}/notion-ids.json`. **R2 reads this file** (does not use env vars):

```json
{
  "page_principal": "...",
  "page_brand_identity": "...",
  "page_config": "...",
  "page_fontes": "...",
  "page_manual": "...",
  "page_headlines": "...",
  "page_arquitetura": "...",
  "page_design_system": "...",
  "page_render_engine": "...",
  "page_refs_qualidade": "...",
  "page_refs_visuais": "...",
  "db_news_feed": "...",
  "db_carrosseis": "..."
}
```

---

## Re-running setup without destroying

```bash
cd ~/{brand-slug}
claude
> rebuild brand
```

The agent reads `.brand.json`, reapplies interpolation to the `.md` files, and does `PATCH /v1/blocks/{id}/children` replacing the blocks of each sub-page. **It does not recreate the structure, does not touch the databases, does not duplicate.** Useful when you edited an `.md` locally and want to sync with Notion.
