# 03 — Notion Template (V2.0 — via Claude Desktop connectors)

> **Don't paste manually.** This page describes the **desired final structure** in Notion. The Maestro creates everything automatically via **native Claude Desktop connectors** (Settings → Connectors). You read this file only to debug or customize.

## Principle: everything via connectors, never via direct API

All Creative DNA integration follows a single rule: **native Claude Desktop connectors**.

| Tool | How it integrates | NOT used |
|---|---|---|
| Notion | Connector → tools `notion-search`, `notion-create-pages`, `notion-update-page`, `notion-fetch` | Integration Token, REST API, `curl https://api.notion.com/...` |
| Google Drive | Connector → tools `gdrive-*` | Manual OAuth, Service Account, `gcloud` |
| Slack / Linear / GitHub / Gmail (if relevant) | Connector → native tools | Webhooks, App tokens, API keys |

**Reason:** ease for the person. Connector is activated in Settings → Connectors → [name] → Connect → authorize (3 clicks, 30 seconds). No need to create integrations, generate tokens, share pages, configure webhooks. The person sees no credentials.

**Change V1 → V2 (May/2026):** the old version of this document described use of Notion REST API + Integration Token. That model has been discontinued — don't use it anymore. V2 uses MCP connector, full stop.

---

## Desired structure in Notion

The DNA system creates more things than the Carrossel one: **4 databases + 14 sub-pages + 1 main page**. More depth means more blocks, more relations, more care with idempotency.

---

## Structure created automatically by the agent

Main page: `🧬 {brand_name} — Creative DNA`

Inside:
- 4 inline databases
- 14 sub-pages

---

## Database 1: 🗂️ Touchpoints

> **Created FIRST** — other databases have relations pointing to it.

Each brand touchpoint is an entry: Instagram post, story, reel, email, landing, ad, deck, podcast, event, packaging, in-store, etc. Works as a map of "where the brand appears".

| Property | Type | Configuration |
|---|---|---|
| Nº | Unique ID | **prefix `TP`** |
| Name | Title | E.g.: "Instagram — carousel post", "Email — welcome", "Landing — product X" |
| Category | Select | `Social`, `Email`, `Web`, `Ad`, `Deck`, `Physical`, `Audio`, `Video`, `Other` |
| Channel | Select | `Instagram`, `LinkedIn`, `YouTube`, `Transactional email`, `Marketing email`, `Site`, `Landing`, `Meta Ads`, `Google Ads`, `Physical`, `Other` |
| Frequency | Select | `Daily`, `Weekly`, `Biweekly`, `Monthly`, `Quarterly`, `On demand` |
| Predominant tone | Select | `Editorial`, `Conversational`, `Commercial`, `Crisis`, `Institutional` |
| Owner | People | Who's responsible for this touchpoint |
| Technical specs | Text | Dimensions, formats, weights, restrictions |
| Canonical template | Files & Media | PNG/PDF of the approved template (if any) |
| Last DNA review | Date | When this touchpoint was audited against the DNA |

**Views:** "By category" (Board, group by Category — default), "By channel" (Table, order by Frequency), "Without recent review" (Table, filter Last DNA review < 90 days ago).

---

## Database 2: 📥 Briefs

> **Created AFTER** Touchpoints (relation points to it).

Each creative brief sent to R2 is an entry. Permanent history of "what was asked", for reuse and calibration.

| Property | Type | Configuration |
|---|---|---|
| Nº | Unique ID | **prefix `BR`** |
| Title | Title | E.g.: "Welcome email v2", "Carousel about launch Y" |
| Touchpoint | Relation | → `🗂️ Touchpoints` |
| Original brief | Text | What the user requested, in free text |
| Processed brief | Text | Brief enriched by R2 with DNA applied |
| Status | Select | `In production`, `Delivered`, `Approved`, `Published`, `Archived` |
| Output | Relation | → `🎯 Assets` (generated output) |
| Compliance score | Number | 0-10 — average of the output audit |
| Requester | People | Who asked |
| Deadline | Date | Deadline |
| Notes | Text | Adjustments, context, external links |

**Views:** "In production" (Board, group by Status — default), "By touchpoint" (Table), "History" (Table, order by Created Time desc).

---

## Database 3: 🎯 Assets

> **Created AFTER** Briefs.

Canonical library of approved outputs — copy, images, decks, videos. Each approved asset becomes a reference for future agents (feeds `📚 Reference Library`).

