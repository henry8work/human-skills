# 16 — Troubleshooting (V2.5)

Diagnosis of the most common problems. Version V2.5 — Claude Desktop Routines.

---

## Setup via CLI + Notion API

### Notion token does not authorize access
- **Symptom:** `403 Forbidden` when trying to create pages
- **Cause:** the integration was not shared on the main page
- **Solution:** Notion page → ••• → Add connections → select the integration → confirm

### Structure partially created (some blocks missing)
- **Cause:** Notion rate limit (3 req/s soft)
- **Solution:** the agent already adds `time.sleep(0.4)` between batches. If it still fails, run `rebuild brand` in the agent — it detects gaps and completes.

### Page only has title, no content
- **Cause:** first pass creates the page, second pass adds the blocks. If the second one silently fails, only the title is left.
- **Solution:** `rebuild brand` in the agent. It does not recreate the page, only PATCHes blocks.

### Code block with language rejected
- **Error:** `validation_error: language is not a valid language`
- **Cause:** language outside Notion's allowlist (e.g. `sh`, `console`)
- **Solution:** the `md_to_notion.py` parser normalizes: `sh` → `bash`, `js` → `javascript`, etc.

### Truncated table
- **Cause:** Notion API limits blocks per call (100). A 150-row table overflows.
- **Solution:** parser paginates automatically. If it still truncates, edit manually or split the table into two in the `.md`.

---

## R1 (News Scout — Remote Routine)

### Did not insert any news
- **Cause 1:** filter too restrictive or no source with updates in the last 5h. Normal on weekends.
- **Cause 2:** all candidates were duplicates.
- **Solution:** edit the `📋 News Sources` page (add sources, tweak the dedup threshold in the prompt).

### Inserting junk
- **Solution:** tweak the "Topics to IGNORE" section in `📋 News Sources`. Specific beats generic.

### Wrong relevance
- **Solution:** reinforce examples in the relevance criterion in `📋 News Sources`. "A 5 IS X, a 5 is NOT Y."

### News in English
- **Solution:** reinforce in the R1 prompt: "Translate to Portuguese always, keep technical terms in English when standard."

### R1 marked every news item with "Has hero? = false"
- **This is expected and NOT an error.** R1 runs Remote — the cloud sandbox blocks direct HTTP (curl/requests return 403). R1 **does not download images by design**. It only discovers a candidate URL (best-effort via web_fetch) and writes the `Visual hint`.
- **The one that actually extracts the image is R2** (Local, open network), in Step 1.5, only for the chosen news item.
- **What to verify:** is the `Visual hint` column on the News Feed filled in? If yes, the system is healthy — R2 will extract the photo or generate one from the hint.
- **If the `Visual hint` is empty:** then yes it's a bug — reinforce in the R1 prompt that the Visual hint is mandatory on every news item.

### R2 can't get the news photo (Step 1.5 always falls to "ai-generated")
- **Symptom:** the run summary shows `News image: AI-generated` every time — never extracts a real photo
- **Remember:** "AI-generated" **is not failure** — the carousel comes out complete with a coherent image (Path B, from the Visual hint). It's just not the literal photo of the news.
- **If you want more real photos, diagnose Step 1.5** (runs Local — the cascade works, unlike R1):
  - **Site blocks everything (403 on browser-UA):** Level C tries as `facebookexternalhit` and `Twitterbot` — many sites serve a clean og:image to those. Confirm R2 is trying the 3 User-Agents.
  - **og:image empty but the page has an image:** lazy-load / JSON-LD. Level B scans `data-src`, `data-lazy-src`, `srcset`, JSON-LD. Confirm.
  - **Relative URL:** R2 needs to resolve `/images/foo.jpg` via urljoin against the news URL.
  - **R1 candidate URL dead:** the URL R1 left can have expired between R1 and R2 (12-24h later). Normal — R2 falls to Level B (extracts from scratch).
  - **Good image discarded by validation:** if the URL has "logo"/"icon" in the path but is the right image, the substring filter may be dropping it. Refine the filter to match only the file name.
- **Health criterion:** the goal is not 100% real photos. AI news often doesn't have a good hero anyway. Path B with a rich Visual hint produces a great cover. The focus is on the Visual hint being good.

