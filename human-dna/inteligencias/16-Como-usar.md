# 16 — How to use day-to-day

Eight real usage scenarios once everything is running.

---

## Scenario 1 — Produce a compliant asset following the DNA

Situation: you need a new piece (post, email, CTA copy, etc.). You want it to come out "with the brand's tone" without having to review 5 times.

**Flow:**

1. Open Claude Desktop → Routines → `{brand_name} — DNA Routine` → **Run now**
2. First message:
   ```
   generate: Welcome email for a new customer who bought product X.
   Tone: more intimate editorial. Includes link to the quickstart.
   ```
3. R2 enters GENERATE MODE:
   - Reads DNA (voice, audience, behavior, anti-patterns)
   - Reads email references in the `📚 Reference Library`
   - Builds enriched brief
   - Generates 2-3 variations
   - Self-audits each one (Compliance Score)
   - Delivers the best + second option

4. You review the output in ~5 min, copy, send

Total time: **8-15 min** (vs. 1-2h writing from scratch)

---

## Scenario 2 — Audit an existing asset (your own or external)

Situation: you produced a post and you're not sure if it "sounds like us". Or you want to understand why that competitor's post looks good.

**Flow:**

1. Run now → first message:
   ```
   audit: [paste the full post text]
   ```
   or
   ```
   audit: https://instagram.com/p/XXXXX/
   ```

2. R2 enters AUDIT MODE:
   - Reads DNA (voice, visual, audience, anti-patterns)
   - Scores 4 dimensions (0-10)
   - Prose diagnosis
   - Rewrite suggestion (if applicable)

3. Output in ~3 min:
   ```
   AUDIT COMPLETE

   Total score: 7.2/10
   ├── Voice: 8.5/10
   ├── Visual: 6.0/10  ← problem
   ├── Persona: 8.0/10
   └── Anti-patterns: 6.5/10  ← problem
   
   Top 3 issues:
   1. Image with purple AI gradient — visual anti-pattern
   2. CTA "comment here!" with no object — verbal anti-pattern
   3. 4 emojis in the caption — emoji policy exceeded
   
   ⚠️ SUGGESTED ADJUSTMENTS — see suggestions.md
   ```

4. You open `suggestions.md` in the working folder, see the proposed rewrite

---

## Scenario 3 — Evolution mini-discovery (DNA needs an update)

Situation: the brand pivoted product, or the audience matured, or the aesthetic aged. DNA needs refresh.

**Flow:**

1. Run now → first message: `evolve`

2. R2 asks the reason:
   ```
   Reason for the evolution?
   (a) Strategic pivot
   (b) Visual refresh  
   (c) New audience
   (d) Post-crisis
   (e) Performance
   (f) Other
   ```

3. You choose — R2 runs **8 focused questions** on the aspect

4. R2 presents proposed diff:
   ```
   DNA EVOLUTION PROPOSAL

   Affected pages: 🧬 DNA Master, 🎨 Visual System, 📚 Reference Library

   Proposed changes:

   🧬 DNA Master:
   - "brand_color_primary: #EC5E26"
   + "brand_color_primary: #2A2E45"

   🎨 Visual System (canonical palette):
   - all references to #EC5E26 replaced with #2A2E45
   - derived tones recalculated

   📚 Reference Library:
   - Anti-references added: "warm/orange 2010s aesthetic"
   - Refs A-04, A-12, A-23 marked as "archive" (aged)

   Reason: Visual refresh — audience matured (average age went up 8 years),
   warm-orange aesthetic is being read as "startup-y" by the enterprise profile.

   Apply? (y) Yes / (e) Edit / (c) Cancel
   ```

5. You confirm → R2 applies on all Notion pages + updates `.brand.json` + creates pre-change snapshot

6. **Next execution of any agent** (R2 Carousel, future agents) already reads the updated DNA

Total time: **15-30 min**

---

## Scenario 4 — Briefing an external vendor (freelance designer, agency)

Situation: you're going to hire a designer for a one-off project. You want the delivery to arrive aligned with the DNA.

**Flow:**

1. Access in Notion: `🧬 DNA Master`, `🎨 Visual System`, `📚 Reference Library`, `🚫 Anti-Patterns`

2. Share **the 4 pages** with the vendor (Notion allows sharing specific pages)

3. Attach:
   - PDF with canonical variables (export of `🧬 DNA Master`)
   - ZIP with 10-15 approved references (export of `📚 Reference Library`, Section A)
   - List of visual anti-patterns (export of `🚫 Anti-Patterns`, Dimension 1)

