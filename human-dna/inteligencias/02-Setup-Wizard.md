# 02 — Setup Wizard

> **Not a Notion page.** This is the script the **setup agent (Claude Code CLI)** executes on the first interaction to collect the brand DNA in 7 discovery phases, before creating the structure in Notion.
>
> The DNA wizard is deeper than the Carrossel one — it's not 11 questions, it's **52 questions in 7 phases**. Runs in ~30-45 min. The result is a DNA proper, not a registration form.

---

## When the wizard runs

First execution of the agent, in the terminal:

```bash
cd ~/{brand-slug-temporary}
claude
```

The first message you send can be anything — `hi`, `start`, `?`. The Maestro (defined in `CLAUDE.md`) recognizes that there's no `.dna.json` in the working folder and opens a conversation.

> **Important:** the Maestro does NOT dump "7 phases, 52 questions, 30-45 min" in the first message. These numbers are internal operational details, not welcome content. The person enters the conversation answering light questions one at a time (the first is just "what is your brand called?"), and the notion of "process size" only appears if she asks.
>
> If the person needs to pause at any moment, she just says ("I need to stop now", "I'll continue tomorrow"). The agent saves progress in `~/{brand-slug-temporary}/.discovery-progress.json` and resumes where it stopped the next time she comes back.

---

## The 4 discovery modes

The wizard offers 4 modes with increasing depth. You choose at the start.

| Mode | Time | When to use |
|---|---|---|
| **Lean** (12 questions) | ~10 min | New brand without existing material, or quick test. Output: raw DNA, sufficient to start |
| **Standard** (32 questions) | ~25 min | Brand in formation, with some clear intuition. Output: solid DNA for production |
| **Pro** (52 questions) | ~45 min | Operational brand wanting to formalize DNA. Output: complete DNA, branding studio level |
| **Audit-first** (Pro + audit) | ~75-120 min | Operational brand with existing material (site, Instagram, portfolio, blog, decks, posts, competitors, press). Agent recursively collects links, analyzes material first, returns "observed DNA", you confront with "declared DNA" in the 52 questions |

> **Recommendation:** if you have public brand material, go with **Audit-first**. The contrast between "what I think we are" (declared) and "what it appears to be" (observed) is where the real DNA appears.
>
> **Hard rule:** when the user chooses Audit-first, the Maestro can't accept a shallow audit with 1 site and 1 Instagram if the brand has more public traces or private materials the user can send. It must ask for a broad reference package, organize everything by category, ask in a human way if there's anything else and only advance when the person says she's finished sending all the references.

---

## Phase 0 — Human intake of references (mandatory in Audit-first)

Before the 7 phases, the Maestro opens a deep reference collection. The objective is to assemble a real map of the public presence and internal materials of the brand/campaign before interpreting anything.

### How to ask

The Maestro asks for everything the person can send in a broad message, without turning the beginning into a bureaucratic interrogation. The person can send a mixed package; the Maestro organizes afterwards.

Mandatory initial question:

```
Before building the DNA, I want to study the brand as it really exists.
Send me everything you have and can share: site, Instagram, LinkedIn, TikTok,
YouTube, portfolio, blog, newsletter, landing pages, PDFs, decks, brand manual,
photos, videos, VFX, mockups, screenshots, references, anti-references, cases,
competitors, interviews, press, founder/team links and any file that
helps understand the language.

You can send everything mixed. I organize from here.
```

If the person sends images that contain text, tables, lists or examples of structure, the Maestro must read the content of these images. They may be briefing, checklist or DNA scope. Don't treat automatically as aesthetic reference.

After each batch received, the Maestro saves/organizes and asks:

```
I received and organized this batch. Is there anything else you want to send?
Could be photo, video, PDF, VFX, selfie, screenshot, link, folder, reference, anti-reference,
mockup, old ad, presentation or any loose material.

When you finish, tell me exactly: "I finished sending all the references".
```

The Maestro repeats this loop until the user declares they're done. If the user says only "I think that's it", "I don't remember", "for now that's it" or something ambiguous, the Maestro confirms carefully:

```
Perfect. Before I close the inventory: can I consider that you've finished sending
all the references or do you still want to look for more?
```

Only advances when the answer is equivalent to "I finished sending all the references".

### Visible extraction contract

When starting a DNA, before the deep analysis, the Maestro must clearly show what it will extract from the references and the brand. This serves to align expectations and show the real effort of the work.

Mandatory message after receiving the first package or before closing the inventory:

```markdown
I'll extract the brand in layers:

- References: brands, directors/photographers, design/editorial, cinema, culture, competitors, anti-references and close visual worlds
- Site: texts, internal pages, narrative, CTAs, images, structure, promise, proof, objections, conversion and behavior
- Instagram: up to 50 recent posts, grid, captions, Reels, highlights, themes, CTAs, visual, photography, language and behavior
- Visual: logo, photos, typography, palette, composition, light, shadow, projection, texture, photography, mockups, icons, illustrations, grid, margins and breathing
- Voice: general tone, rhythm, vocabulary, words to avoid, humor, positioning, examples and limits
- Content: themes, formats, proofs, arguments, stories, promises, repertoire and editorial patterns
- Application: rules for marketing, social, ads, landing pages, presentations and future pieces

While I analyze, I'll return findings in blocks so you can see the reasoning path.
```

During long analyses, the Maestro doesn't stay silent. It must bring short updates: what it has already opened, what it has already extracted, how many images/texts were analyzed, what patterns appeared and what's still left to study.

If there's Instagram, the progress update needs to mention the collection: how many posts were requested, how many were captured, if captions were read, if media was downloaded, if there was a block and what fallback will be used. The expected standard is to attempt 50 recent posts; less than that requires justification.

Categories the Maestro must organize automatically:

1. **Own links** — site, internal pages, social networks, portfolio, blog, newsletter, landing pages
2. **Visual files** — photos, frames, stills, screenshots, moodboards, mockups, logos, palettes, fonts
3. **Video and motion** — videos, reels, VFX, animations, motion references, selfie videos
4. **Documents** — PDFs, decks, manuals, proposals, press kit, media kit, strategic docs
5. **Texts and voice** — captions, emails, manifestos, articles, scripts, posts, sales messages
6. **Competitors** — brands that dispute the same attention/purchase
7. **Aspirational references** — brands, campaigns, artists, editorials and systems that raise the bar
8. **Anti-references** — everything the brand doesn't want to look like

### Maturity by profile type

The Maestro must begin the reading by understanding whether the project is a company, personal brand, influencer/creator, artist, specialist, founder-led, community, auteur product or hybrid.

This classification isn't bureaucracy. It changes what needs to be extracted.

For personal profiles, creators and influencers, ask for and analyze:

- Instagram, TikTok, YouTube, LinkedIn, newsletter, podcast, interviews, lives, talks, collabs and press;
- posts with face, speech, backstage, routine, opinion, humor, controversy, authority, vulnerability and sales;
- profile photos, selfies, selfie videos, recurring poses, expressions, wardrobe, setting, objects and places;
- recurring sentences, catchphrases, slang, profanity, pauses, speech rhythm, way of responding to audience and exposure limits;
- relationship with followers, community, fans, students, clients, partner brands, critics and haters;
- current moment: growing audience, repositioning, launching product, selling service, professionalizing image, separating person from company or assuming a more public persona.

For companies, ask for and analyze product, service, category, offer, site, proof, design system, support, culture, competitors and institutional behavior.

For hybrids, separate:

- DNA of the person;
- DNA of the brand/company;
- points where the two mix;
- points where they need to stay separate to avoid noise, excessive founder dependency or loss of authenticity.

The final DNA must sound appropriate to the model. Personal brand should not become corporate report. Company should not become intimate diary. Influencer should not be treated like cold e-commerce. Founder-led should not erase the founder when he is the main asset of trust.

### When the brand has no public presence yet

If there's no site, Instagram, portfolio, blog, store, published campaign or sufficient files, the Maestro must explain that the DNA is still possible, but the base will be built by guided interview and alternative materials.

The agent must ask, without sounding like a cold form:

- brands the person admires and why;
- brands the person rejects and why;
- directors, photographers, films, magazines, covers, editorials, artists, songs, objects, places and cultures that help explain the universe;
- loose photos of the product, service, founder, space, team, packaging, backstage or process;
- videos, selfies, VFX, drafts, PDFs, presentations, screenshots, old texts, sales messages and any previous attempt;
- colors that seem right, colors that seem wrong, desired visual sensation, light, texture, composition, rhythm and level of sophistication;
- how the brand speaks, what words it uses, what words don't fit, if there's humor, aggressiveness, profanity, slang, provocation or sweetness;
- where this DNA will be applied: social, ad, landing page, presentation, packaging, video, support, event or proposal.

The objective is to fill the same analysis intentions even without public reference. The absence of a site doesn't authorize a shallow DNA. It requires the Maestro to collect more human context, record gaps and separate three levels in the document: observed, declared by the person and proposed as hypothesis.

### How to save

All material received must be stored in a traceable way inside the project:

```text
referencias/
├── links.md
├── 01-links-proprios/
├── 02-arquivos-visuais/
├── 03-video-motion-vfx/
├── 04-documentos-pdfs-decks/
├── 05-textos-voz/
├── 06-concorrentes/
├── 07-referencias-aspiracionais/
└── 08-anti-referencias/

discovery/
├── link-inventory.md
├── asset-inventory.md
├── link-analysis.md
├── asset-analysis.md
├── dna-observado.md
└── gaps-e-hipoteses.md
```

If the material comes as a link, save in the inventory with URL, category, collection date and note. If it comes as a file, preserve the original file, record name, type, origin, likely use and any technical limitation. Don't rename files destructively; when you need to standardize, copy to a clean name and keep reference to the original.

### Closing criterion

The collection only ends when:

- all received batches have been saved and categorized;
- the Maestro has shown an inventory summary;
- the user has declared they finished sending all references.

Mandatory summary before the analysis:

```
Inventory organized:
- Own links: ...
- Visual files: ...
- Video/motion/VFX: ...
- Documents/PDFs/decks: ...
- Texts/captions/emails: ...
- Competitors: ...
- Aspirational references: ...
- Anti-references: ...

Can I close the inventory and start the deep analysis or is there still more?
```

As soon as the first extraction closes, the Maestro must bring a clear summary to the chat:

```markdown
Initial extraction completed.

- Links/pages studied: ...
- Images found/analyzed: ...
- Logos/symbols found: ...
- Texts and CTAs read: ...
- PDFs/decks/files analyzed: ...
- Visual patterns perceived: ...
- Voice patterns perceived: ...
- Gaps or access limits: ...

Now I'll turn this into interpretation: meaning, practical rule, limit and application.
```

### Analysis depth

After the inventory is closed, the Maestro does autonomous and dense analysis. It must follow relevant internal links to sufficient depth to understand:

- declared value proposition
- explicit promise and implicit promise
- offer architecture
- sales language
- editorial tone
- recurring vocabulary
- frequent themes and avoided themes
- social proof and authority
- visual pattern, palette, typography and grid
- visual usage percentage of each color (dominant, secondary, accent, neutrals)
- color application rules by channel/format
- typographies used, hierarchy, weights, scale and spacing
- existing mockups and application patterns
- existing logo, variations, proportion, breathing, correct use, incorrect use and application context
- use of signatures, seals, watermarks and recurring elements
- margins, breathing, empty spaces, visual density and composition rhythm
- photographic/audiovisual direction
- photography: light, shadow, projection, pose, gesture, product/service, setting, surface, texture, treatment and editorial line
- typography: families found, lettering, weights, contrast, hierarchy, scale, spacing and editorial function
- video language, selfie, VFX, editing, rhythm, motion and transitions
- publishing rhythm
- tension between channels
- gaps, inconsistencies and opportunities
- difference between declared DNA, observed DNA and performed DNA

### Personality without censorship

The Maestro must preserve the brand's real personality. Taboo is no excuse to erase strength, aggressiveness, acidic humor, profanity, provocation, sensuality, confrontation or popular language when this appears in the references.

During the voice analysis, the Maestro must record:

- level of aggressiveness or softness
- presence of profanity, slang, irony, mockery, confrontation, sensuality or brute language
- frequency of these traits
- context in which they appear
- communicative intent: grab attention, create belonging, attack cliché, sell with urgency, provoke enemy, create intimacy or generate shock
- where this strengthens the brand
- where this can generate real platform, legal, commercial or reputational risk

The Maestro should not trade authenticity for neutrality. If there's risk, it records the risk and guides use by context. It doesn't erase the trait.

### Site X-ray (high priority)

When the user sends a site, the Maestro must treat that site as a primary source of the DNA. Site isn't just URL. Site is architecture, narrative, tone of voice, image, rhythm, proof, promise and behavior.

The Maestro must navigate the site with depth, whenever access allows:

- open home, about, product/service, cases, blog/articles, contact, pricing, FAQ, manifesto, landing pages and relevant internal pages
- read all important texts, including titles, subtitles, CTAs, captions, menus, footer, microcopy, buttons, forms and error messages when visible
- understand the order of the narrative: what appears first, what the brand explains next, where it proves, where it sells, where it creates trust
- open and interpret images, illustrations, photos, icons, mockups and embedded videos whenever possible
- interpret images as language, not as decoration: theme, light, framing, color, texture, gesture, atmosphere, metaphor, type of person, setting and intent
- identify how the images reveal tone of voice, way of thinking, behavior and worldview
- map composition patterns: margins, breathing, blocks, grid, rhythm, density, hierarchy and use of empty space
- observe the brand's behavior: how it invites, explains, promises, proves, sells, responds to objections, reduces risk and conducts the visitor
- record pages visited, key texts, key images and hypotheses extracted in `discovery/link-analysis.md`