| Property | Type | Configuration |
|---|---|---|
| Nº | Unique ID | **prefix `AS`** |
| Name | Title | E.g.: "Welcome email v3 — approved" |
| Type | Select | `Copy`, `Image`, `Video`, `Deck`, `Carousel`, `Email`, `Landing`, `Other` |
| Origin brief | Relation | → `📥 Briefs` |
| Touchpoint | Relation | → `🗂️ Touchpoints` |
| Status | Select | `Draft`, `Approved`, `Published`, `Archived`, `Discontinued` |
| Files | Files & Media | PNGs, PDFs, MP4s |
| Public URL | URL | Link to the published asset (post, landing, etc.) |
| Performance | Select | `Excellent`, `Medium`, `Poor`, `No data` |
| Lessons | Text | What you learned from this asset (feeds `📚 Reference Library`) |
| Can reuse? | Checkbox | If yes, becomes canonical reference for future briefs |

**Views:** "Gallery" (Gallery, order by Created Time desc — default), "Reusable approved" (Gallery, filter Can reuse = true), "By type" (Board).

---

## Database 4: ✅ Compliance

> **Created last.**

Audit history. Every time R2 audits an asset (own or external) against the DNA, it records here. Creates history of adherence to the DNA over time.

| Property | Type | Configuration |
|---|---|---|
| Nº | Unique ID | **prefix `CP`** |
| Audited asset | Title | Name or descriptor of the asset |
| Asset type | Select | `Copy`, `Image`, `Video`, `Deck`, `Carousel`, `Email`, `Landing`, `Other` |
| Origin | Select | `Internal (R2 generated)`, `Internal (human made)`, `External (competitor)`, `External (inspirational reference)` |
| Related asset | Relation | → `🎯 Assets` (if own) |
| Voice score | Number | 0-10 |
| Visual score | Number | 0-10 |
| Persona score | Number | 0-10 |
| Anti-patterns score | Number | 0-10 |
| Total score | Formula | (voice + visual + persona + anti-patterns) / 4 |
| Diagnosis | Text | What's aligned, what's not |
| Suggestion | Text | How to improve |
| Image | Files & Media | Screenshot of the audited asset |
| Audit date | Date | — |

**Views:** "History" (Table, order by Audit date desc — default), "Low score" (Table, filter Total score < 7), "By type" (Board).

---

## The 14 sub-pages created

In order (exact emojis — agent creates via API):

1. `🧬 DNA Master` — content from `01-DNA-Master.md`, populated with the executive synthesis of the wizard. **The PNG logo is attached here by the user afterwards.**
2. `🔐 Configuração` — environment page. Created with Higgsfield CLI checklist; user does not paste a generation key.
3. `🔍 Discovery Protocol` — content from `04-Discovery-Protocol.md` (the 52 questions for reuse in future reviews)
4. `🎯 Brand Strategy` — content from `05-Brand-Strategy.md`, populated with answers from Phase 2
5. `👥 Audience DNA` — content from `06-Audience-DNA.md`, populated with answers from Phase 3
6. `🗣️ Voice & Tone` — content from `07-Voice-and-Tone.md`, populated with answers from Phase 4
7. `🎨 Visual System` — content from `08-Visual-System.md`, populated with answers from Phase 5
8. `📸 Photography Direction` — content from `09-Photography-Direction.md`, populated with chosen lighting setups
9. `🖼️ Image Generation Engine` — content from `10-Image-Generation-Engine.md`
10. `🤝 Brand Behavior` — content from `11-Brand-Behavior.md`, populated with answers from Phase 6
11. `🚫 Anti-Patterns` — content from `12-Anti-Patterns.md`, populated with seeds from Phase 7
12. `📚 Reference Library` — content from `13-Reference-Library.md` (you attach images later; R1 feeds automatically)
13. `📋 Pilares & Tabus` — page derived from Phase 7 answers (content pillars and taboo themes, expanded with scope)
14. `📜 Manifesto` — optional, derived from Phase 2 answers — public text of 200-400 words that synthesizes purpose + positioning + promise, formatted for eventual publication on the site/about

---

## Page `🔐 Configuração` — detailed

Private page that centralizes environment and connectors. Same philosophy as the Carrossel: visual generation uses local Higgsfield CLI, not API key in Notion. If you've already installed Carrossel, **the two Configuração pages can be unified**.

The agent creates with this content:

```
# 🔐 Configuração

⚠️ PRIVATE PAGE — don't share. Keep this Notion workspace
restricted to you. Whoever has access to this page has your API keys.

## Higgsfield CLI (mandatory for R2 when generating images)

Checklist:

​```
HIGGSFIELD_CLI=installed
HIGGSFIELD_LOGIN=done
HIGGSFIELD_IMAGE_MODEL=nano_banana_2
​```

Login is local: `higgsfield auth login`.

## ElevenLabs key (optional — for voice generation)

​```
ELEVENLABS_API_KEY=
​```

Leave empty if you don't use voice.

## R1 settings (Brand Scout)

​```
SCOUT_INSPIRATION_SOURCES=pinterest,arena,behance,dribbble
SCOUT_COMPETITOR_HANDLES=
SCOUT_BRAND_MENTIONS=true
​```

List of sources R1 monitors for visual inspiration and brand mentions.
```