4. Project brief includes simple contract:
   > "Every delivery goes through compliance check via R2 of the DNA Routine. Score < 7 on any dimension = revision at no extra cost. Adjustments included in scope until score ≥ 8."

5. When vendor delivers, you run AUDIT MODE on the asset. Score >= 8 → approve; < 8 → return with structured diagnosis.

> Advantage: objective feedback, not subjective "I didn't like it". Designer quickly understands what to adjust.

---

## Scenario 5 — Onboarding a new team member

Situation: someone new joined (designer, copy, social, support). You want them producing within the DNA from the first week.

**Flow (extracted from `🔍 Discovery Protocol`, section "Onboarding"):**

### Day 1 (~75 min reading)
- 🧬 DNA Master (15 min)
- 🎯 Brand Strategy (15 min)
- 🗣️ Voice & Tone (20 min)
- 🚫 Anti-Patterns (15 min)
- 📐 Pillars & Taboos (10 min)

### Days 2-5 (reads remaining pages according to role)
- Designer → 🎨 Visual System + 📸 Photography Direction + 🖼️ Image Generation Engine
- Copy → 🗣️ Voice & Tone + 📚 Reference Library
- Social manager → 🤝 Brand Behavior + 📚 Reference Library
- Support → 🤝 Brand Behavior + 👥 Audience DNA

### Days 6-7 (practical exercise)
- Takes 3 recent assets → audits using R2 (audit mode)
- Compares own score with history
- Presents to the team: what they learned, what they questioned, what they would suggest changing

### Day 30 (own mini-discovery)
- Runs 8 personal questions: what would you change in the DNA based on what you saw in the 30 days?
- Presents suggestions — team decides what goes into the next update

---

## Scenario 6 — Quarterly competitive analysis

Situation: every 90 days, you want to evaluate what competitors did, identify trends, adjust differentiation.

**Flow:**

1. R1 (Brand Scout) is already collecting monthly snapshots of the monitored competitors (defined in Discovery)

2. At the end of the quarter, open Claude CLI:
   ```bash
   cd ~/{brand-slug}
   claude
   > quarterly competitive analysis
   ```

3. Agent compiles:
   - Snapshots of the 3 competitors (3 months × 3 = 9 snapshots)
   - Visual changes observed
   - Tonal pivot observed
   - New launches
   - White space (what no one is doing)

4. Output: document of 800-1200 words with tables, saved to Drive `{brand_slug}/Competitive Analyses/{YYYY-Q[N]}.md`

5. You read in quarterly strategy meeting. Decisions may become `evolve` on the DNA.

---

## Scenario 7 — Run complete annual discovery (DNA refresh)

Situation: 1 year has passed. Brand has evolved. DNA needs a systematic review.

**Flow:**

1. Create a complete snapshot of the current DNA (safety):
   ```bash
   cd ~/{brand-slug}
   claude
   > snapshot DNA quarterly-Q[N]-YYYY
   ```

2. Run the complete wizard:
   ```bash
   claude
   > run complete discovery (annual review)
   ```

3. Agent enters wizard mode, but **brings your previous answers as hypotheses alongside each question** — you confirm, refine or refute. The 52 questions in ~30 min.

4. After final confirmation:
   - Creates complete diff (DNA before vs. after)
   - Creates labeled snapshot: `DNA Q[N]-{YYYY} — pre-annual-refresh`
   - Applies all changes in batch

5. Internal communication (optional):
   - Agent generates changelog "what changed in the DNA in this annual refresh"
   - Team reads
   - They update practices accordingly

---

## Scenario 8 — Parallel generation of the same brief in N variations

Situation: you need to test 4 different versions of an ad. Same brief, different approaches.

**Flow:**

1. Run now → first message:
   ```
   generate: 4 variations of Meta ad copy for product X.
   Each one with a different hook:
   - V1: data-anchored hook
   - V2: rhetorical question hook  
   - V3: case-anchored hook
   - V4: objection-anchored hook
   Constraints: up to 125 chars in the headline, up to 90 in the body, CTA "I want to know more".
   ```

2. R2 enters GENERATE MODE:
   - Brief is processed (1 brief, 4 outputs)
   - Each variation goes through auto-audit
   - Compares scores and flags which one is more adherent to the DNA
   - Delivers 4 outputs + ranking

3. You run the 4 in an A/B test, then mark the winner in Notion (Performance: Excellent / Medium / Poor)

4. R2 accumulates this learning — in future similar generations, weights the hook that historically performed

---