### R1 takes 30+ min
- **Symptom:** a run that should take 5-8 min hangs
- **Common cause:** a specific source hangs the agent (timeout not configured)
- **Solution:** add a `5s` timeout to every HTTP fetch in the prompt; identify the stuck source from the logs and mark it priority=low or remove it

### Status changing without you asking
- **Cause:** R1 messing with entries it shouldn't
- **Solution:** make sure the prompt says "NEVER modify existing entries" (step 10)

---

## R2 (Carousel Creator — Local Routine)

### Routine did not fire at the expected time
- **Cause 1:** Claude Desktop was not open at the tick time
- **Cause 2:** Mac/Windows was sleeping
- **Cause 3:** Routine paused in the panel
- **Solution — 3 fallback layers already set up in V2.5:**

  **a) `*/30 8-22` Schedule:**
  Routine fires every 30 min between 08:00 and 22:00. The first tick in which the app is open runs the carousel. The next ones detect `.completed` and soft-exit in <2s — negligible cost. Without this frequent schedule, you lost the day if the app wasn't open exactly at 08:00.

  **b) Automatic catch-up:**
  If you only open the app in the afternoon after it was closed, Claude Desktop fires 1 automatic run of the most recent missed tick (7-day coverage).

  **c) Manual:**
  Routine panel → **Run now** forces it now.

- **How to diagnose which layer didn't work:**
  - Schedule didn't fire? Check the cron expression in the Routine panel
  - Catch-up didn't fire? Check that the Schedule is Active (toggle On)
  - To avoid sleeping at the scheduled time: macOS → System Settings → Battery → "Prevent computer from sleeping when display is off"; Windows → Power & sleep → Never

### Routine runs but does immediate soft exit (generates nothing)
- **Symptom:** Routine fires but ends in ~2 seconds without generating a carousel
- **Cause:** It's **correct behavior** — the day's `.completed` already exists, so the Routine exits immediately (idempotency). The carousel was already generated on a previous tick.
- **Verify:** check in `~/{brand-slug}/state/$(date +%Y-%m-%d)/` whether `.completed` and the other expected files exist
- **If you really want to regenerate:** Run now → first message `--re-render` (visual-only re-render) or `--news=N` (swap news)

### R2 Routine does not run on its own — stays in "Ask Permissions"
- **Symptom:** the 8am automatic run doesn't generate the carousel. When you open it, the Routine is stopped asking for confirmation. Each new run chat of the day comes in "Ask Permissions" mode.
- **Root cause:** the Routine's permission mode is on "Ask Permissions" — it asks for human OK on each action. Without someone to click, the run hangs. `Always allow` ticked in one run **does not persist** for new runs/chats.
- **Solution (two layers):**

  **1. Routine permission mode = automatic**
  Open the R2 Routine config → permissions. Take it off "Ask Permissions". Put it on the mode that runs without asking for confirmation ("Allow all" / "Auto" / "Full access" / "Bypass permissions" — the name varies). This is the main fix.

  **2. `.claude/settings.json` in the working folder**
  Confirm that `~/{brand-slug}/.claude/settings.json` exists with:
  ```json
  {
    "permissions": {
      "allow": ["Bash", "Read", "Write", "Edit", "WebFetch", "WebSearch"]
    }
  }
  ```
  The setup creates this file. If it doesn't exist, create it by hand. The project allowlist covers the local tools even if the permission mode resets.

- **Acceptance criterion:** run **Run now** and observe. If it goes through from start to finish **without a single permission prompt**, the automation will work. If any prompt appears, it's still not right — adjust and test again.

### Higgsfield CLI missing, not logged in or out of credit
- **Symptom:** render aborted before generating cover or slides
- **Diagnosis:** test manually in the Routine's session itself:
  ```bash
  higgsfield account status
  ```
  - command not found → install `npm install -g @higgsfield/cli`
  - missing login → run `higgsfield auth login`
  - insufficient credits → top up at Higgsfield

### R2 stops early with Higgsfield not authenticated
- **Cause:** CLI not installed or local login not completed.
- **Solution:** run `higgsfield auth login`, confirm in the browser and run `higgsfield account status`.

