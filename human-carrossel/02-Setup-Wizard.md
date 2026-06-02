# 02 — Setup Wizard

> **Not a Notion page.** This is the script that the **setup agent (Claude Code CLI)** runs in the first interaction to collect brand identity before creating the structure.

---

## When the wizard runs

First run of the agent, in the terminal:

```bash
cd ~/{temporary-brand-slug}
claude
```

First message you send: `let's start`.

The agent recognizes that `01-Brand-Identity.md` is not filled in this session, and fires the wizard.

---

## The 11 wizard questions

The agent asks ONE question at a time, waits for an answer, and moves on. It does not dump all 11 at once.

### 1. Brand name

```
What is the full name of the brand? (it will be shown on the cover slide and on slide 9)
Example: Human Academy
```

→ becomes `brand_name`

### 2. Instagram handle

```
What is the @handle on Instagram?
Example: @humanacademy
```

→ becomes `brand_handle` (with the @)
→ derives `brand_slug` (no @, lowercase, hyphen) for the local path

### 3. Primary color

```
What is the brand's primary color? (hex)
Default: #EC5E26 (warm orange)
```

→ becomes `brand_color_primary`

### 4. Custom dark color (optional)

```
Do you want a custom dark background color? (hex, or Enter to use default)
Default: #1B1411 (warm-dark)
```

→ becomes `brand_color_dark`

### 5. Custom light color (optional)

```
Do you want a custom light background color? (hex, or Enter to use default)
Default: #F1ECE3 (warm-cream)
```

→ becomes `brand_color_light`

### 6. Subject/niche

```
What is the brand's subject/niche in one sentence?
Examples:
  - "AI for creatives"
  - "Fixed income for retail investors"
  - "Product design trends"
```

→ becomes `brand_subject`
→ also used to **automatically suggest sources** (cf. Part 6.5 of SETUP)

### 7. How to address the audience

```
How do you refer to your audience? (short term)
Examples: students, readers, investors, designers
```

→ becomes `brand_audience_term`

### 8. Editorial reference outlet

```
Which news outlet is a tone reference for you?
(the system will anchor itself in it for the editorial standard)
Examples:
  - Folha de S.Paulo (BR mainstream)
  - JOTA (BR legal/political)
  - Bloomberg Brasil (finance)
  - Pirate Wires (counterculture tech)
  - Stratechery (tech strategy)
```

→ becomes `brand_voice_anchor`

### 9. R1 schedule

```
When should R1 (news fetching) run?
Default: 9, 13, 17 (morning/lunch/end of afternoon)
Format: hours separated by commas (cron hours)
```

→ becomes `cron_r1_hours`

### 10. R2 schedule

```
What time should R2 (carousel generation) run in the morning?
Default: 08:00
```

→ becomes `cron_r2_time`

### 11. Brand logo

```
Do you want to use the brand/personal logo on the carousels?
(the logo appears small on the cover and large on the final slide — middle slides have no logo)

(y) Yes, I'll attach a PNG later (in Notion, Brand Identity page)
(n) No, use typographic lockup with the brand name
```

→ becomes `brand_has_logo` (true/false)

If you answered yes, the agent says:
```
Cool. After creating the structure in Notion, open the 🏷️ Brand Identity page
and drag the logo PNG into the "Brand logo" section. The next R2 run
will pick it up.

Recommendation: PNG with transparent background, minimum 800x800px, clean square
or rectangular format. You can swap it any time by replacing the attachment.
```

→ You can change it later by toggling `brand_has_logo` in the Brand Identity page table, or by attaching/removing the PNG. **No need to touch code.**

---

## Final confirmation

After the 11 answers, the agent shows a summary:

```
Confirm this identity?

  brand_name:           Human Academy
  brand_handle:         @humanacademy
  brand_slug:           human-academy
  brand_color_primary:  #EC5E26
  brand_color_dark:     #1B1411 (default)
  brand_color_light:    #F1ECE3 (default)
  brand_subject:        AI for creatives
  brand_audience_term:  students
  brand_voice_anchor:   Folha de S.Paulo
  cron_r1_hours:        9,13,17
  cron_r2_time:         08:00
  brand_has_logo:       true (you attach the PNG later)

(y) Yes, create the structure
(n) No, redo
(e) Edit a specific variable
```

When you confirm, the agent:

1. Creates the `~/human-academy/` folder on Mac (or `C:\Users\your-user\human-academy\` on Windows)
2. Moves the 17 `.md` files to `~/human-academy/docs/`
3. Creates `~/human-academy/.brand.json` with the dictionary above
4. Creates `~/human-academy/.claude/settings.json` with the permission allowlist (so the R2 Routine runs without asking for confirmation — see `13-R2-Routine-Local.md`)
5. Asks for the **Notion Integration Token**
6. Asks for the **slug of the main Notion page** (which you created blank) or creates it via API
7. Creates the structure in Notion following the **error-proof procedure** in `03-Notion-template.md` (2 databases + 10 sub-pages)
8. Populates `🏷️ Brand Identity` with the confirmed variables
9. Populates the other 9 pages with the contents of the `.md`s, interpolating all variables
10. Creates `🔐 Configuration` with the Higgsfield CLI checklist and validates `higgsfield account status`
11. **Tests the connectors** Notion + Google Drive (cf. `03-Notion-template.md`, "Connector verification")
12. Saves `~/human-academy/notion-ids.json` with all IDs
13. **Guides you through creating the 2 Routines in the chat**, one Routine at a time — each delivered in a single message, with all fields (see section below) — including leaving R2's permission mode on automatic

Total wizard time: **~5 min of conversation + ~30s of execution** + 2 min creating the Routines.

---

## How the agent delivers the Routine creation

> **Hard rule for the setup agent: DO NOT create an `.md` file for the user to open.** Everything goes **directly in the chat**, in copyable blocks. **One Routine at a time** (R1 first, R2 next), but **all fields of each Routine at once** — in a single message. An `.md` file breaks the flow; drip-feeding one field at a time and waiting for "ok" too — the user wants to see the entire Routine at once, copy everything and paste.

The agent follows this sequence:

### First: R1 — News Scout (Remote Routine)

The agent sends **a single message** with ALL R1 fields, each in its own copyable block, in this order:

1. Opening instruction: Claude Desktop → Routines → New routine → type **Remote**
2. **Name** (copyable block)
3. **Connectors** to enable
4. **Tools** to enable
5. **Permissions** (automatic mode)
6. **Schedule** (cron)
7. **Full prompt** (a single large copyable block)

All in one message. The user fills out the entire Routine, runs a test "Run now", and confirms → the agent moves on to R2.

### Then: R2 — Carousel Creator (Local Routine)

Same logic — **a single message with all fields** of R2:

1. Opening instruction: New routine → type **Local**
2. **Name**
3. **Working folder**
4. **Connectors** and **Tools**
5. **Permissions** (automatic mode)
6. **Schedule** (cron)
7. **Full prompt**

### Why one Routine at a time, but all fields together

- **All fields together:** the user copies and pastes the entire Routine without waiting for the next field. Faster, less back-and-forth.
- **One Routine at a time:** configure R1 fully, test, **see it work** — gain confidence. Only then move to R2, without mixing.
- Copyable blocks in chat are easier to use than opening a file.
- If something goes wrong, the user asks — conversational flow, but without the friction of confirming field by field.

The full Routine prompts are in `12-R1-News-Scout.md` and `13-R2-Routine-Local.md` — the agent reads from there and pastes them into the chat (interpolating `{brand_*}`).

---

## Sources wizard (Part 6.5 of SETUP)

Right after the identity wizard, the agent runs a **mini-wizard for source suggestion** based on `brand_subject`:

```
I'll suggest news sources for the "AI for creatives" niche.
[runs web search for: "best ai news sources", "ai newsletter creative", etc.]

I found 14 potential sources. I'll group them by priority:

HIGH PRIORITY
1. The Verge (AI vertical) — EN, scrape
2. TechCrunch AI — EN, RSS
3. ...

MEDIUM PRIORITY
...

LOW PRIORITY / NICHE
...

Want them all? Or edit the list? (all / edit / none)
```

You confirm/edit. The list goes to the `📋 News Sources` page in structured table format.

---

## Wizard reset

If you got an answer wrong and want to reconfigure:

```bash
cd ~/{brand-slug}
claude
> reset brand identity
```

The agent deletes `.brand.json` and runs the wizard again.

---

## Agent sub-commands after the wizard

After the initial configuration, the conversational agent (claude CLI in the local terminal) recognizes day-to-day commands:

```bash
cd ~/{brand-slug}
claude
> add source: <URL>                  # adds to 📋 Sources
> change primary color to #2A2E45    # edits 🏷️ Brand Identity
> rebuild brand                      # re-interpolates all pages with updated variables
> diagnose last run                  # reads state/$TODAY/log.txt and investigates
```

R2's day-to-day commands no longer need the claude CLI — they go directly in the **Local Routine** panel in Claude Desktop (Run now + optional flag):

```text
[Routine] → Run now                          # runs normally
[Routine] → Run now → "--re-render"          # re-render visual only
[Routine] → Run now → "--news=12"            # news override
[Routine] → Run now → "--only-slide=5"       # regen specific slide
```

The CLI agent's conversational commands live in `PROJECT-INSTRUCTIONS.md` (generated at setup).