**How agents read:** R2 of the DNA and R2 of the Carrossel validate the environment in the shell with `higgsfield account status`. If it fails, they stop with clear error asking for installation or login.

> **Security note:** do not store visual generation keys in Notion. Higgsfield stays authenticated locally via CLI.

---

## Creation procedure via Notion MCP

> The Maestro follows this order using **MCP tools** (`notion-search`, `notion-create-pages`, `notion-update-page`, `notion-fetch`). The gotchas listed still apply because the backend is the same Notion — but the Maestro doesn't need to deal with tokens, headers, manual retries or rate limits (the connector handles it).

### Step 0 — Connector verification
- Tries a simple call (`notion-search` with empty query) to confirm the connector is active
- If the tool doesn't respond → instructs the person to activate Settings → Connectors → Notion → Connect (message in `CLAUDE.md` Step 1.8)
- **Only proceeds when the connector is functional.**

### Step 1 — Locate workspace and create main page
- `notion-search` to see accessible workspaces
- `notion-create-pages` creates page `🧬 {brand_name} — Creative DNA` in the appropriate workspace
- Saves the returned `page_id`

### Step 2 — Create 4 inline databases (in the right order, because of relations)

Order matters — Touchpoints first because other databases have relations pointing to it.

1. **Touchpoints** (`prefix: TP`) — created first
2. **Briefs** (`prefix: BR`) — relation `Touchpoint` → Touchpoints
3. **Assets** (`prefix: AS`) — relations `Origin brief` → Briefs, `Touchpoint` → Touchpoints
4. **Compliance** (`prefix: CP`) — relation `Related asset` → Assets, formula `Total score = (voice + visual + persona + anti-patterns) / 4`

Use `notion-create-pages` with database type. Properties go in the call payload — the MCP accepts creating a complete database in one go in most cases.

**Maintained gotcha:** `unique_id` needs prefix with 2+ characters. `T` fails; `TP` passes.

### Step 3 — Create 14 sub-pages (sequential)
- `notion-create-pages` one at a time, foreground
- ⚠️ **Never in parallel** — duplicates pages (Notion gotcha, not MCP)
- Created with just title first; blocks come in Step 4

List of 14 pages (in order):
1. `🧬 DNA Master`
2. `🔐 Configuração`
3. `🔍 Discovery Protocol`
4. `🎯 Brand Strategy`
5. `👥 Audience DNA`
6. `🗣️ Voice & Tone`
7. `🎨 Visual System`
8. `📸 Photography Direction`
9. `🖼️ Image Generation Engine`
10. `🤝 Brand Behavior`
11. `🚫 Anti-Patterns`
12. `📚 Reference Library`
13. `📋 Pilares & Tabus`
14. `📜 Manifesto`