## Best practices

### Review `🚫 Anti-Patterns` monthly

R2 brings a log of the top 5 anti-patterns most detected in the last 30 days. Team evaluates if it needs reinforcing (train who produces) or removing (anti-pattern is no longer an issue).

### Update `📚 Reference Library` weekly

Curate pending items collected by R1 (~20 min/week). Living bench > frozen brand book.

### Quarterly snapshot of the entire DNA

R2 creates automatically in `{brand_slug}/DNA-Snapshots/{YYYY-MM-DD}/` on Drive. Works as history ("how the DNA was in Q1 vs Q3") and as backup.

### Visual evolution history

Every 6 months, take a visual snap of the feed (screenshot of the last 30 posts in a 5×6 grid). Paste in the "Visual evolution history" section of the `📚 Reference Library`. Timeline of the visual identity.

### Performance tracking

Every published piece → updates Performance in `🎯 Assets` (Excellent/Medium/Poor). In 3-6 months, you have internal data to calibrate:
- Which pillars perform better
- Which hooks work more
- Which aesthetic connects more
- Which tone converts more

R2 uses this data in future generations.

### Order of adjustment when something comes out poorly

1. `📚 Reference Library` (aesthetic)
2. `🗣️ Voice & Tone` (copy)
3. `🚫 Anti-Patterns` (filters)
4. `🤝 Brand Behavior` (microcopy)
5. **Last:** `🧬 DNA Master` (canonical variables)

The solution is almost never to touch the canonical variables. The system was made to be configured by the depth levels, not by the top.

### Backup of the Routines prompts

When you edit the prompt in the panel, copy it to `~/{brand-slug}/r1-routine-prompt.txt` and `~/{brand-slug}/r2-routine-prompt.txt`. If the app loses the config, you restore by pasting.

---

## Commands cheat-sheet

```text
# Day-to-day (in the Local Routine panel — DNA Routine)
[Run now] → enter (no message)                 = BRIEF MODE (lists jobs)
[Run now] → "audit:<URL or text>"              = AUDIT MODE
[Run now] → "generate:<brief>"                 = GENERATE MODE
[Run now] → "evolve"                           = EVOLVE MODE

# Conversational in the active session
> audit: <new asset>
> generate: <new brief>
> what's our central editorial principle?
> what's our visual anti-pattern #2?
> show approved visual refs

# Debug / local consult (terminal outside Claude Desktop)
cat ~/{brand-slug}/.dna.json | jq .          # full snapshot
cat ~/{brand-slug}/state/$(date +%Y-%m-%d)/log.txt
ls ~/{brand-slug}/state/$(date +%Y-%m-%d)/briefs/
ls ~/{brand-slug}/state/$(date +%Y-%m-%d)/audits/

# Routines (Claude Desktop panel)
Routines → list                                  # 2 routines + status
Routines → DNA Routine → Run now                 # trigger now
Routines → Brand Scout → Schedule toggle         # pause/resume collection
Routines → [routine] → Edit prompt               # adjust instructions

# CLI agent sub-commands
cd ~/{brand-slug}
claude
> rebuild DNA                                  # re-sync .dna.json with Notion
> snapshot DNA                                 # manual quarterly snapshot
> diff DNA vs last snapshot                    # shows what changed
> quarterly competitive analysis
> run complete discovery (annual review)
```

---

## When to ask for the agent's help vs go directly to the Routine

**Use the Routine directly (Run now + flag) when:**
- You know exactly what you want (audit, generate, evolve)
- Brief is clear

**Use the conversational session (message after Run now) when:**
- Want to iterate (generated a piece, want to adjust a small part)
- Want to understand why something came out in a specific way

**Use the claude CLI (`claude` in the terminal) when:**
- Not on Claude Desktop (on mobile you can use it via web)
- Want to do maintenance / debug of the DNA
- Want to rebuild, snapshot, complex analysis
- Want to run annual review

---

## Suggested cadence

| Action | Frequency | Who does it | Time |
|---|---|---|---|
| Audit piece before publishing | Every piece | Whoever produces | 3-5 min |
| Curate pending items from Reference Library | Weekly | Designer / founder | 20 min |
| Review top detected anti-patterns | Monthly | Team | 30 min |
| Competitive analysis | Quarterly | Strategy | 1h |
| Visual feed snapshot | Semi-annual | Designer | 15 min |
| Complete annual discovery (DNA refresh) | Annual | Team + founder | 2-3h |
| Crisis playbook drill (simulation) | Annual | Team + founder | 1h |
