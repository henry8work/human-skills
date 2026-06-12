# 15 — Day-to-day use

Seven use scenarios once everything is up and running.

---

## Scenario 1 — Fully automatic (default case)

1. During the previous day, R1 (Remote Routine) fills the News Feed (3x a day)
2. The **Local** R2 Routine fires on the first tick of the day (`*/30 8-22`) in which Claude Desktop is open
3. R2 executes editorial pipeline + parallel render + Notion + Drive backup
4. Subsequent ticks of the day fall into soft exit (~2s, zero cost) because `.completed` already exists
5. You open Notion on your phone, "Gallery" view of `🎨 Carrosséis`
6. You see the day's carousel (Status: Draft), evaluate visually
7. If approved: set Status = Approved, download the 9 PNGs, post on Instagram
8. Set Status = Posted

Time spent on your part: **~3 min/day**.

> **Robust fallback (3 layers):**
> - `*/30 8-22` schedule — catches the first time of the day the app opens
> - Automatic catch-up — if the app was closed for hours, fires 1 run for the most recent missed tick when you open it
> - Manual — Run now in the panel at any time
>
> Even if you only open the app in the afternoon, the day's carousel is generated. No need for the Mac to be always on.

---

## Scenario 2 — Swap the chosen news item

Situation: R2 chose a bad news item. You prefer Nº 12.

**Option A — Run now in the Routine panel:**
1. Open Claude Desktop → Routines → `{brand_name} — Carousel Creator`
2. **Run now** button
3. First message of the session: `--news=12`

R2 marks the day's previous entry as Discarded with prefix `[Replaced]`, generates a new carousel with Nº 12, creates a new entry.

Time: ~5-10 min.

**Option B — Conversational claude CLI (outside the Routine):**
```bash
cd ~/{brand-slug}
claude
> regenerate today's carousel with news 12
```

Conversational agent fires the equivalent. Useful when you don't remember the flags.

**Option C — Pin for the next cron:**
News Feed → desired news → Status = Pinned. Tomorrow's 8am R2 uses that one with priority (the sort filter already favors Pinned).

---

## Scenario 3 — Carousel from a simple topic

Situation: you don't want to wait for the news feed. You only have an idea.

Examples:

```text
/carrossel I want a carousel about electric bicycles in São Paulo
```

```text
/carrossel make a carousel about how small businesses can use AI in customer service
```

The agent must research, pick the angle and structure it. The person doesn't have to bring a headline, script or data.

**If using the Local Routine:**

1. Open Claude Desktop → Routines → `{brand_name} — Carousel Creator`
2. **Run now** button
3. First message of the session:

```text
I want a carousel about electric bicycles in São Paulo
```

or:

```text
--topic="electric bicycles in São Paulo"
```

R2 creates a manual pitch of the day, researches the topic, generates a headline, 9-slide narrative architecture, caption, visual brief, slides, Drive and Notion. In this mode, it doesn't depend on a news item in the News Feed.

**If there isn't a complete visual setup yet:**
the agent delivers headline, slides, caption, visual direction and render checklist, without blocking creation.

---

## Scenario 4 — Re-render when the visual came out weak

Situation: excellent copy, but the carousel ended up visually generic.

**Option A — in the session of the run that just finished:**
If the Routine session is still open, just send a message:
```
> --re-render
```

The session already has the full context (narrativa.json, visual-plan.json in memory). Skips steps 1, 2, 3. Re-runs 4-8.

**Option B — Run now in the Routine panel:**
1. Routines → `{brand_name} — Carousel Creator` → Run now
2. First message: `--re-render`

Fires a new session. Reads existing state from disk (`./state/{TODAY}/`), skips steps that already have output, re-runs from the visual brief onward.

Cost: check Higgsfield credits. Time: depends on queue/model.

**When it makes sense:**
- You edited `🖼️ Visual References` (attached new images, adjusted descriptions)
- You adjusted `🏷️ Brand Identity` (primary color, contrast)
- Higgsfield/model had a "bad day" — some slides came out conflicting with the cover

**When it does NOT make sense:**
- Weak copy → edit `📚 Editorial Manual`, fire Run now WITHOUT `--re-render` (full run)
- Wrong news → Run now with `--news=N`

---

## Scenario 5 — Adjust a specific slide

Situation: 8 slides are great, but slide 5 came out weird.

**Option A — in the Routine session still open:**
```
> regenerate only slide 5 with more visual density. Keep the rest.
```

Session:
1. Reads `state/$TODAY/narrativa.json` and `visual-plan.json` from disk
2. Adjusts slide 5's prompt per your request
3. Calls the Higgsfield CLI with GPT Image 2 (`gpt_image_2`) and reference UUIDs (`--image cover_uuid` + brand visual refs + news hero when applicable)
4. Overwrites `url-5.txt` and (optionally) `slides/slide-05.png`
5. PATCH on the Notion entry (only slide 5)