### Step 4 — Populate the 14 sub-pages
- `notion-update-page` for each, in sequence
- Content comes from the corresponding `.md` (see map in `CLAUDE.md` → "Internal map of files")
- `{brand_*}` variables interpolated from the briefing
- Strategic analysis (from Maestro's Step 1.7) is injected as expanded content into the relevant pages — not just compilation, **insight that emerged from the briefing**

**Gotchas that still matter:**
- Code block: languages outside Notion's allowlist (e.g.: `sh`, `console`) need to be normalized to `bash`/`bash`
- Long strings: `rich_text.content` has a 2000 char limit per segment — break into multiple blocks
- Block batches: maximum 100 children per update — paginate if necessary

### Step 9 — Connector verification

> Runs **before** finalizing the setup. Same logic as the Carrossel.

**Notion:** OK by construction (just created everything via API).

**Google Drive:** Real write test:
1. Via MCP Google Drive, creates test folder `{brand_slug}/_setup_test/`
2. Uploads dummy file `test.txt`
3. Reads it back to confirm
4. Deletes test file and folder
5. **If passes:** Drive confirmed. R2 can back up outputs.
6. **If fails:** the agent STOPS and instructs:
   ```
   ⚠️ Google Drive is not connected.
   Open Claude Desktop → Settings → Connectors → Google Drive → Connect.
   Authorize access. Then tell me "drive connected" so I can test again.
   ```

### Step 10 — Save `notion-ids.json`
- Saves all IDs in the working folder `~/{brand-slug}/notion-ids.json`
- Complete schema in the "Setup output" section below

### Step 11 — Save `.dna.json`
- Complete snapshot of the DNA in local JSON (quick cache for subprocess)
- Schema in the `🧬 DNA Master` section (`01-DNA-Master.md`)

### Step 12 — Final checklist
- [ ] 4 databases created (Touchpoints `TP`, Briefs `BR`, Assets `AS`, Compliance `CP`)
- [ ] Relations between databases working
- [ ] 14 sub-pages created and populated
- [ ] `🔐 Configuração` created with placeholders
- [ ] Views created in the 4 databases
- [ ] Notion + Drive connectors tested and OK
- [ ] `notion-ids.json` + `.brand.json` + `.dna.json` saved in the working folder
- [ ] No duplicated page
- [ ] At least 3 seed-entries in the Touchpoints database (Instagram post, marketing email, landing — to make usage clear)

---

## Notion MCP tools used

| Action | MCP Tool |
|---|---|
| Verify connector + list workspaces | `notion-search` |
| Create main page / sub-page | `notion-create-pages` |
| Create inline database | `notion-create-pages` (with database type) |
| Populate sub-page with blocks | `notion-update-page` |
| Read content of existing page | `notion-fetch` |
| Comment (record evolve diff) | `notion-create-comment` |
| Read comments | `notion-get-comments` |

> **There are no more "REST endpoints".** The Maestro calls the tools like any other Claude Code function. The MCP handles auth, retries, rate limit.

---

## Gotchas that still apply (even with MCP)

Some gotchas are **from Notion itself** (not the transport layer) — they still apply:

- **`unique_id` prefix ≥ 2 characters** — use `TP`, `BR`, `AS`, `CP`. 1-char prefix is rejected by Notion.
- **Never create pages in parallel** — duplicates entries. Always serial, foreground, single pass.
- **Empty page first, blocks later** — more robust. Creates title; populates content in a second step.
- **Long strings in rich_text** — limit of 2000 chars per segment. Break into multiple blocks or multiple rich_text segments.
- **Code block languages** — Notion accepts only a specific set. Normalize: `sh`→`bash`, `js`→`javascript`, `console`→`bash`.
- **Relation: destination database before origin** — Touchpoints before Briefs/Assets/Compliance.
- **Formula property** — uses Notion expression (not JS): `(prop("Voice score") + prop("Visual score") + prop("Persona score") + prop("Anti-patterns score")) / 4`.

### Gotchas that DISAPPEARED with MCP (no need to deal with anymore)

- ❌ Token validation (`/v1/users/me`) — MCP handles auth
- ❌ Manual page sharing ("Add connections") — connector gives access to everything in the workspace
- ❌ Manual rate limit (`sleep 0.4`) — MCP returns error, you retry
- ❌ Transient "Unexpected error" retry — MCP already has internal retry
- ❌ Difference between POST `/v1/pages` and PATCH `/v1/blocks/{id}/children` — you use nominal tools
- ❌ Own markdown parser (`md_to_notion.py`) — you generate Notion blocks directly via `notion-update-page`

---

## Setup output — `notion-ids.json`

At the end, the agent saves `~/{brand-slug}/notion-ids.json`. **The R2s read this file** (they don't use env vars):

```json
{
  "page_principal": "...",
  "page_dna_master": "...",
  "page_config": "...",
  "page_discovery": "...",
  "page_strategy": "...",
  "page_audience": "...",
  "page_voice": "...",
  "page_visual": "...",
  "page_photography": "...",
  "page_image_engine": "...",
  "page_behavior": "...",
  "page_anti_patterns": "...",
  "page_reference_library": "...",
  "page_pillars_taboos": "...",
  "page_manifesto": "...",
  "db_touchpoints": "...",
  "db_briefs": "...",
  "db_assets": "...",
  "db_compliance": "..."
}
```

If the brand also has Carrossel installed, the `notion-ids.json` is **merged** — it also contains `page_brand_identity`, `db_news_feed`, `db_carrosseis`, etc., from the Carrossel. R2 of the Carrossel starts reading `page_dna_master` before reading `page_brand_identity` (DNA takes precedence).

---

## Re-run setup without destroying

```bash
cd ~/{brand-slug}
claude
> rebuild DNA
```

The agent reads `.brand.json` + `.dna.json`, reapplies interpolation in the `.md` files, and does `PATCH /v1/blocks/{id}/children` replacing the blocks of each sub-page. **Does not recreate the structure, does not touch the databases, does not duplicate.** Useful when you've edited a `.md` locally, or when the Notion content went out of sync with the local JSON.

```bash
> rebuild DNA --pages=voice,visual
```

Selective variation — only re-populates specific pages.

---

## Quarterly snapshots

R2 automatically creates a snapshot of the entire DNA every 90 days, saved in Drive at `{brand_slug}/DNA-Snapshots/{YYYY-MM-DD}/`:

- `dna-master.pdf` — export of the `🧬 DNA Master` page
- `dna-full.zip` — export of all 14 pages + 4 databases
- `dna.json` — structured version
- `changelog.md` — diff vs. previous snapshot

Serves as history ("how was our DNA in Q1 vs Q3") and as backup. To run manually: command `> snapshot DNA` in the CLI agent.