### Logo doesn't appear on slides 1 and 9
- **Symptom:** `brand_has_logo=true` but the carousel comes out with no logo
- **Cause 1:** the logo was not attached on the `🏷️ Brand Identity` page (section "Brand logo"). The run summary shows `Logo: ⚠️ brand_has_logo=true but no attachment`
- **Cause 2:** the attachment is not a PNG or is corrupted
- **Solution:** attach a valid PNG (transparent background, ≥800px) in the "Brand logo" section of the `🏷️ Brand Identity` page. Run `--re-render`.
- **Note:** the logo is pasted via Pillow composition (not drawn by the generator). If the slide came out with the logo area empty but the logo didn't enter, it's because the `logo.png` was not downloaded — check the attachment in Notion.

### Editorial pipeline runs but render fails
- **Symptom:** `narrativa.json` exists, `slides/` empty (or only `cover-url.txt`)
- **Verify:** `cat ~/{brand-slug}/state/$(date +%Y-%m-%d)/log.txt`
- **Common cause 1:** Higgsfield CLI/login/credits (see above)
- **Common cause 2:** missing `--image` UUIDs on slides 2-9
- **Solution:** see `COVER_URL` bug below

### Cover comes out but slides 2-9 don't maintain coherence
- **Main cause:** `--image` UUIDs are not being passed to slides 2-9
- **Diagnosis:** check `state/$TODAY/url-N.txt` — if empty, it failed. Check the session logs.
- **Solution:** ensure the Routine is uploading the logoless cover + the brand visual refs with `higgsfield upload create` and passing those UUIDs into every internal slide.

### Empty `COVER_URL` bug
- **Symptom:** slides 2-9 call Higgsfield with no reference
- **Cause:** session captured the cover URL/job but did not persist it before starting the parallel batch
- **Solution:** ensure the Routine prompt always writes `cover-url.txt` BEFORE starting slides 2-9:
  ```bash
  COVER_URL=$(echo "$COVER_RESP" | python3 -c '...')
  echo "$COVER_URL" > state/$TODAY/cover-url.txt
  # ONLY THEN fire parallel
  ```
  Never trust a bash variable between steps — always write to file.

### Parallel render but a slide came out wrong
- **Diagnosis:** with parallel, logs mix. Ask the session to prefix each line with `[slide-N]`
- **Targeted solution:** re-run only the problem slide:
  ```
  > --only-slide=5
  ```

### Visual briefing came out generic
- **Diagnosis:** open `state/$TODAY/visual-brief.txt` — if it mentions "vibrant colors" and vague words, it failed
- **Main cause:** the `🖼️ Visual References` page only has textual descriptions, no real images attached
- **Solution:** attach a minimum of 5 real images covering variety (cover, dark slide, light slide, slide with photo). Vision needs variety to extract a pattern.

### State directory taking up disk
- **Cause:** accumulates ~50-100MB per day (refs + slides + raw PNGs)
- **Solution:** run the archive script quarterly (cf. `15-Como-usar.md` best practices)

### Slides only appear hours later in Notion
- **Cause:** PNG upload (slow) was being used instead of external URLs
- **Solution:** the Routine prompt uses external URLs returned by Higgsfield or Drive URLs. Appears immediately. If still slow, check whether properties.Slides has type=external in the PATCH.

