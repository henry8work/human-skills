# 12 — R1: News Scout (Remote Routine)

> **Where to create:** Claude Code Desktop Routines panel → New routine → type **Remote**.
> R1 runs in the Anthropic cloud. Collects news and writes to Notion. Mac/Windows can be closed all day.

> **⚠️ For the setup agent — deliver in chat.** DO NOT create an `.md` file for the user to open. Drop **all R1 fields at once, in a single message**, each in its own copyable block: Name → Connectors → Tools → Permissions → Schedule → Full prompt. Don't drip-feed one field at a time waiting for "ok". Guide the entire R1 first; only after the user confirms it was created and tested, move on to R2. See `02-Setup-Wizard.md`, section "How the agent delivers the Routine creation".

---

## ⚠️ Remote environment limitation — read first

R1 runs in the **Anthropic cloud sandbox**. The sandbox **blocks direct HTTP requests**: `curl`, `requests`, RSS feed fetches and calls to external APIs (NewsAPI, Microlink) return **403**.

**What works in the sandbox:** the native `web_search` and `web_fetch` tools, and the MCP connectors (Notion).

**Practical consequence:** R1 **does not download images**. Downloading image bytes and uploading to Drive is impossible in the sandbox. Therefore:
- R1 only handles **text** — finds news, writes title/summary/relevance/link to Notion
- R1 does **best-effort** to discover the URL of the hero image (without downloading) and generates a textual **Visual hint**
- The actual image extraction/download is the responsibility of **R2**, which runs **Local** with open network (see `13-R2-Routine-Local.md`, Step 1.5)

This solves the "every news item with Has hero? = false" problem — R1 never again tries what the sandbox doesn't permit.

---

## What it does

3 times a day (default 9am / 1pm / 5pm):

1. Reads the `📋 News Sources` page in Notion (sources to monitor, topics, relevance criterion)
2. Uses `web_search` + `web_fetch` to find recent news of `{brand_subject}`
3. Deduplicates against what's already in the News Feed
4. Best-effort: discovers the hero image URL (without downloading) + writes a Visual hint
5. Inserts up to 8 news items into the `🗞️ News Feed` database

---

## Prerequisites

- **Claude Code Desktop** with active Pro+ plan
- **Notion** connected as a connector
- Notion structure already created (cf. `02-Setup-Wizard.md` + `03-Notion-template.md`)

> R1 does **not** need Google Drive (it doesn't upload images) nor API keys (NewsAPI/Microlink don't work in the sandbox).

---

## Create the Remote Routine in Claude Desktop

1. Open Claude Code Desktop
2. **Routines → New routine**
3. Type: **Remote**
4. Fill in the fields below

### Name
```
{brand_name} — News Scout
```

### Connectors
- ✅ Notion

### Allowed tools
- ✅ WebSearch
- ✅ WebFetch
- ✅ MCP Notion (notion-fetch, notion-search, notion-create-pages, notion-update-page)

> R1 doesn't use Bash, Drive, or visual render. Render stays with R2 Local + Higgsfield CLI.

### Permissions
Leave the permission mode **automatic** (not "Ask Permissions"). A Routine that asks for confirmation on every action doesn't run on its own. See `13-R2-Routine-Local.md`, section "Permissions" — same applies to R1.

### Schedule
- Type: **Cron**
- Expression: `0 {cron_r1_hours} * * *` (default `0 9,13,17 * * *`)
- Timezone: `America/Sao_Paulo`
- Catch-up: **Enabled**

> If the panel only accepts "Daily at HH:MM", create 3 routines (`News Scout 9am`, `1pm`, `5pm`) with the same prompt.

### Prompt
Paste the content of the **"Full Routine prompt"** section below. The setup agent interpolates `{brand_*}` before delivery.

---

## Full Routine prompt

````
You are the News Scout agent for {brand_name}. Your task is to collect relevant
news about {brand_subject} and insert it into the "🗞️ News Feed" Notion database.

## EXECUTION ENVIRONMENT — read first
You run as a REMOTE Routine (Anthropic cloud). The sandbox BLOCKS direct
HTTP requests — curl, requests, RSS fetches, calls to external APIs return
403. Use ONLY the native web_search and web_fetch tools (these work)
and the Notion MCP connector. NEVER try curl. NEVER try to download image bytes.
NEVER call NewsAPI, Microlink or any external HTTP API.

## Context page
Main page URL in Notion: {NOTION_PAGE_URL}

## Steps

1. Time in São Paulo: 6am-12pm = "Morning", 12pm-4pm = "Afternoon",
   4pm-8pm = "End of afternoon".

2. Read the "📋 News Sources" page in Notion: list of sources to
   monitor, topics that matter, topics to ignore, 1-5 relevance criterion.

