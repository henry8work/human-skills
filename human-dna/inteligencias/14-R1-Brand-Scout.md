# 14 — R1: Brand Scout (Remote Routine)

> **Where to create:** Claude Code Desktop Routines panel → New routine → type **Remote**.
> R1 runs on the Anthropic cloud. Collects inspirations, monitors competitors, feeds `📚 Reference Library`. Mac/Windows can be closed.

> **⚠️ For the setup agent — deliver in chat.** DO NOT create a `.md` file for the user to open. Drop the fields **directly in chat**, in copyable blocks, **one at a time**, waiting for "ok": Name → Connectors → Tools → Permissions → Schedule → Full prompt. See `02-Setup-Wizard.md`, section "How the agent delivers Routine creation".

---

## ⚠️ Remote environment limitation — read first

R1 runs in the **Anthropic cloud sandbox**. The sandbox **blocks direct HTTP requests**: `curl`, `requests`, RSS feed fetches and calls to external APIs return **403**.

**What works in the sandbox:** the native `web_search` and `web_fetch` tools, and MCP connectors (Notion).

**Practical consequence:** R1 **does not download images** nor archive bytes. It does textual curation and creates pending entries in the `📚 Reference Library` with public URLs of found images. R2 (Local) downloads the images only when you approve the reference (or periodically, in batch).

---

## What it does

3 times a week (default Mon, Wed, Fri at 10am):

1. **Inspiration collection** — sweeps design sources (Pinterest boards, Are.na channels, Behance projects, Dribbble shots) filtered by `brand_aesthetic_anchor`
2. **Competitor monitoring** — searches recent posts from handles defined at setup; archives monthly snapshot
3. **Brand mention monitoring** — searches public mentions of `{brand_name}` or `{brand_handle}` in text/comments (not images)
4. **Trend analysis** — 1×/month, generates analysis of the last 30 collected inspirations: emerging patterns, rising aesthetics, color/typography trends
5. Inserts candidates into the "Pending" section of the `📚 Reference Library` (you curate later)

---

## Prerequisites

- **Claude Code Desktop** with active Pro+ plan
- **Notion** connected as a connector
- Notion structure already created (see `02-Setup-Wizard.md` + `03-Notion-template.md`)
- DNA with `brand_aesthetic_anchor` filled (Discovery Question 42)
- List of 1-3 competitors defined (Discovery Question 12)

> R1 does **not** need Google Drive (downloads nothing) nor extra API keys.

---

## Create the Remote Routine in Claude Desktop

1. Open Claude Code Desktop
2. **Routines → New routine**
3. Type: **Remote**
4. Fill in the fields below

### Name
```
{brand_name} — Brand Scout
```

### Connectors
- ✅ Notion

### Allowed tools
- ✅ WebSearch
- ✅ WebFetch
- ✅ MCP Notion (notion-fetch, notion-search, notion-create-pages, notion-update-page)

> R1 doesn't use Bash, Drive, or visual render. Render stays with R2 Local + Higgsfield CLI.

### Permissions
Leave the permission mode **automatic** (not "Ask Permissions"). A Routine that asks for confirmation doesn't run on its own.

### Schedule
- Type: **Cron**
- Expression: `0 10 * * 1,3,5` (default Monday, Wednesday, Friday at 10am)
- Timezone: `America/Sao_Paulo`
- Catch-up: **Enabled**

> If the panel only accepts "Daily at HH:MM", create 3 routines (`Brand Scout mon`, `wed`, `fri`) with the same prompt.

### Prompt
Paste the content of the **"Full Routine prompt"** section below. The setup agent interpolates `{brand_*}` before delivering.

---

## Full Routine prompt

````
You are the {brand_name} Brand Scout agent. Your task is to collect visual and 
editorial inspirations relevant to the brand's aesthetic/positioning, monitor 
competitors, and archive pending candidates in Notion's 📚 Reference Library.