### Routine consuming too much subscription
- **Symptom:** Pro+ quota tightening
- **Cause:** long runs or parallel turned sequential
- **Diagnosis:** see average duration in the panel's run list. Healthy: 6-10 min.
- **Solution:** if it goes over 18 min, something is stuck (probably step 2 with too many redundant web searches, or a visual batch that didn't parallelize). Adjust the prompt limiting web_fetch to 3-5 calls per run and check that slides 2-9 are in parallel.

---

## Claude Desktop (operational)

### Routine disappeared from the panel
- **Cause:** app was updated and lost the config
- **Solution:** Routines are saved locally. Recommended backup: copy the Routine prompt to a file `~/{brand-slug}/r2-routine-prompt.txt` after every edit

### Notion / Drive MCP disconnected
- **Symptom:** Routine fails right at the start with a connector error
- **Solution:** Settings → Connectors → reconnect. No need to redo the Routine.

### Catch-up didn't fire as expected
- **Cause:** catch-up only covers **the most recent missed run** of the last 7 days, not multiple
- **Solution:** if you want to run a specific day X, open the panel → Run now → first message `--news=N` (pick the news from the desired day)

### App is open but the Routine doesn't fire
- **Diagnosis:** Routine panel → Schedule status must be "Active"
- **Cause:** toggle off
- **Solution:** turn on the toggle

---

## Notion (operational, post-setup)

### R2 overwrites the carousel of previous days
- **Cause:** wrong filter when locating the day's entry (Routine confusing dates)
- **Solution:** the prompt always filters `Date == TODAY` (exact date). Reinforce it in the prompt if needed.

### "🎨 Carrosséis" database filling up too much
- **Solution:** the "Archive" view filters Posted/Discarded older than 90 days. The default "Gallery" view only shows recent ones.

---

## Higgsfield CLI

### Error with aspect ratio or dimensions
- **Cause:** undeclared proportion or unexpected output
- **Solution:** use `--aspect_ratio "3:4"` and `--resolution "2k"` in the call, validate that the output is 3:4 and deliver the original downloaded PNG. Don't normalize, crop, resize or convert to 1080×1350.

### Cost is high
Solutions:
- Check credits with `higgsfield account status`
- Generate only necessary variations
- Re-render only when worth it (don't keep swapping on a hunch)

### `Insufficient credits`
- Solution: top up at Higgsfield. The Routine marks slides as failed and continues.

### Slides are coming out identical to the cover
- **Cause:** the internal slide's prompt is copying the cover instead of using the cover as style
- **Solution:** reinforce in the Routine prompt:
  > "Use the cover and brand references for visual style only: palette, typography, mood and composition system. Create different content for this internal carousel page. Do not copy the cover layout or render any page number/counter."

---

## When nothing renders — step-by-step debug

1. Is R1 running? → claude.ai/code/routines → Runs (or Desktop Routines panel)
2. Does the News Feed have yesterday's entries? → "Today" view in Notion
3. Did R2 fire? → Local Routine panel → last run
4. Did the editorial pipeline complete? → `cat ~/{brand-slug}/state/$(date +%Y-%m-%d)/narrativa.json`
5. Was the visual brief generated? → `cat ~/{brand-slug}/state/$(date +%Y-%m-%d)/visual-brief.txt`
6. Was the cover generated? → does `cover-url.txt` exist and is populated?
7. Were slides 2-9 generated? → do `url-2.txt` through `url-9.txt` exist?
8. Did the Drive backup complete? → check the folder `{brand_slug}/Carrosseis/$(date +%Y-%m-%d)/` in Drive
9. Was Notion updated? → new entry in `🎨 Carrosséis` with Slides populated?

Find the step where it broke. The fix will be in a Notion page (instruction, `🔐 Configuration`, `🖼️ Visual References`) or in the Routine prompt — almost never in code.

---

## Learnings that became V2.5 rules

| Learning | Where it became a rule |
|---|---|
| Sandbox blocked direct API calls | Hybrid architecture: R2 becomes Local Routine with Higgsfield CLI |
| Scripts + launchd have too much error surface | Everything collapses into ONE Local Routine prompt |
| Vision on the refs needs real bytes | The Routine downloads via curl + Claude's native Read |
| Sequential render is slow | Slides 2-9 always in parallel via bash & + wait |
| Capturing URL via filesystem is fragile | `cover-url.txt` written IMMEDIATELY after cover |
| Base64 upload blows up the context | Notion entry uses external URLs and Drive as backup |
| Remote sandbox blocks direct HTTP | R1 doesn't download images; extraction migrates to R2 Local (Step 1.5) |
| R1 failed every hero with 403 | R1 only does best-effort URL + writes textual Visual hint |
| Routine in "Ask Permissions" hangs the automation | Automatic permission mode + `.claude/settings.json` in the working folder |
| Logo drawn by the AI distorts | Logo composited via Pillow over a reserved area |
| Mac can be offline at 8am | Automatic catch-up + `*/30 8-22` schedule |
| Re-render used to be an exception, became a rule | The `--re-render` command is primary |
| Manual setup in Notion is slow | CLI setup + Integration Token creates everything via API |
| Homebrew + jq + magick + rclone is too much setup | Zero external deps — Claude Desktop has it all |
