# 17 — Troubleshooting

Diagnosis of the most common problems. Creative DNA V1.0 System — Claude Desktop Routines.

---

## Setup via CLI + Notion API

### Notion token doesn't authorize access
- **Symptom:** `403 Forbidden` when trying to create pages
- **Cause:** integration wasn't shared on the main page
- **Solution:** Notion page → ••• → Add connections → select the integration → confirm

### Structure created partially (some blocks missing)
- **Cause:** Notion rate limit (3 req/s soft)
- **Solution:** the agent already adds `time.sleep(0.4)` between batches. If it still fails, run `rebuild DNA` on the agent — it detects gaps and completes.

### Duplicate pages after setup
- **Cause:** creation ran in background + foreground simultaneously (classic bug)
- **Solution:** delete the duplicates manually in Notion, then run `rebuild DNA`. Ensures `.brand.json` points to the correct IDs.

### Code block with rejected language
- **Error:** `validation_error: language is not a valid language`
- **Cause:** language outside Notion's allowlist (e.g. `sh`, `console`)
- **Solution:** the `md_to_notion.py` parser normalizes: `sh` → `bash`, `js` → `javascript`, etc. Same parser as the Carousel.

### Truncated table
- **Cause:** Notion API limits blocks per call (100). A 150-row table overflows.
- **Solution:** parser paginates automatically. If still truncated, edit manually or split the table in two in the `.md`.

### Discovery wizard interrupted midway
- **Cause:** you closed the terminal, or the Mac slept, or unexpected error
- **Solution:** state saved in `~/{brand-slug}/.discovery-progress.json`. Reopen:
  ```bash
  cd ~/{brand-slug}
  claude
  > continue discovery
  ```
  Agent resumes from the last answered question.

---

## R1 (Brand Scout — Remote Routine)