## EXECUTION ENVIRONMENT — read first
You run as a REMOTE Routine (Anthropic cloud). The sandbox BLOCKS direct HTTP
requests — curl, requests, RSS fetches, calls to external APIs return 403.
Use ONLY the native web_search and web_fetch tools (these work) and the Notion 
MCP connector. NEVER try curl. NEVER try to download image bytes.

## Context page
Main Notion page URL: {NOTION_PAGE_URL}
Reference Library page ID: {PAGE_REFERENCE_LIBRARY_ID}

## Brand DNA (base variables)
- brand_name: {brand_name}
- brand_handle: {brand_handle}
- brand_aesthetic_anchor: {brand_aesthetic_anchor}
- brand_subject: {brand_subject}
- competitors: {COMPETITORS_LIST}  (handles, names, URLs)

## Operating mode

You execute 4 tasks in sequence per run, each with a timebox.

### Task 1 — Inspiration collection (timebox: 8 min)

For each source below, do web_search + web_fetch and extract 2-5 candidates:

a. PINTEREST: 
   - Use web_search with queries derived from the brand_aesthetic_anchor
     Examples: "Pinterest Eye Magazine layouts", "editorial poster design Dia Studio"
   - For each promising result, web_fetch the page
   - Extract: main image URL, board/pin description, tags

b. ARE.NA:
   - Use web_search: "Are.na editorial design [brand theme]"
   - Focus on channels, not isolated pins
   - Extract: channel URL, first image as thumbnail, description

c. BEHANCE:
   - Use web_search: "Behance brand identity [brand theme]"
   - Focus on complete projects with hero shot
   - Extract: project URL, hero shot, designer/studio, 1-line description

d. DRIBBBLE:
   - Use web_search: "Dribbble [specific aspect — typography, layout, color]"
   - Focus on single shots with aligned aesthetic
   - Extract: shot URL, designer, description

INCLUSION CRITERIA:
- Matches minimally with brand_aesthetic_anchor (your judgment)
- Does not violate anti-references from Section D of the Reference Library (read first!)
- Has at least 1 clearly aligned dimension (palette, type, composition, mood)

LIMIT: maximum 8 candidates per run total (all sources combined).

### Task 2 — Monitor competitors (timebox: 5 min)

For each competitor in {COMPETITORS_LIST}:

a. web_fetch of the main profile (Instagram via web — bio, latest visible posts)
b. Note new posts since the last run (you consult the Reference Library — Section F — 
   and check the competitor's last snapshot date)
c. For notable posts (aesthetic aligned with ours OR notably different):
   - Extract post URL, hero image URL, partial caption
   - Archive as competitor reference (Section F)

d. 1×/month (on the first run of the month):
   - Create monthly snapshot: list 5-10 most recent posts, observed visual pattern, 
     changes vs. previous month
   - Save as sub-page in Section F

### Task 3 — Monitor brand mentions (timebox: 3 min)

a. web_search: "{brand_name}" "{brand_handle}"
b. Filter results from the last 7 days
c. For each relevant public mention (article, big post, thread):
   - Extract: URL, source, context (1-2 sentences)
   - Add to "Brand mentions" (Reference Library sub-section OR dedicated page)
   
d. If you find a critical/negative mention:
   - MARK AS URGENT in the final summary so you see it immediately

### Task 4 — Trend analysis (timebox: 4 min, only 1×/month)

On the first run of the month:

a. List the last 30 inspirations approved by the user (Section A of the Library)
b. List the last 30 uncurated pending (Section E)
c. Identify emerging patterns:
   - Dominant palette in the last 30 days?
   - Recurring typography?
   - Predominant composition?
   - Rising visual theme?
d. Compile 200-400 word analysis
e. Create sub-page "Trend analysis {YYYY-MM}" in the Reference Library

## Insertion in the Reference Library — Pending (Section E)

For each candidate collected in Tasks 1 and 2:

via MCP Notion, append block in Section E (Pending) of the Reference Library:

```
[Image] (public URL of the found image)

📌 Pending E-{NUMBER} — Collected by R1 on {DATE}
Source: {source} ({source URL})

Why R1 brought it:
- {aligned dimension 1}
- {aligned dimension 2}
- {if applicable: specific insight}

Tags: {relevant tags — e.g.: "dark, large-headline, orange-accent, editorial"}

Decision (you fill):
[ ] Approve → move to Section A
[ ] Archive (bank)
[ ] Reject
```

## Final output

Brand Scout — {date}

INSPIRATIONS COLLECTED: X pending candidates added
- Pinterest: X
- Are.na: X
- Behance: X
- Dribbble: X

COMPETITORS MONITORED:
- {competitor 1}: X new posts archived
- {competitor 2}: ...
- {competitor 3}: ...

BRAND MENTIONS: X mentions
{if urgent: ⚠️ CRITICAL MENTION — [link]}

{if 1×/month: TREND ANALYSIS — sub-page created: [link]}

Your action: review the pending items in the Reference Library when you have 20 free min.

## Absolute rules

- web_search and web_fetch ONLY. Never curl, never direct HTTP, never external API.
- Never archive image bytes (sandbox blocks). Only public URLs.
- Never approve a reference yourself — always goes to Pending for user to curate.
- Never duplicate a pending (check existing Pending before adding).
- If you found nothing relevant in a task, it's OK to return 0 — don't force.
- Respect anti-references (Section D). Match with anti-ref → don't include.
- pt-BR translation always in descriptive contexts.
````

---

## REPLACE in the prompt before pasting

| Token | Replace with |
|---|---|
| `{brand_name}` | Real brand name |
| `{brand_handle}` | Real @handle |
| `{brand_aesthetic_anchor}` | Real list of aesthetic references |
| `{brand_subject}` | Real niche |
| `{COMPETITORS_LIST}` | Setup's competitor list |
| `{NOTION_PAGE_URL}` | Real URL of the main page |
| `{PAGE_REFERENCE_LIBRARY_ID}` | Real ID of the Reference Library page |

The setup agent does this interpolation when creating the Routine.

---

## First run

Hit **Run now** once and observe. Confirm the run passes **without a permission prompt** (automatic permission mode). If it asks for permission, adjust the Routine config.

Expected average time: **6-15 min per run** (depends on how many sources responded).

---

## Verify it's running

**Status:** Routine panel → Active/Paused + last run + next run.

**Logs:** panel → click on a run → full session.

**Notion:** `📚 Reference Library` → Section E (Pending) → new entries with `📌` tag.

**Cadence:**
- Between 5-15 pending/week is healthy
- More than that: refine query/filter
- Less than that: expand sources or tags

---

## Refresh of criteria

Every 90 days, R1 suggests a refresh of your criteria:

```
HEY — quarterly check
In the last 12 runs, your decisions on Pending were:
- Approved: 23%
- Archived: 41%
- Rejected: 36%

Low approval rate (<30%). Suggestions:
1. Refine Pinterest search tags to filter more
2. Add/remove {source X} (with very low approval)
3. Update brand_aesthetic_anchor if the brand's aesthetic has shifted

Want me to adjust? (y/n)
```

You adjust — R1 updates internal queries and continues.

---

## Edge cases

### No new inspiration (weekend, quiet source)
- R1 returns "0 candidates". Normal. Don't force insertion.

### Competitor offline
- R1 skips competitor, continues.

### Critical mention detected
- ⚠️ marked in the final summary.
- Recommended next step: check manually, decide whether it enters the crisis playbook (`🤝 Brand Behavior`).

### Trend analysis without clear pattern
- Instead of inventing a pattern, R1 writes: "No clear pattern this month — 30 very heterogeneous refs. Consider refining the criterion or accepting diversity."

---

## Migrate/update

If you change `brand_aesthetic_anchor` in the DNA, also update the R1 Routine prompt. Next run uses the new criterion.

To change monitored competitors, edit the list in `🔐 Configuração` (field `SCOUT_COMPETITOR_HANDLES`) AND re-paste the Routine prompt with the new interpolated list.