When the site is rich in images, the Maestro can't stop at one logo and a few screenshots. It must create `discovery/site-visual-inventory.md` with a real visual sweep:

- capture or record all important images from the home and key pages
- include hero images, product photos, photos of people, mockups, icons, illustrations, banners, cases, applications, seals, backgrounds, patterns and video frames when accessible
- analyze at least 12 relevant images when the site has sufficient volume
- in very rich sites, analyze between 20 and 60 images distributed by page type and visual role
- for each image, record origin, page, function, visual description, dominant colors, composition, implicit message and rule it teaches the brand
- if fewer than 12 images are analyzed in a clearly visual site, justify the access limit or revise the extraction

If the site has many pages, the Maestro prioritizes the pages that carry the most identity and decision: home, about, product, cases, manifesto, sales pages and strong editorial content. If it finds relevant internal links during navigation, follow until forming an intimate reading of the system. Doesn't need to track irrelevant or repetitive pages.

### Deep interpretation ladder

The Maestro can't skip from "I read the materials" to "I generated the DNA". It must cross five layers:

1. **Forensic reading** — record what exists: assets, channels, formats, sentences, colors, grid, materials, offers, proofs, repetitions and absences
2. **Critical interpretation** — explain what these signals mean: ambitions, contradictions, clichés, real strengths, fragilities and opportunities
3. **Central idea** — formulate the main tension, the guiding idea, the brand's territory and the editorial point of view
4. **Brand translation** — turn the interpretation into clear rules of voice, visual, palette, typography, composition, photography, motion, behavior and applications
5. **Final documentation** — write the DNA as a clear story, with depth and solid base, without depending on production of new pieces

Each layer must leave a trace in `discovery/` or in `resultado/DNA.md`. If the DNA only describes what the brand already had, it failed. The Maestro needs to interpret, translate, organize and document.

### Logo and visual absorption

When there's a logo, symbol, monogram or visual signature in site, PDF, social network, mockup or sent file, the Maestro must try to extract and save a usable version in `referencias/02-arquivos-visuais/` or record the original path/URL in the inventory.

The logo must enter the `resultado/DNA.pdf` whenever quality allows. If there's no logo, if it's illegible or if the extraction is poor, the flow continues without loss of quality. The Maestro records the limit and uses available name, typography, colors and visual signals.

The single PDF must absorb the brand intensely. Whenever possible, its layout must follow the extracted base:

- typographic style
- main and neutral colors
- rhythm of margins and breathing
- proportion between text and image
- use of empty spaces
- visual density
- presence or absence of lines, frames, grids and blocks
- cover style, section openings and graphic details

The document should not just talk about the brand. It must look like it was born from the brand. Can't look like a markdown exported to PDF. Palette must appear as real color blocks, images must enter in editorial composition with caption and breathing, and sections must have clear visual hierarchy.

### Mandatory interpretation matrix

For each relevant reference/material, the Maestro must answer:

- What is it?
- What does it show?
- What does it reveal without saying?
- What pattern repeats in other materials?
- What reading about the brand does this suggest?
- What practical rule enters the DNA?
- What would be a bad copy of this reference?
- How does this change the way of explaining voice, visual, behavior or positioning?

When the sent material asks for content structure, the Maestro must turn this into clear matrices. The DNA must contain, when applicable:

- **Reference map:** brands, directors/photographers, design/editorial, cinema and culture
- **Voice map:** general tone, rhythm, vocabulary, words/phrases to avoid, humor and positioning
- **Visual map:** palette, aesthetics, composition, light, texture and references
- **Photographic map:** direction, lighting, shadow, projection, pose, product/service, setting, treatment and editorial line
- **Typographic map:** families, lettering, weights, scale, hierarchy, contrast, spacing, function and personality

Each row needs to have extracted reading, meaning, practical rule and limit. It's not enough to repeat guiding questions.

The Maestro can follow relevant internal and external links found on the pages, but should not bypass login, paywall, robots, privacy, closed accounts or any unauthorized material. If something important is behind access, ask for export, screenshot, PDF or summary.

Mandatory output:

- `discovery/link-inventory.md` — categorized list of links and status
- `discovery/asset-inventory.md` — list of received files, type, origin and function
- `discovery/link-analysis.md` — analysis per link/channel
- `discovery/asset-analysis.md` — analysis of photos, videos, PDFs, mockups, VFX and attached materials
- `discovery/dna-observado.md` — strategic, verbal, visual and behavioral synthesis inferred
- `discovery/ideia-central.md` — guiding idea, main tension, brand territory and point of view
- `discovery/matriz-de-interpretacao.md` — reference → meaning → rule → implication table
- `discovery/gaps-e-hipoteses.md` — contradictions, hypotheses and questions that need human validation