Time: ~30s. Cost: $0.05.

**Option B — Run now with flag:**
```
--only-slide=5
```

Useful variations:
- *"On slide 5, swap the table for a single centered card"*
- *"Regenerate slide 2 with grainier texture"*
- *"Drop the background photo on slide 6, keep only solid dark"*

---

## Scenario 6 — Change the entire feed's aesthetic

Situation: tired of the current aesthetic, want to give the next carousel a visual refresh.

**No need to touch the Routine prompt.**

1. Edit the `🖼️ Visual References` page in Notion:
   - Replace the attached images with new ones
   - Update textual descriptions
   - Update anti-examples
2. Optional: adjust the primary color in `🏷️ Brand Identity`
3. The next carousel (next cron OR `--re-render` now) goes out in the new aesthetic

You can keep a log on the page itself, like "aesthetic 2026-01 → 2026-03" for future reference.

---

## Scenario 7 — Pause / skip day / reset

**Skip a specific day:** do nothing. The carousel stays in Draft in Notion, you don't post, life goes on.

**Pause everything for a few days:**
- Remote Routine (R1): claude.ai/code → Routines → toggle Schedule Off
- Local Routine (R2): Claude Desktop → Routines → toggle Schedule Off

Reactivate whenever (same toggles On).

**Reset of the day (after a serious error):**
```bash
cd ~/{brand-slug}
rm -rf state/$(date +%Y-%m-%d)
```

Then fire Run now in the Local Routine panel.

---

## Best practices

**Review the Headline Engine every 30 days.** Look at the carousels that performed best — which patterns? Which triggers? Reinforce the page with the lessons.

**Update Quality References.** When one of your carousels comes out excellent, consider adding it as a 3rd example on that page. R2 will use it as an anchor for the next ones.

**Order of adjustment when something goes wrong:**
1. `🖼️ Visual References` (aesthetic)
2. `📚 Editorial Manual` (copy)
3. `📐 Quality References` (quality standard)
4. Operational pages
5. **Last:** the Routine prompt

The solution is almost never to touch the Routine prompt. The system was built to be configured via Notion.

**Performance tracking.** After posting, go back to Notion and fill in `Performance` (Excellent/Average/Poor) on the entry. In 1 month you'll have internal data to calibrate criteria.

**State backup.** The `state/` directory grows. Keep the last 90 days locally, archive the rest to Drive:
```bash
# Run manually every quarter:
cd ~/{brand-slug}/state
find . -maxdepth 1 -type d -mtime +90 -exec tar -czf {}.tar.gz {} \; -exec rm -rf {} \;
# Upload the .tar.gz files to Drive via MCP or web app
```

**Routine prompt backup.** When you edit the prompt in the panel, copy it to `~/{brand-slug}/r2-routine-prompt.txt`. If the app loses the config, you restore it by pasting.

---

## Commands cheat-sheet

```text
# Day-to-day (in the Local Routine panel)
[Run now] → enter (no message)         = runs normally
[Run now] → "I want a carousel about X" = manual pitch with research
[Run now] → "--topic=X"                 = manual pitch with research
[Run now] → "--re-render"               = visual-only re-render
[Run now] → "--news=N"                  = news override
[Run now] → "--only-slide=N"            = regen specific slide

# Conversational in the active session
> --re-render
> regenerate only slide 5
> show the day's narrativa.json

# Local debug (terminal outside Claude Desktop)
cat ~/{brand-slug}/state/$(date +%Y-%m-%d)/log.txt      # logs
cat ~/{brand-slug}/state/$(date +%Y-%m-%d)/narrativa.json  # approved narrative architecture
cat ~/{brand-slug}/state/$(date +%Y-%m-%d)/visual-brief.txt  # visual briefing

# Routines (Claude Desktop panel)
Routines → list                                  # see the 2 routines + status
Routines → [routine] → Run now                   # fire now
Routines → [routine] → Schedule toggle           # pause/resume
Routines → [routine] → Edit prompt               # adjust instructions

# claude CLI (conversation outside the Routine)
cd ~/{brand-slug}
claude
> [natural language command]
```

---

## When to ask the agent for help vs. go directly into the Routine

**Use the Routine directly (Run now + flag) when:**
- You want to run an exact, known command (`--re-render`, `--news=12`)
- You want to run outside the cron schedule

**Use the conversational session (message after Run now) when:**
- You want to regenerate a specific slide with a custom instruction
- You want to adjust a Notion page without opening Notion
- You want to understand why something went wrong (ask a question in the session)

**Use the claude CLI (`claude` in the terminal) when:**
- You're not on Claude Desktop (on the phone you can use it via web)
- You want to do maintenance / debug the local structure
- You want reset, archive, etc.