### Collected no references
- **Cause 1:** `brand_aesthetic_anchor` is empty or too generic (e.g. "modern" — can't search)
- **Cause 2:** search queries returned nothing relevant
- **Solution:** edit `🧬 DNA Master` → "Anchor aesthetic" section → fill with 2-3 specific references (Eye Magazine, Dia Studio, etc.). Next run uses them.

### R1 bringing only anti-references
- **Symptom:** all collected pending items violate some anti-reference
- **Cause:** the search criterion is poorly calibrated
- **Solution:** review `📚 Reference Library` → Section D (anti-references) — is it complete? If yes, it may be that the brand's niche has a lot of noise. Refine queries in the R1 prompt.

### Competitor without recent snapshot
- **Cause 1:** competitor's handle changed
- **Cause 2:** competitor's Instagram is private / offline
- **Solution:** update `🔐 Configuração` → `SCOUT_COMPETITOR_HANDLES`. Re-paste the R1 Routine prompt with the updated list.

### Trend analysis without clear pattern
- **Symptom:** monthly analysis returns "30 very heterogeneous refs"
- **Cause 1:** you're approving very varied refs (no unified visual criterion)
- **Cause 2:** brand's aesthetic is in transition
- **Solution:** if (1), review approval criteria in weekly curation. If (2), consider running `evolve` mode (b) Visual refresh on the DNA's R2.

### R1 takes 30+ min
- **Symptom:** a run that should take 6-15 min hangs
- **Common cause:** specific source hangs the agent (timeout not configured)
- **Solution:** add `5s` timeout on each HTTP fetch in the prompt; identify hung source from logs and remove from query

### Status changing without you asking
- **Cause:** R1 messing with entries it shouldn't
- **Solution:** ensure prompt says "NEVER modifies existing entries — only inserts new pending ones" (final step)

---

## R2 (DNA Routine — Local Routine)

### R2 Routine doesn't run — stuck in "Ask Permissions"
- **Symptom:** Run now hangs asking human confirmation for each action
- **Root cause:** Routine's permission mode is set to "Ask Permissions"
- **Solution (two layers):**

  **1. Routine permission mode = automatic**
  Open R2 Routine config → permissions. Remove from "Ask Permissions". Set to automatic mode ("Allow all" / "Auto" / "Bypass permissions" — varies by app version).

  **2. `.claude/settings.json` in working folder**
  Confirm there's a `~/{brand-slug}/.claude/settings.json` with:
  ```json
  {
    "permissions": {
      "allow": ["Bash", "Read", "Write", "Edit", "WebFetch", "WebSearch"]
    }
  }
  ```
  
- **Acceptance criterion:** run Run now. If it passes start to finish without a prompt = OK.

### Higgsfield CLI missing or not logged in (Generate mode)
- **Symptom:** R2 stops at Step 0 when validating `higgsfield account status`
- **Solution:** install `npm install -g @higgsfield/cli`, run `higgsfield login` and confirm with `higgsfield account status`.

### R2 Generate mode fails on copy but works on image (or vice versa)
- **Symptom:** pure copy generate works; image generate fails on CLI
- **Cause:** CLI/login/credits/queue issue
- **Solution:**
  - CLI missing → install `@higgsfield/cli`
  - login missing → `higgsfield login`
  - 429 → rate limit, sleep 5s between calls
  - 500 → retry 1-2x

### Compliance score always high / always low
- **Symptom:** audits always return score 9-10, or always 4-6
- **Cause 1 (high):** DNA poorly defined — agent can't discriminate
- **Cause 2 (low):** anti-patterns too broad — anything matches
- **Solution:** review `🚫 Anti-Patterns` and `🗣️ Voice & Tone` — whether the rules are too vague OR too restrictive. Calibration takes 30-60 days of use.

### Score on one dimension always low
- **Symptom:** Voice dimension always 5-6, but Visual always 8-9
- **Cause:** that dimension needs more density in the DNA
- **Solution:** open the relevant page (`🗣️ Voice & Tone` if Voice, `🎨 Visual System` if Visual), add more specificity. Criterion: "if I remove the dimension and read the rest, do I know how to produce in that dimension on my own?"

### R2 suggests change in DNA but you disagree (Evolve mode)
- **Symptom:** ran evolve, R2 proposed diff, but something doesn't match your view
- **Solution:** option (e) Edit — open each diff item individually, adjust. Or cancel the application — DNA stays intact.

### Evolve applied a change and I want to revert
- **Symptom:** I applied evolve but the result turned out bad
- **Solution:** pre-evolution snapshot is in Drive `{brand_slug}/DNA-Snapshots/{TODAY}-pre-evolve/`. Use those files to restore:
  ```bash
  cd ~/{brand-slug}
  claude
  > restore DNA snapshot from {date}
  ```
  Agent PATCHes all affected pages back to pre-change state.

### Generated output has invented information (hallucination)
- **Symptom:** R2 generated copy citing data/case that doesn't exist
- **Cause:** R2 didn't verify via web search (skipped Parameter 4 - Verified facts)
- **Solution:** reinforce in R2 Routine prompt: "EVERY statistic goes through web_fetch/web_search before output. If it couldn't be verified, rewrite without the data."

### State directory taking up disk
- **Cause:** accumulates 50-200MB per month (briefs + outputs + audits + refs cache)
- **Solution:** run quarterly:
  ```bash
  cd ~/{brand-slug}/state
  find . -maxdepth 1 -type d -mtime +90 -exec tar -czf {}.tar.gz {} \; -exec rm -rf {} \;
  # Upload the .tar.gz to Drive via MCP or web app
  ```

### `.dna.json` out of sync with Notion
- **Symptom:** you edited a page in Notion, but R2 still uses the old version
- **Cause:** `.dna.json` is a local cache
- **Solution:**
  ```bash
  cd ~/{brand-slug}
  claude
  > rebuild .dna.json
  ```
  Agent reads all DNA pages from Notion, regenerates local JSON. ~30s.

---

## Notion (operational, post-setup)

### `🧬 DNA Master` showing `{brand_*}` literally (not interpolated)
- **Cause:** page was populated by a human (without interpolation) or rebuild bugged
- **Solution:** `> rebuild DNA --pages=dna_master` on the agent. Re-does interpolation.

### Database `🎯 Assets` filling up too much
- **Solution:** "Archive" view filters Status = Archived / Discontinued. Default "Gallery" view shows only recent. To archive in bulk:
  ```bash
  > archive assets approved more than 6 months ago
  ```

### Old Compliance entries mixing with recent ones
- **Solution:** "Recent" view filters Audit date >= 30 days. "History" view shows everything (only use for comparative analysis).

### Relations between databases broken
- **Symptom:** Brief doesn't pull related Asset, or vice versa
- **Cause:** manual edit in Notion broke the link
- **Solution:** open the database, on the Relation property, confirm destination_database_id. If wrong, delete and recreate the relation manually, then run `> repair relations` on the agent.

---

## Higgsfield CLI (image generation in Generate mode)

### 400 Error with `image_size`
- **Cause:** dimension not multiple of 16
- **Solution:** use approved aspect ratios (`4:5`, `9:16`, `1:1`, `16:9`) and normalize locally when needed.

### Cost is high
| Scenario | Cost |
|---|---|
| 1 pure audit (no image) | $0 (no visual generation) |
| 1 audit with vision (reads image) | $0 (native Claude vision) |
| 1 copy generate | $0 |
| 1 hero image generate | $0.05-0.08 |
| 1 composite piece generate (2-4 images) | $0.20-0.40 |
| 1 carousel generate (9 images) | $0.50-0.70 |

Solutions:
- Check credits with `higgsfield account status`
- Generate only necessary variations
- Log model, job_id and attempt

### Slides coming out identical to cover
- **Cause:** slide N prompt isn't making clear it's ANOTHER slide
- **Solution:** same as Carousel — reinforce in Routine prompt:
  > "This is image [N] of [TOTAL], NOT a duplicate. Match the visual STYLE (palette, typography, mood) of reference, but show DIFFERENT content."

---

## Real vision / Reference Library

### Visual briefing came out generic (image Generate mode)
- **Diagnosis:** open `state/$TODAY/briefs/{N}-{slug}/visual-brief.txt` — if it mentions "vibrant colors" and vague words, it failed
- **Main cause:** `📚 Reference Library` (Section A) has only text descriptions, no real images attached
- **Solution:** attach minimum 5 real images covering variety (hero, post, slide, composite piece). Vision needs variety to extract a pattern.

### R2 isn't reading refs from my thematic pack
- **Cause:** "Active pack" isn't marked in the Library
- **Solution:** check if the thematic pack entry has `ATIVO: true` field in Notion. R2 only prioritizes packs with active flag.

---

## Integration with the Carousel system

### Carousel R2 isn't reading the DNA
- **Symptom:** Carousel comes out with old tone, ignoring DNA updates
- **Cause:** Carousel's R2 Routine prompt wasn't updated to include Step -1 (load DNA)
- **Solution:** edit Carousel's R2 Routine prompt, add BEFORE Step 0:
  ```
  STEP -1 — Load Creative DNA
  - Reads page_dna_master via MCP Notion
  - Loads local .dna.json
  - brand_* variables come FROM HERE (not from the legacy 🏷️ Brand Identity page)
  - Editorial manual passes through DNA's 🗣️ Voice & Tone filter
  - DNA's Visual System has precedence over legacy 🎨 Design system
  ```

### Conflict between Brand Identity (Carousel) and DNA Master (DNA)
- **Symptom:** the two pages have different versions of the same variable (e.g. different primary color)
- **Solution:** DNA is the source of truth. Empty the Carousel's `🏷️ Brand Identity` page leaving only a note:
  ```
  ⚠️ This page is legacy. Canonical variables now live in 🧬 DNA Master.
  Carousel's R2 reads DNA first.
  ```

---

## Claude Desktop (operational)

### Routine disappeared from the panel
- **Cause:** app was updated and lost config
- **Solution:** Routines are saved locally. Recommended backup: copy both Routine prompts to files `~/{brand-slug}/r1-routine-prompt.txt` and `~/{brand-slug}/r2-routine-prompt.txt` after any edit.

### MCP Notion / Drive disconnected
- **Symptom:** Routine fails right at the start with connector error
- **Solution:** Settings → Connectors → reconnect. No need to redo Routine.

### App is open but R1 Routine doesn't trigger
- **Diagnosis:** R1 Routine panel → Schedule status should be "Active"
- **Cause:** toggle disabled or wrong cron expression
- **Solution:** enable the toggle. If cron is wrong, set it to `0 10 * * 1,3,5` (default).

---

## When everything fails — step-by-step debug

1. Is R1 running? → Desktop Routines panel
2. Does Reference Library have recent pending? → Section E in Notion
3. Does R2 BRIEF mode list jobs? → Run now without message
4. Does R2 AUDIT mode work on text? → paste a simple post, see if it returns score
5. Does R2 GENERATE mode of copy work? → "generate: simple caption about X"
6. Does R2 GENERATE mode of image work? → "generate: hero shot for landing X" (needs Higgsfield CLI ok)
7. Does `.dna.json` reflect the Notion? → `cat .dna.json | jq .` and compare with `🧬 DNA Master`

Find the step where it broke. Fix will be on a Notion page (instruction, `🔐 Configuração`, `📚 Reference Library`) or in the Routine prompt — almost never in code.

---

## Lessons learned that became V1.0 rules

| Learning | Where it became a rule |
|---|---|
| Frozen brand book goes unused → DNA must be executable | Whole system is "read by AI, not just by humans" |
| Superficial discovery generates superficial DNA → 52 questions with quality criteria | Pro wizard forces specificity |
| Explicit anti-pattern > waiting for good taste | `🚫 Anti-Patterns` is a page with depth equal to `🗣️ Voice & Tone` |
| Ref vision needs real bytes | R2 downloads via curl + Claude native Read |
| DNA needs to be organism, not monument | R1 feeds refs continuously; quarterly auto-snapshot |
| Subjective compliance creates rework | Quantitative compliance score (0-10 per dimension) |
| Onboarding a new member takes weeks → explicit DNA speeds up | 7-day onboarding protocol |
| Competitor without monitoring creates weak differentiation | R1 monitors 3 competitors monthly |
| Generic persona generates generic copy → persona as a novel character | `👥 Audience DNA` requires dense 6-10 line bio |
| Hardcoded generation key is fragile | Higgsfield CLI stays authenticated locally |
| Routine on "Ask Permissions" hangs | Automatic permission mode + `.claude/settings.json` |
| Conflict between legacy Brand Identity and DNA → resolve with precedence | DNA is canonical; Brand Identity becomes legacy |
| Mac can be offline | R2 DNA is manual (has no daily schedule); R1 has catch-up |
| Manual setup in Notion is slow | CLI Setup + Integration Token creates everything via API |
| Annual refresh without snapshot is risky | Automatic pre-discovery snapshot |