---

## The 7 phases of the Pro wizard (52 questions)

> The agent asks ONE question at a time, waits for the response, and continues. Never dumps the whole phase. After each phase, shows a mini-summary and asks "continue / redo / skip".

### PHASE 1 — Basic identity (8 questions)

The most surface layer — canonical variables. It's what the Carrossel also asks, expanded.

1. **Brand name** → `brand_name`
2. **Legal name / corporate name** → `brand_legal_name` (optional, default: same as name)
3. **Main Instagram handle** → `brand_handle` → derives `brand_slug`
4. **Main URL** → `brand_url`
5. **Main communication email** → `brand_email_main`
6. **Brand logo?** → `brand_has_logo` (true/false) + instruction to attach PNG later
7. **In one sentence: what does your brand do?** → seed for `brand_subject`
8. **In one sentence: for whom?** → seed for `brand_audience_term` + persona

### PHASE 2 — Strategy (10 questions)

The "why" layer. What comes out of here becomes `🎯 Brand Strategy` + the anchor variables.

9. **Why does this brand exist? If it closed today, what stops existing in the world?** → purpose
10. **What do you do today, operationally, to fulfill this purpose?** → mission
11. **In 5-10 years, what's the "end state" you pursue?** → vision
12. **Who are the 3 closest competitors?** → competitive map
13. **What do you do that NONE of these competitors does?** → differentiator
14. **What do you NOT do, deliberately, even though you could?** → negative scope
15. **In one counterintuitive sentence: what's the "ah-ha" that moves the brand's pitch?** → key insight
16. **If the audience uses the product and succeeds, what's the emotional outcome? And the functional one?** → central promise
17. **In which market category do you compete? And which would you like to redefine?** → positioning
18. **What's the editorial reference journalism outlet?** → `brand_voice_anchor_editorial`

### PHASE 3 — Audience (8 questions)

The "for whom" layer. Comes out of here for `👥 Audience DNA`.

19. **Describe the ideal primary persona — fictional name, age, profession, family/social context, location**
20. **What decision does this persona make every week that has to do with what you offer?**
21. **What's her functional aspiration?** (what she wants to be able to do)
22. **What's the identity aspiration?** (who she wants to be perceived as)
23. **What's her professional fear?** (what she fears getting wrong)
24. **What's the identity fear?** (what kind of person she fears looking like)
25. **Where does she spend time today? What apps/sites/communities?**
26. **Anti-persona: describe someone you do NOT want to talk to — even if they pay**

### PHASE 4 — Voice and tone (8 questions)

The "how we speak" layer. Comes out of here for `🗣️ Voice & Tone`.