3. For each source, use web_search to find recent news (~last 12h)
   about {brand_subject}. Use web_fetch to open the candidates and read the content.
   For each valid news item, extract:
   - Title, source, news URL
   - 2-3 sentence summary in pt-BR (translate if it's in English, keep technical
     terms like "prompt", "fine-tuning", "agentic")
   - Relevance 1-5 per the Sources page criterion
   - Discard if it falls into "Topics to IGNORE"

4. Deduplicate against the News Feed:
   - Exact URL already exists → discard
   - Title ≥80% similar to something from today → discard
   - Topic repeated in the last 3 days with no new angle → discard

5. NEWS IMAGE — best-effort, NO download:
   The sandbox prevents downloading images. You DO NOT download or store images.
   You only try to DISCOVER the URL of the hero image and describe it:

   a. When using web_fetch on the news page, observe whether the returned
      content exposes a main image URL (the article cover image, og:image,
      featured image). If a plausible URL appears, save it — it goes into the
      "Original URLs" property.

   b. ALWAYS write a "Visual hint": 1-2 sentences in pt-BR describing
      what image would well illustrate the news. Be concrete and visual.
      Examples:
      - "Screenshot of the OpenAI app showing the video editing
        timeline, dark interface, focus on the camera control panel"
      - "Anthropic logo over a gradient background, new model announcement"
      - "Design studio with monitor showing an AI-generated video still,
        creative environment, natural light"
      The Visual hint is MANDATORY on every news item. It's what allows R2
      to generate a coherent image when there's no usable real photo.

   c. If you didn't find an image URL: that's fine. "Has hero?" = false. R2
      (which runs locally, with open network) will extract the image from the
      chosen news item, or generate one from the Visual hint.

6. INSERT into the "🗞️ News Feed" database via the Notion MCP:
   - Title (pt-BR)
   - Source
   - Link (news URL)
   - Summary (2-3 sentences)
   - Relevance (1-5)
   - Collection date (today)
   - Time slot (Morning/Afternoon/End of afternoon)
   - Status = "Pending"
   - Original URLs (text): the candidate image URL, if you found one
   - Has hero? (checkbox): true if you found a candidate image URL,
     false if not
   - Visual hint (text): the visual description of the image (ALWAYS filled in)

7. Limit: 8 news items per round. If there are more, keep the 8 with highest
   relevance.

8. NEVER modify existing entries. NEVER change the status of an already-inserted
   news item. Only insert new ones.

9. Source down / link won't open → skip and move on. Don't invent.

10. News without an image is OK — don't discard for lack of image.

## Final output
News Scout — {date} {time slot}
Searched X sources. Inserted Y news items (Z with candidate image URL, W without).
Discarded D duplicates.
Top of the round: "{title}" (relevance N).

## Absolute rules
- web_search and web_fetch ONLY. Never curl, never direct HTTP, never external API.
- pt-BR translation always.
- Don't invent news. Zero inserted is OK (weekend, no news).
- Don't duplicate.
- Visual hint ALWAYS filled — it's what guarantees a good carousel image
  even when there's no real photo.
````

---

## REPLACE in the prompt before pasting

| Token | Replace with |
|---|---|
| `{brand_name}` | Real brand name |
| `{brand_subject}` | Real niche |
| `{cron_r1_hours}` | Cron hours |
| `{NOTION_PAGE_URL}` | Real main page URL |

The setup agent does this interpolation when creating the Routines.

---

## First run

Run **Run now** once and observe. Confirm the run passes **without a permission prompt** (automatic permission mode). If it asks for permission, adjust the Routine config.

---

## Expected actual time

**~3-6 min per run.** Without the image download cascade (gone in V2.5), R1 became faster and more reliable — it's only text: web_search + web_fetch + insert into Notion.

If a run goes over 15 min, a source is probably hanging — check the logs.

---

## Verify it's running

**Status:** Routine panel → Active/Paused + last run + next run.

**Logs:** panel → click on a run → full session.

**Notion:** `🗞️ News Feed` → "Today" view → entries with pt-BR title, summary, relevance 1-5 and **Visual hint** filled in.

---

## Test before scheduling

1. Create the Routine with Schedule **Off**
2. Run now
3. Wait 3-6 min
4. Confirm in Notion ("Today" view of the News Feed):
   - News with pt-BR title, coherent summary, relevance 1-5
   - **Visual hint filled in** on all
5. If error: read the run's session in the panel
6. OK → activate the Schedule

---

## Recommended: let it accumulate before bringing up R2

Let R1 run for 2-3 days before activating R2. The more varied news in the feed, the better R2's choice.

---

## Migrate from V2 (Web Routine in claude.ai/code)

1. claude.ai/code → Routines → old R1 → Schedule **Off**
2. Create a new **Remote** Routine in Claude Desktop per this page (new prompt — the image cascade is gone)
3. Run now to validate
4. Confirmed → delete the old Web Routine

`🗞️ News Feed` in Notion is the source of truth — there's no need to migrate data.