27. **In one sentence: how does the brand speak?** (like "as an editor of Folha who opened an agency") → central editorial principle
28. **4 adjectives of what the brand IS**
29. **4 adjectives of what the brand is NOT**
30. **5 words you use (own jargon, brand words, slang, verbal force or profanity if they're part of the brand)**
31. **5 words you avoid (saturated jargon, others' words, terms that weaken the brand's real personality)**
32. **How do you call the audience? (give 1 approved term and 2 forbidden terms)**
33. **Reference tonal brand (non-journalistic) — who sounds similar to you but in another context?** → `brand_voice_anchor_brand`
34. **Paste 2-3 of your own texts (post, email, caption) that represent the right tone. And 1 text that does NOT represent the tone — that needs to be rewritten**

### PHASE 5 — Visual (10 questions)

The "how it looks" layer. Comes out of here for `🎨 Visual System` + `📸 Photography Direction` + `🖼️ Image Generation Engine`.

35. **Brand primary color (hex)** → `brand_color_primary`
36. **Secondary color (hex, or enter to derive)** → `brand_color_secondary`
37. **Dark background color (hex, or enter for default warm-dark `#1B1411`)** → `brand_color_dark`
38. **Light background color (hex, or enter for default warm-cream `#F1ECE3`)** → `brand_color_light`
39. **Display typographic family (headlines)** — name or "need suggestion" → `brand_font_display`
40. **Body typographic family (paragraphs)** — name or "need suggestion" → `brand_font_body`
41. **Mono typographic family (tags, metadata)** — name or "need suggestion" → `brand_font_mono`
42. **Anchor aesthetic: cite 2-3 publications/studios whose aesthetic you want close to yours** → `brand_aesthetic_anchor`
43. **Preferred photographic direction: of the 7 lighting setups (Golden Hour, Low Key, Spotlight, Chiaroscuro, Cutter Lights, Hard Flash, Silhouette), which are the 2-3 that best represent you?**
44. **Attach 3-5 visual reference images** (the agent asks to drag files into the chat OR to paste URLs)

### PHASE 6 — Behavior (5 questions)

The "how it acts" layer. Comes out of here for `🤝 Brand Behavior`.

45. **On which channels is the brand present today?** (list)
46. **On which are you MOST active? And on which would you like to be more active in the next quarter?**
47. **Who responds to negative DM/email/comment? What's the SLA?**
48. **Crisis playbook: if a negative article/post about the brand comes out, in how much time do you respond? And how (silence, clarification, self-critique)?**
49. **Behavioral calendar: which 3-5 dates of the year are "mandatory" for the brand to touch (Black Friday, brand anniversary, annual launch)? And which 2-3 dates do you deliberately NOT touch (generic Mother's Day, politicized dates)?**

### PHASE 7 — Pillars and taboos (3 questions)

The editorial scope layer. Comes out of here for `🧬 DNA Master` (pillars) and `🚫 Anti-Patterns` (taboos).

50. **List 3-5 content pillars — allowed editorial axes. For each, give 1 sentence of scope + estimate of % of production** → `brand_pillars`
51. **List 3-5 taboo themes — themes you NEVER touch, with reason (ethical, commercial, strategic)** → `brand_taboo_topics`
52. **Give 5 anti-patterns: 1 visual, 1 verbal, 1 behavioral, 1 editorial, 1 commercial — things the brand NEVER does** → seeds for `🚫 Anti-Patterns`

---

## Intermediate confirmation per phase

After each phase, the agent shows the summary:

```
─── PHASE 2 — Strategy — completed ───

Purpose:           We exist so creative Brazilian professionals don't...
Mission:           We build creative AI systems in Portuguese, trained...
Vision:            [answer to question 11]
Competitors:       [answer to question 12]
Differentiator:    [answer to question 13]
Negative scope:    [answer to question 14]
Key insight:       [answer to question 15]
Central promise:   [answer to question 16]
Positioning:       [answer to question 17]
Voice anchor:      [answer to question 18]

(c) Continue to Phase 3 — Audience
(r) Redo some answer from Phase 2
(s) Save progress and continue later
```

---

## Audit-first mode — agent analyzes existing material

If you chose **Audit-first**, the agent runs a phase 0 before Phase 1.

```
I'll start by analyzing the brand's existing material to extract the observed DNA.
Then I confront it with what you answer in the 7 phases.

I'll first assemble a reference inventory. Send me everything you have:
links, site, Instagram, networks, portfolio, blog, newsletter, PDFs, decks, photos,
videos, VFX, mockups, screenshots, texts, competitors, references and anti-references.

You can send mixed. I organize by category. After each batch, I'll ask
if there's anything else. When you say "I finished sending all the references",
I close the inventory, study everything in depth and come back with the "observed DNA".

Estimated time: 30-60 min of autonomous processing after the inventory is closed.
```

The agent runs in background:

1. **Reference inventory** → saves `discovery/link-inventory.md` and `discovery/asset-inventory.md` with category, origin, type, status, note and priority
2. **Main site X-ray** → navigates internal pages, reads texts, interprets images, understands structure, journey, promise, proof, tone of voice and behavior
3. **Selective deep crawl** → follows relevant internal links (about, product, cases, blog, manifesto, pricing, FAQ, landing pages) until forming intimate reading of the brand
4. **Web fetch of social networks** → analyzes headlines, captions, hashtags, visual format, frequency, themes, engagement peaks when visible
5. **Portfolio/cases analysis** → identifies type of work, demonstrated promise, proof, process, aesthetic and recurrences
6. **Blog/newsletter analysis** → extracts editorial thesis, vocabulary, argumentative cadence, cultural repertoire and authority
7. **Decks/PDFs/emails analysis** → compares institutional, commercial and editorial tone
8. **Photos, videos, VFX and mockups analysis** → extracts visual direction, color, typography, composition, texture, rhythm, application and production patterns
9. **Web search and competitor analysis** → competitive map, category codes, white space and market clichés
10. **References and anti-references analysis** → separates useful aspiration from what would be copy or noise
11. **Central idea** → formulates main tension, guiding idea, brand territory and point of view
12. **Interpretation matrix** → connects reference/material → meaning → rule → implication
13. **Synthesis** → produces "observed DNA" with variables filled in as **traceable hypotheses**

Output: eight documents in the working folder, shown before Phase 1.

- `discovery/link-inventory.md`
- `discovery/asset-inventory.md`
- `discovery/link-analysis.md`
- `discovery/asset-analysis.md`
- `discovery/dna-observado.md`
- `discovery/ideia-central.md`
- `discovery/matriz-de-interpretacao.md`
- `discovery/gaps-e-hipoteses.md`

```
OBSERVED DNA (extracted autonomously):

brand_name (declared on the site): ...
brand_subject (extracted from hero/about): ...
brand_audience_term (extracted from captions): ...
brand_color_primary (extracted from CSS): #...
brand_voice_anchor_editorial (inferred from tone): ...
brand_aesthetic_anchor (inferred from feed visual refs): ...
brand_pillars (inferred from 60 posts): [Pillar A: 35%, Pillar B: 25%, ...]

3 IMPORTANT OBSERVATIONS:
1. Post tone is more technical than the site tone (probable proposition tension)
2. Site primary color (#EC5E26) does NOT appear in the last 60 posts (gap between digital and social)
3. Competitor X covers pillar Y better than you — worth checking if to maintain or yield

LINKS ANALYZED:
- Site: 14 internal pages
- Instagram: last available public posts
- Portfolio/cases: 6 pages
- Blog/newsletter: 11 articles
- Competitors: 5 brands, 23 pages

FILES ANALYZED:
- Photos/stills: 18 files
- Videos/Reels/VFX: 7 files
- PDFs/decks: 3 documents
- Mockups/screenshots: 12 images

GAPS:
- No access to closed emails/newsletter
- Portfolio has visual cases, but little process explanation
- Founder's LinkedIn suggests more authorial tone than the site

When you go to answer the 52 questions, I'll put these hypotheses next to them so 
you can confirm or refute. Ready to start Phase 1?
```

Then it enters Phase 1 normally — but each question comes with the observed hypothesis next to it:

```
Question 7: In one sentence: what does your brand do?

Observed hypothesis (from site/posts): "Creative AI courses and workshops for Brazilians"

Your answer:
```

You confirm or rewrite. **This contrast is where real DNA appears** — frequently what the brand declares is different from what it does.

---

## Final confirmation

After the 7 phases (and the audit if there is one), the agent shows an executive summary:

```
═══ CREATIVE DNA — EXECUTIVE SUMMARY ═══

IDENTITY
  brand_name:         [confirmed name]
  brand_handle:       [confirmed @handle]
  brand_slug:         [derived slug]
  brand_url:          [confirmed URL]
  brand_color_primary: [confirmed #hex]
  brand_has_logo:     [true | false]

STRATEGY
  Purpose:            [condensed answer to question 9]
  Positioning:        [condensed answer to question 17]
  Key insight:        [condensed answer to question 15]

AUDIENCE
  Primary persona:    [fictional name] — short descriptor
  Anti-persona:       [short descriptor]

VOICE
  Principle:          [sentence]
  Is:                 4 adjectives
  Is not:             4 adjectives
  Editorial anchor:   [outlet from question 18]
  Brand anchor:       [brand from question 33]

VISUAL
  Palette:            #... (primary), #... (dark), #... (light)
  Display font:       [name]
  Body font:          [name]
  Aesthetic anchor:   [visual references from question 42]
  Photo setups:       [setups chosen in question 43]

PILLARS (5)
  1. [Pillar 1] — 30%
  2. [Pillar 2] — 25%
  ...

TABOOS (3)
  1. ...
  2. ...
  3. ...

ANTI-PATTERNS (5)
  1. ...
  ...

(y) Yes, create the structure in Notion + activate Routines
(r) Redo specific phase
(e) Edit specific variable
(p) Preview each page before creating
```

When you confirm, the agent:

1. Creates the folder `~/{brand-slug}/` on Mac (or `C:\Users\your-user\{brand-slug}\` on Windows)
2. Moves the 18 `.md` files to `~/{brand-slug}/docs/`
3. Creates `~/{brand-slug}/.brand.json` with the canonical variables
4. Creates `~/{brand-slug}/.dna.json` with the complete DNA snapshot (executive synthesis in JSON)
5. Creates `~/{brand-slug}/.claude/settings.json` with the permissions allowlist
6. Asks for the **Notion Integration Token**
7. Asks for the **main Notion page slug** (which you created blank) or creates via API
8. Creates the Notion structure following the procedure in `03-Notion-template.md` (4 databases + 14 sub-pages)
9. Populates `🧬 DNA Master` with the executive synthesis
10. Populates the 13 other pages with depth derived from the answers (each page is an expansion of the relevant phases)
11. Creates `🔐 Configuração` with Higgsfield CLI checklist and validates `higgsfield account status`
12. **Tests the connectors** Notion + Google Drive
13. Saves `~/{brand-slug}/notion-ids.json` with all the IDs
14. **Guides you through creating the 2 Routines in the chat**, one at a time

Total time: **~30-45 min of discovery + ~60s of setup execution + 3 min creating the Routines**.

---

## How the agent delivers the creation of the Routines

> **Hard rule for the setup agent: DO NOT create a `.md` file for the user to open.** Everything goes **directly into the chat**, in copyable blocks, **one Routine at a time**, waiting for confirmation. Same philosophy as the Carrossel.

The agent follows this sequence:

### First: R1 — Brand Scout (Remote Routine)

```
Let's create Routine 1 (R1 — Brand Scout). Open Claude Desktop → 
Routines → New routine → Remote type.

I'll pass you field by field. Let me know "ok" after each one.
```

Releases, **one at a time, waiting for "ok"**:
1. **Name** (copyable block)
2. **Connectors** to mark
3. **Tools** to mark
4. **Schedule** (cron)
5. **Complete prompt** (one large copyable block)

When the user confirms they created it and ran the "Run now" test → the agent moves to R2.

### Then: R2 — DNA Routine (Local Routine)

```
R1 created. Now Routine 2 (R2 — DNA Routine). 
New routine → Local type.
```
Releases in the chat, one at a time: Name → Working folder → Connectors/Tools → Schedule → Complete prompt.

The complete prompts for the Routines are in `14-R1-Brand-Scout.md` and `15-R2-DNA-Routine-Local.md` — the agent reads from there and pastes in the chat (interpolating `{brand_*}`).

---

## Lean mode (12 questions) — when to use

For a brand still being born or for quick test. The 12 questions are a strategic subset of the 52:

1, 2, 3 (Phase 1, basic identity) +
9, 12, 16, 17 (Phase 2, purpose, competitors, promise, positioning) +
19, 23 (Phase 3, persona + fear) +
27 (Phase 4, editorial principle) +
35, 42 (Phase 5, color + anchor aesthetic) +
50 (Phase 7, pillars)

The DNA generated in Lean mode is **enough to start producing**, but the executive summary of `🧬 DNA Master` comes with `[expand later]` tags in various fields. R2 recognizes these tags and runs mini-discovery when it needs depth in an `[expand later]` field.

Recommendation: run Lean to start, schedule rerun in Standard/Pro mode when you've passed 30 days of production (you'll have observable material of your own to calibrate).

---

## Standard mode (32 questions) — when to use

Subset between Lean and Pro. Skips:
- Phase 2: questions 13, 14 (detailed competitors/negative scope)
- Phase 3: questions 25, 26 (touchpoints, detailed anti-persona)
- Phase 4: questions 33, 34 (non-journalistic tonal reference, text sample)
- Phase 5: questions 36, 41 (secondary color, mono font)
- Phase 6: questions 47, 48 (SLA, crisis playbook)
- Phase 7: questions 51 (detailed taboos — only gets general anti-patterns)

Ideal for **80% of cases**.

---

## Reset / re-run wizard

If you got an answer wrong and want to reconfigure:

```bash
cd ~/{brand-slug}
claude
> reset DNA
```

The agent deletes `.brand.json` + `.dna.json` + `.discovery-progress.json` and runs the wizard again.

To adjust a specific answer without redoing everything:

```bash
> edit answer to question 27 of the DNA
```

Or directly in Notion: edits the relevant page, then runs `> rebuild DNA` in the agent — it re-reads all the pages, regenerates `.dna.json` and propagates interpolations.

---

## Agent sub-commands after the wizard

After the initial setup, the conversational agent (claude CLI in the local terminal) recognizes day-to-day commands:

```bash
cd ~/{brand-slug}
claude
> audit this post: [URL or paste the text]      # runs compliance score
> write welcome email following DNA              # generates compliant output
> what's our visual anti-pattern #2?             # queries DNA
> rebuild DNA                                    # re-syncs .dna.json with Notion
> diff DNA vs last snapshot                      # shows what changed in the DNA
> snapshot DNA                                   # creates quarterly snapshot in Drive
> review DNA (quarterly)                         # runs mini-discovery (8 questions) for refresh
```

R2 day-to-day commands go directly into the **Local Routine** panel in Claude Desktop (Run now + optional flag):

```text
[Routine] → Run now                          # default mode (waits for input)
[Routine] → Run now → "audit:<URL>"          # audit external asset
[Routine] → Run now → "generate:<brief>"     # generate output
[Routine] → Run now → "evolve"               # evolution mini-discovery
```

The conversational commands of the CLI agent live in `PROJECT-INSTRUCTIONS.md` (generated in setup).
