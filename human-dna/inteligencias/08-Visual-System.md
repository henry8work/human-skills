# 08 — Visual System

> **Master document of the visual design and graphic identity discipline.** Written with the authority of a senior art director — PhD in visual design, trained in schools ranging from Ulm to Basel to Cooper Union, with experience in studios like Pentagram, Wolff Olins, Collins, Porto Rocha, Manual, Berger&Föhr, Mucho, and active reference in Vignelli, Müller-Brockmann, Tschichold, Bringhurst, Lupton, Itten, Albers, Rams, Frutiger.
>
> This file is the visual identity reference of the WHOLE system. The Maestro consults it before generating graphic piece, before auditing layout, before proposing visual system. For real image generation, the excerpts go into Higgsfield CLI with Nano Banana 2 (`nano_banana_2`).

---

## Table of contents

0. **Doctrine** — authority and premise
1. **Reference literature** — canonical bibliography
2. **The 12 founding principles**
3. **Consolidated frameworks** (Vignelli Canon, Swiss System, Atomic Design, Design Tokens, Carbon, Material)
4. **Color system** (palette, neutrals, semantics, derivatives, harmony, contrast)
5. **Typographic system** (hierarchy, modular scale, proportions)
6. **Grid and spacing system** (modular, baseline, breakpoints)
7. **Logo and graphic mark** (variants, clear space, anti-use)
8. **Universal components** (cards, buttons, dividers)
9. **Motion** (principles, easings, durations)
10. **What is GOOD vs BAD design** (canonical cases)
11. **What is FAST vs SLOW design** (production efficiency)
12. **What WORKS vs DOESN'T WORK** (effectiveness at scale)
13. **What SELLS vs REPELS** (visual conversion)
14. **What AGES WELL vs DATES FAST**
15. **Exhaustive visual anti-patterns**
16. **Quality criteria** (how to judge work)
17. **When the Maestro should call me** (routing)
18. **Operational checklist**

---

## 0. Doctrine

Design isn't decoration. Design is **applied communication with restriction**. Every visual decision is, ultimately, a decision of hierarchy: what comes first for reading, what comes after, what's left out. Form serves function; and strong function generates lasting form.

A mediocre brand in 2026 is easy to identify: uses Bootstrap template, has hero with blue-purple gradient CTA, stock photography of smiling people, generic Google Fonts typography (Inter or Poppins) without hierarchy, and a palette of 7 colors that no one would distinguish from 10 thousand other brands. A distinct brand in 2026 is equally easy to identify: it has a hard decision made with conviction in each dimension. Usually has LESS, not more. Usually has RULE, not improvisation.

The central canon of modern design (from Bauhaus to Apple to Aesop) is: **restriction frees**. A well-defined system produces more, faster, with more consistency, than improvisation. The most dangerous sentence in a design meeting is "let's make it special this time" — because system is what **defends the brand from each moment of temptation**.

Every decision in this document starts from a premise: **design is a technical discipline with centuries-old foundation**. There are 100 years of theory and practice. Whoever ignores this repertoire repeats the mistakes that the 70s and 80s already corrected.

---

## 1. Reference literature

Every decision in this document is anchored in canonical works. In case of doubt, consult these sources first — they are the court of appeal.

### Theoretical foundations of modern design

- **Massimo Vignelli** — *The Vignelli Canon* (2010, free PDF). Manifesto of responsible design. Fundamental principles in 100 pages.
- **Paul Rand** — *Thoughts on Design* (1947). The beginning of modern American design. Logos of IBM, ABC, UPS, Westinghouse.
- **Josef Müller-Brockmann** — *Grid Systems in Graphic Design* (1981). The bible of the modular Swiss system. Applicable to any medium.
- **Jan Tschichold** — *The New Typography* (1928). Manifesto of modern sans-serif typography, left alignment, functional hierarchy.
- **Karl Gerstner** — *Designing Programmes* (1964). System as program (prior to generative design).
- **Emil Ruder** — *Typographie: A Manual of Design* (1967). Swiss School of Basel.
- **Wolfgang Weingart** — *My Way to Typography* (2000). Post-Swiss, anti-rigidity.

### Typography (mandatory canon)

- **Robert Bringhurst** — *The Elements of Typographic Style* (1992). The bible. Read 1x per year. Portuguese version: *Elementos do Estilo Tipográfico* (Cosac Naify).
- **Ellen Lupton** — *Thinking with Type* (2004). Accessible, contemporary, perfect for beginning.
- **Karen Cheng** — *Designing Type* (2005). Anatomy of the letter.
- **Adrian Frutiger** — *The Type and the Eye* (1998). Memoirs of the creator of Univers, Frutiger, Avenir.
- **Hermann Zapf** — *Manuale Typographicum* (1968). On Zapfino, Optima, Palatino.
- **Erik Spiekermann** — *Stop Stealing Sheep & Find Out How Type Works* (1993). Typography for non-designers.
- **Peter Bilak** (Typotheque) — online essays on contemporary typography.

### Color

- **Johannes Itten** — *The Art of Color* (1961). Fundamental Bauhaus course. Color wheel, harmonies, contrasts.
- **Josef Albers** — *Interaction of Color* (1963). Color isn't absolute — it's relational.
- **David Hornung** — *Color: A Workshop for Artists and Designers* (2005). Contemporary practical application.
- **Patrick Baty** — *Anatomy of Colour* (2017). Cultural history of colors.

### Brand identity and visual system

- **Wally Olins** — *On Brand* (2003) and *Brand New: The Shape of Brands to Come* (2014). Strategy + identity.
- **Marty Neumeier** — *The Brand Gap* (2003). Connection between strategy and expression.
- **Michael Bierut** — *How to* (2015). Pentagram cases explained by himself.
- **Steven Heller & Veronique Vienne** — *100 Ideas that Changed Graphic Design* (2012).
- **Per Mollerup** — *Marks of Excellence: The Function and Variety of Trademarks* (1997). Definitive study of logos.
- **Kevin Murphy & Brian Collins** (Collins) — essays and talks.
- **Stefan Sagmeister** — *Things I Have Learned in My Life So Far* (2008). Creative provocation.
- **Pentagram Papers** (periodic publication, 50+ editions). Authorial case study.

### Universal principles and dieter rams

- **Dieter Rams** — *10 Principles of Good Design* (manifesto, ~1980). Mandatory 1-page reading.
- **Naoto Fukasawa** — *Without Thought*. Design as absence of obstacle.
- **Jonathan Ive** — interviews and talks on Apple design.
- **Hartmut Esslinger** — *A Fine Line: How Design Strategies Are Shaping the Future of Business* (2009). Frog Design.

### Web and digital design

- **Brad Frost** — *Atomic Design* (2016, free online). Component-atom-molecule-organism system.
- **Jared Spool** — UIE essays. UX that thinks visually.
- **Erik Kennedy** — *Refactoring UI* (2018, with Adam Wathan, creator of Tailwind). Practical UI for programmers.
- **Steve Krug** — *Don't Make Me Think* (2000, rev 2014). Classic UX.
- **Refactoring UI**, **Material Design**, **IBM Carbon**, **Apple HIG**, **Shopify Polaris**, **GOV.UK Design System**, **GitLab Pajamas** — public reference design systems.

### History and criticism

- **Steven Heller** — *Graphic Style: From Victorian to Hipster* (3rd ed, 2017). Contextual visual history.
- **Philip B. Meggs** — *Meggs' History of Graphic Design* (1983, rev 2016). The history of the field, in volume.
- **Richard Hollis** — *Swiss Graphic Design* (2006). Swiss movement in context.
- **Adrian Shaughnessy** — *How to Be a Graphic Designer Without Losing Your Soul* (2005, rev 2010). Professional + ethical.

### Brazilians

- **Aloisio Magalhães** — founder of modern Brazilian design. Logo of Petrobras, BNDES.
- **Cauduro Martino** — Brazilian institutional reference.
- **Alexandre Wollner** — Bauhaus pioneer in Brazil.
- **Rico Lins** — contemporary Brazilian editorial design.
- **Brazilian reference studios**: Ana Couto Branding, Greco Design, Tátil Design, Crama Design Estratégico, Luminous Design, Veracidade.

### Design systems and tokens (digital, contemporary)

- **Material Design** (Google) — design tokens at massive scale.
- **IBM Carbon** — serious enterprise design system.
- **Apple Human Interface Guidelines** — iOS/macOS reference.
- **Shopify Polaris** — e-commerce.
- **GitLab Pajamas** — open-source.
- **Atlassian Design** — productivity.
- **Tailwind CSS / Catalyst** (Adam Wathan) — contemporary utility-first. Catalyst and shadcn/ui are modern extensions.

> Whoever comes to design without having read Vignelli Canon, Bringhurst Elements and Müller-Brockmann Grid Systems is like doing architecture without having read Le Corbusier, Frank Lloyd Wright, Louis Kahn. Possible. Not recommended.

---

## 2. The 12 founding principles

Non-negotiable doctrine. Every visual piece passes through them.

### Principle 1 — Hierarchy decides everything

The first question before any composition: **what comes first for reading?** Hierarchy isn't decoration — it's reading instruction. Without clear hierarchy, the eye doesn't know where to go, and the piece fails to communicate even if each element is individually beautiful.

Every piece has 3 levels of hierarchy:
- **Anchor (level 1)** — what the eye sees first (headline, big number, or dominant image)
- **Context (level 2)** — what explains the anchor (body, sub-headline)
- **Metadata (level 3)** — what organizes without competing (tag, slide number, handle)

When two elements have equal visual weight, hierarchy broke. Rewrite the prompt, redo the layout.

Theoretical anchoring: Müller-Brockmann (ch. 4); Bringhurst (ch. 8); Lupton (part 3).

### Principle 2 — Restriction frees

A visual system with 3 colors produces more than a system with 9. A system with 2 fonts produces more than with 5. Restriction forces creativity, sustains consistency, accelerates production.

Brands that live by this: Aesop (off-white palette + deep olive-green, period), Apple (Helvetica + white + gray, for 30 years), MUJI (deliberate chromatic absence), Patagonia (palette of 4 colors in 50 years).

Brands that suffer the opposite: the majority of small Brazilian brands that try to have 8 colors, 4 fonts, 12 icons — and end up with no identity at all.

Vignelli: *"Design is one"*. Single system, multiple expression.

### Principle 3 — Negative space is content, not empty

White space isn't "leftover space" — it's an active element. Space breathes composition, separates hierarchy, gives importance to what remains.

Brands that master it: Aesop (50%+ of layouts is negative space), MUJI, Apple, The New Yorker, Wallpaper Magazine.

Brazilian anti-pattern: fear of empty space. Beginner designers fill everything "so it doesn't look incomplete". Result: suffocating piece, heavy reading, forgotten brand.

Practical rule: 3:1 hierarchy. Space between main sections is 3× the space between subsections. Upper third free in editorial pieces (slide, long post, page).

### Principle 4 — Typography first, everything else after

Before color, before image, before layout: **right typography**. Typography carries 80% of the brand's visual personality. Color can change (Coca-Cola went through various palettes), but Coca's Spencerian script remains since 1885.

Frequent error: treating typography as a technical decision ("I'll use Inter because it's free"). Font is a first strategic decision. Stripe chose Söhne (~$1,500 USD for license) because it carries technical authority + freshness; Apple designed custom San Francisco; Aesop uses Garamond because it carries apothecary tradition.

Font decision = personality decision. It isn't "which is pretty". It's "which carries who we are".

### Principle 5 — Color is relational, never absolute

Albers: color doesn't exist alone — it only exists in relation to other colors. Red next to green is vibrant; next to another red, it's subtle. Off-white over black is luminous; over white is dirty.

Implication: never decide a color by looking at it alone. Always test in context: over which background, next to which other color, at what size.

Frequent error: choosing isolated hex on Coolors or Adobe Color, without testing in use. Result: palette that looks beautiful in swatch and burns in application.

### Principle 6 — Contrast is function, not style

Typographic contrast (weight, size, style) creates hierarchy. Color contrast creates attention. Space contrast creates breathing. Contrast is the engine that makes design communicate.

Every piece needs **3 minimum levels of contrast**:
- Macro (between main sections)
- Medium (between headline and body)
- Micro (between body strong and body regular)

Without contrast = flat reading, no hierarchy, dead design.

### Principle 7 — Grid is freedom, not prison

A grid doesn't restrict creativity — it frees mental attention for important decisions. A designer who improvises every margin, every spacing, every alignment, spends 80% of energy on micro-decisions and 20% on what matters.

Müller-Brockmann: the grid is **invisible scaffolding**. Allows consistent creation at scale. Allows other designers to continue the work. Allows the brand to grow without losing identity.

Brands without grid: each piece looks loose. Brands with grid: the feed looks like a curated collection.

### Principle 8 — Detail defines perceived quality

The difference between good design and great design lies in micro-decisions: 1px kerning, 0.05 line-height, 5% contrast, baseline alignment. User doesn't consciously detect — but feels.

Apple invests months adjusting 1px on an icon. Aesop reviews every character of every label. The New Yorker has a fact-checker for every comma.

Implication: good design is obsessively edited. First version is draft. Second begins to be design. Tenth begins to be excellent.

### Principle 9 — Performance is part of design

Slow site = bad design, even if the layout is beautiful. 5MB image without compression = bad design, even if the photo is good. Blocking load = bad design, even if the animation is creative.

Digital performance is a design function — not a later technical decision. Optimized images, pre-loaded fonts (font-display: swap), critical inline CSS, lazy-load outside viewport, GPU-accelerated transitions.

In 2026, **Google Core Web Vitals** (LCP, FID, CLS) are part of SEO. Bad performance = invisible in search.

### Principle 10 — Accessibility is non-negotiable

Minimum WCAG AA:
- Text contrast ≥ 4.5:1 (normal text), ≥ 3:1 (large text)
- Minimum touch size 44×44 px (mobile)
- Visible focus on all interactive elements
- Alt text on every image with function
- Correct heading hierarchy (H1 → H2 → H3, no skipping)
- Color not as sole marker (always + icon or text)

15% of the population has some visual impairment; 30% of mobile users are in adverse conditions (strong sun, dirty hands, fatigue). Accessibility serves everyone.

### Principle 11 — Atomic is inevitable at scale

In a system with more than 5-10 screens, improvised design breaks. Atomic Design (Brad Frost): build from atom (button, icon, label) → molecule (search bar = input + button + icon) → organism (header, footer, product card) → template → page.

Token-first design: colors, typography, spacing, radius — all as variables (`--color-primary`, `--space-4`, `--radius-md`). Change in token propagates through whole system.

Without atomic + tokens, brand redesign takes months. With it, takes weeks.

### Principle 12 — Explicit anti-pattern beats intuition

Listing what NOT to do is as important as listing what to do. Beginner designer falls into traps that senior designer already recognizes. Explicit anti-pattern list accelerates maturity.

That's why this document has section 15 entirely dedicated to anti-patterns. That's why DNA.md has sections 3.5 and 12 dedicated to anti-references. It isn't negativism — it's repertoire.

---

## 3. Consolidated frameworks (with attribution)

### 3.1 — Vignelli Canon (Massimo Vignelli, 2010)

100-page manifesto with universal principles of responsible design. Core:

- **Semantics** — design has meaning, isn't decoration
- **Syntax** — discipline, order, system
- **Pragmatics** — works, is understandable
- **Discipline** — self-imposed restriction
- **Appropriateness** — right design for right context
- **Ambiguity** — avoid — design communicates clearly
- **Design is one** — graphic, product, environment follow same logic

### 3.2 — Swiss System / International Style (Müller-Brockmann)

Characteristics:
- Modular grid as base
- Sans-serif typography (Helvetica, Univers, Akzidenz-Grotesk)
- Left alignment (not justified)
- Hierarchy through size, weight, space
- Objective photography (not decorative illustration)
- Reduced color (black, white, red or single primary)

Contemporary brands that inherit it: Stripe, Linear, Vercel, Apple, Lufthansa, Knoll.

### 3.3 — Atomic Design (Brad Frost, 2016)

Component hierarchy:
- **Atom** — base element (button, label, input)
- **Molecule** — combination of atoms with function (search bar = input + button)
- **Organism** — combination of molecules with larger function (complete header)
- **Template** — page skeleton (without real content)
- **Page** — template with real content

Advantage: facilitates design system, documentation, maintenance at scale.

### 3.4 — Design Tokens (Salesforce 2014, popularized by Material/Carbon/Tailwind)

Named variables for design values:

```css
--color-primary: #...;
--color-text-on-light: #...;
--space-4: 16px;
--radius-md: 8px;
--font-display: 'Söhne', sans-serif;
```

Advantages:
- Change in token propagates through whole system
- Distinct teams consume same source of truth
- Facilitates dark mode, high-contrast mode, internationalization

### 3.5 — Material Design (Google, 2014, continuous)

Most used design system in the world. Principles:
- Material as physical metaphor (layers with real elevation)
- Movement provides meaning
- Bold, graphic, intentional
- Cross-platform (web, Android, iOS, watchOS)

Ideal for: digital products with volume of functionality. Excessive for: editorial brand, artisanal premium product.

### 3.6 — IBM Carbon (open-source)

Enterprise-grade. Principles:
- Carbon white + IBM blue
- Plex (custom type family)
- 16-column grid
- Accessible components by default
- Multi-platform

Ideal for: enterprise, serious B2B, dashboard.

### 3.7 — Apple Human Interface Guidelines

Reference of iOS/macOS. Principles:
- Clarity, deferral, depth
- Native platform patterns
- Animation as language (not decoration)
- SF Symbols as unified icon system

Ideal for: native iOS/macOS app. Inadequate for: web, non-tech brand.

### 3.8 — Refactoring UI / Tailwind (Adam Wathan, 2018+)

Utility-first design. Principles:
- Compose UI from small utilities
- Color scale 50-950 (not primary/secondary)
- Spacing scale based on rem (4px steps)
- Major-third or minor-second typography scale

Ideal for: web app, agile digital product. Catalyst and shadcn/ui are modern extensions.

---

## 4. Color system

### 4.1 — Minimum brand palette structure

| Category | Needed tokens |
|---|---|
| **Identity** | `primary`, `secondary` (optional) |
| **Neutrals** | `bg-light`, `bg-dark`, `text-on-light`, `text-on-dark`, `border`, `surface` |
| **Semantics** (UI) | `success`, `warning`, `error`, `info` |
| **Derivatives** | `primary-light` (~20% lighter), `primary-dark` (~30% darker), alphas (5%, 15%, 30%) |

Minimum total: ~14 tokens. Operational brand needs this.

### 4.2 — Chromatic harmony (Itten)

5 classic schemes:

1. **Monochromatic** — variations of same hue (Aesop)
2. **Analogous** — adjacent colors on the wheel (warmth: orange+red+yellow)
3. **Complementary** — opposites on the wheel (blue+orange, red+green)
4. **Triad** — 3 equidistant colors (red+yellow+blue)
5. **Split-complementary** — base + 2 neighbors of the complementary

Brazilian brands frequently err in "no scheme" — colors chosen by taste without harmonic relation. Result: chaotic palette, tiring reading.

### 4.3 — Contrast (WCAG and Itten)

Itten describes 7 fundamental contrasts:
1. Tone contrast (dark vs. light)
2. Hue contrast (pure colors opposites)
3. Saturation contrast (vivid vs. subtle)
4. Temperature contrast (warm vs. cool)
5. Complementary contrast
6. Simultaneous contrast (color changes in context)
7. Extension contrast (1 small saturated color + 1 large subtle)

WCAG AA is legal minimum. WCAG AAA is minimum for premium brands (≥ 7:1).

Tools: contrast-ratio.com, WebAIM Contrast Checker, Stark plugin.

### 4.4 — Color application: good vs bad

| ✅ Good | ❌ Bad |
|---|---|
| Primary on **keywords** (1-3 per piece) | Primary on **entire sentences** or large backgrounds |
| Primary as **single main CTA** per screen | 3+ competing primary CTAs |
| Secondary color for **hover**, graphics | Random secondary color in headlines |
| Selective saturation (1 vivid point, rest subtle) | Everything saturated (visual fatigue) |
| WCAG AA contrast respected | Light gray text on white background (broken accessibility) |
| Consistent warm OR cool neutrals | Mixed neutrals (pure white + warm-cream together) |

---

## 5. Typographic system

### 5.1 — Font choice (maximum 3 families)

| Function | Characteristics | Examples |
|---|---|---|
| **Display** | Strong personality, bold/black weight, negative kerning, uppercase OK | Söhne Breit, NaN Holo, Druk, Suisse Int'l Bold |
| **Body** | High legibility, weight 400-500, generous x-height | Inter, Söhne Buch, Plus Jakarta, Geist |
| **Mono** | Mono-width characters, use in metadata/code | JetBrains Mono, Söhne Mono, Geist Mono, IBM Plex Mono |

Premium brands frequently custom: SF Pro (Apple), Google Sans, Spotify Circular, Netflix Sans, IBM Plex.
Zero-cost brands: Inter, Plus Jakarta, Manrope, Geist (Vercel), JetBrains Mono.

### 5.2 — Typographic modular scale

Common modular ratio: **1.250 (major third)** or **1.125 (major second)**.

Example scale 1.250 starting from 16px:
- 16, 20, 25, 31, 39, 49, 61, 76 (px)

A scale gives consistent hierarchy. Without a scale, random sizes create visual noise.

### 5.3 — Hierarchy anatomy

| Token | Size | Line-height | Letter-spacing | Weight | Use |
|---|---|---|---|---|---|
| `display-xl` | 96-108px | 0.95 | -3px | 900 | Carousel cover, strong hero |
| `display-l` | 72-80px | 1.0 | -2px | 900 | Internal dark headline |
| `display-m` | 56-64px | 1.1 | -1.5px | 800 | Section subtitles |
| `body-l` | 20-24px | 1.5 | 0 | 400 | Strong body, hero text |
| `body-m` | 16-18px | 1.6 | 0 | 400 | Default body |
| `body-s` | 14px | 1.5 | 0.2px | 400 | Caption, helper text |
| `tag` | 12-13px | 1.4 | 3px | 700 | Uppercase tags |
| `mono-s` | 12-13px | 1.4 | 0.5px | 600 | Metadata |

### 5.4 — Typography: good vs bad

| ✅ Good | ❌ Bad |
|---|---|
| Headline in display, body in body, tag in mono — maximum 3 families | 4-5 different fonts (Comic Sans + Times + Arial + script) |
| Clear hierarchy (3+ distinct levels) | Everything at the same size/weight |
| Generous line-height in body (1.5-1.6) | Body with line-height 1.0-1.2 (tires) |
| Negative letter-spacing in large headline | Positive letter-spacing in body (dated, irritating) |
| Uppercase only in tag/short headline | Uppercase in body paragraph (illegible) |
| Italic rare, intentional | Constant italic (loses effect) |

---

## 6. Grid and spacing system

### 6.1 — Baseline grid

Every piece follows a baseline of 4 or 8px. Derived spacing scale:

```
4, 8, 12, 16, 24, 32, 48, 64, 96, 128
```

Minimum margin between elements = baseline. Margin between sections = multiple (3-4× baseline).

### 6.2 — Column grid

| Medium | Columns | Gutter | Margin |
|---|---|---|---|
| Web desktop | 12 | 24px | 80-96px |
| Web tablet | 8 | 24px | 48-64px |
| Web mobile | 4 | 16px | 16-24px |
| Slide (1080×1350) | 4-8 modular | 16px | 80px |
| Email | 1-2 | n/a | 32-40px |

### 6.3 — Border radius

| Token | Value | Use |
|---|---|---|
| `radius-none` | 0 | Editorial, brutalist |
| `radius-sm` | 4px | Inputs, small buttons |
| `radius-md` | 8px | Cards, default buttons |
| `radius-lg` | 12-16px | Large cards, modals |
| `radius-xl` | 24px | Hero cards |
| `radius-full` | 9999px | Avatars, badges, pill buttons |

Conservative brand: 0-4px. Contemporary brand: 8-12px. Modern tech brand: 8-16px. Playful brand: 16-24px+.

### 6.4 — Elevation/shadow

| Level | Use |
|---|---|
| `shadow-none` | Sober editorial (Aesop, MUJI, Apartamento) |
| `shadow-sm` | Subtle cards |
| `shadow-md` | Modals, dropdowns |
| `shadow-lg` | Hero cards, elevated elements |
| `shadow-xl` | Almost never — only for very specific pieces |

Trend 2024-2026: **subtle or absent shadow**. 2010 skeumorphism came back nostalgic in some niches, but usually dated.

---

## 7. Logo and graphic mark

### 7.1 — Minimum necessary variants

| Variant | Use |
|---|---|
| Main logotype (horizontal) | Headers, footers, hero, decks |
| Vertical logotype | Square spaces, social profiles |
| Monogram (isolated symbol) | Favicon, app icon, watermark, small contexts |
| Lockup with tagline | Institutional presentations |
| Black mono | On light backgrounds without brand color |
| White mono | On dark backgrounds without brand color |
| Inverted color (if applicable) | On strong primary color |

Total: 5-7 variants. Fewer = lack of flexibility. More = visual inflation.

### 7.2 — Clear space and minimum size

Minimum clear space = **0.5 × height of "x"** (or equivalent unit of the logo). Nothing (text, image, solid color) can invade this area.

Minimum digital size: 80px wide. Below that, use monogram. Minimum print size: 25mm.

### 7.3 — Anti-use of the logo

- ❌ Rotated logo (rotation ≠ 0°)
- ❌ Distorted logo (altered proportion, "stretched" to fit)
- ❌ Logo with strong filter (large drop shadow, glow, blur, gradient overlay)
- ❌ Logo inside another logo (heavy composition)
- ❌ Logo in unapproved color (random red because it looked pretty)
- ❌ Logo over low-contrast image without protection (gradient or reserved area)
- ❌ Logo below minimum size
- ❌ Logo without clear space respected
- ❌ Logo "bleeding" out of canvas in badly calculated crop

### 7.4 — Logo cases: good vs bad

| ✅ Good | ❌ Bad |
|---|---|
| Simple shape, recognizable in silhouette (Nike swoosh, Apple maçã, Twitter bird) | Fine details that disappear at small size |
| Works mono and in color | Only works with gradient or specific color |
| Has monogram version | Only the complete version exists (problem in favicon) |
| Timeless — Paul Rand IBM (1972) still works | Dated trend (2000s 3D effect, purple-blue tech gradient) |
| Carries conceptual meaning | Literal pictogram without depth (bread logo for bakery) |

---

## 8. Universal components

### 8.1 — Cards

- Border-radius: `radius-md` (8px) default
- Internal padding: 24-32px
- Background: slightly contrasts with page background
- Border: 1px solid in `border` token OR subtle shadow — choose one, not both
- Internal spacing: respect baseline scale

### 8.2 — Buttons

| Type | Use |
|---|---|
| **Primary** | 1 per screen. Main action. `primary` color. |
| **Secondary** | Alternative action. Border + transparent OR `surface` |
| **Tertiary / Ghost** | Tertiary action. Text only, no background |
| **Destructive** | Erases, removes. `error` color |
| **Disabled** | Blocked state. Reduced opacity |

Sizes: sm (32px), md (40px), lg (48px). Minimum mobile touch target: 44×44px.

### 8.3 — Forms

- Label always above input (not placeholder-only — loses on starting to type)
- Helper text below (medium gray)
- Error state in `error` + icon + clear message
- Minimal success state (green check, no exaggerated celebration)
- Explicit required marker (asterisk or text)

### 8.4 — Tables

- Header with greater weight (600-700)
- Alternating rows with subtle background (zebra) — optional
- Vertical padding 12-16px, horizontal 16-24px
- Numeric alignment to the right, text to the left
- Border or subtle shadow between rows

---

## 9. Motion

### 9.1 — Principles of movement

Material Design Motion: *"Movement provides meaning."*

- Movement serves function (transition, feedback, hierarchy)
- Not decoration
- Performance > beauty (60fps minimum)
- Respect `prefers-reduced-motion`

### 9.2 — Approved easing curves

| Token | CSS | Use |
|---|---|---|
| `ease-out` | `cubic-bezier(0.0, 0.0, 0.2, 1)` | Appearances, entrances |
| `ease-in` | `cubic-bezier(0.4, 0.0, 1, 1)` | Exits, disappearances |
| `ease-in-out` | `cubic-bezier(0.4, 0.0, 0.2, 1)` | State changes |
| `spring` | `cubic-bezier(0.34, 1.56, 0.64, 1)` | Playful microinteractions (rare) |

### 9.3 — Default durations

| Type | Duration | Easing |
|---|---|---|
| Microinteraction (hover, click, focus) | 150-200ms | ease-out |
| Appearance (modal, tooltip) | 250-350ms | ease-out + fade |
| Screen change | 300-450ms | ease-in-out + subtle slide |

### 9.4 — Motion anti-patterns

- ❌ Bounce/elastic in main transitions (looks fragile)
- ❌ Fade > 500ms (sensation of slowness)
- ❌ Strong parallax (3D rotation, large scale) — dated, distracts
- ❌ Animation for animation's sake (no purpose)
- ❌ Fake loading spinner (doesn't indicate real progress)
- ❌ Auto-playing video with sound
- ❌ Confetti in routine interaction

---

## 10. What is GOOD vs BAD design (canonical cases)

### 10.1 — GOOD design (to study)

**Global reference brands:**
- **Aesop** (aesop.com) — apothecary minimalism, Garamond + off-white palette + deep olive-green, surgical still-life photography
- **MUJI** (muji.com) — Japanese utilitarianism, deliberate chromatic absence, Akzidenz-Grotesk typography
- **Stripe** (stripe.com) — tech-clear, Söhne, subtle gradients, well-dosed primary color
- **Linear** (linear.app) — premium software, dark-first, surgical micro-interactions
- **Vercel** (vercel.com) — geometry, Geist (custom), black+white+1 color
- **Apple** (apple.com) — extreme negative space, absolute product photography, SF Pro
- **Patagonia** (patagonia.com) — serious outdoor, robust typography, natural palette
- **Hermès** (hermes.com) — French luxury, Helvetica + orange, negative space
- **The Gentlewoman** (thegentlewoman.co.uk) — sober editorial, hardcover typography
- **Apartamento** (apartamentomagazine.com) — interior magazine, 35mm photography, dense editorial layout

**Brazilian reference brands:**
- **Granado** — well-worked pharmaceutical heritage
- **Havaianas** — Brazilian pop consistent over decades
- **Osklen** — Brazilian lifestyle with substance
- **Farm** — Brazilian colorful pop, recognizable identity

**Reference studios:**
- Pentagram, Wolff Olins, Collins, Porto Rocha, Manual, Berger&Föhr, Mucho, Mast, Sagmeister & Walsh, Dia Studio, Order, Other Means

### 10.2 — BAD design (avoid)

**Saturated visual anti-patterns:**
- Hero with purple-blue tech gradient (dated 2018-2022 B2B SaaS aesthetic)
- "Corporate Memphis" — flat illustrations with strange proportions, saturated palette
- Stock photo of team smiling in meeting room
- Header with 6 menu items + search + login + language + cart — confusion
- Badges of "AI-powered", "Award-winning", "#1 in market" without proof
- Typography Lobster, Pacifico, Comic Sans in any professional context
- Strong drop shadow of 20px+ blur (dated)
- Large border radius in serious editorial pieces
- Decorative background pattern (dated, distracts)
- 5+ different gradients on the same page

**Brands to study as how NOT to do** (without publicly naming, but recognizable):
- Majority of Brazilian B2B SaaS with identity copied from Stripe but badly executed
- Personal brands of "AI consultant" with purple gradient + smiling founder photo + 3 competing CTAs
- Average fashion e-commerce with 8 colors on home, 4 carousels, fixed promotional banner

---

## 11. What is FAST vs SLOW design (efficiency)

### 11.1 — FAST (scalable, efficient)

- **Design tokens** — change propagates through whole system
- **Reusable components** — Atomic design, component library
- **Templates per touchpoint** — slide, post, email, landing pre-structured
- **Consistent grid system** — don't improvise margin per piece
- **UI libraries** (shadcn, Radix, MUI, Carbon) — don't reinvent button
- **Figma with Variables + Auto Layout** — change in one place, applies in hundreds
- **Clear naming convention** — `button-primary-md` is findable

### 11.2 — SLOW (artisanal, manual)

- **Custom pixel-perfect each piece** — valid for hero, invalid for everything
- **Without tokens** — every change is manual in N files
- **Without grid** — each piece is zero decisions
- **Re-create component every time** — 100% custom is 100% rework
- **Inconsistent naming** — "btn1", "new button", "BUTTON_FINAL_v3.fig" — no one finds
- **Slow series approval** (multiple people, no clear criterion)
- **Redoing logos/illustrations for each piece** instead of having library

### 11.3 — Efficiency: golden rule

> Senior designer spends 80% of time building SYSTEM. 20% applying.
> Beginner designer spends 80% applying. 20% on the system (or zero).

Brands that grow keep senior ratio. Brands that stall keep beginner ratio.

---

## 12. What WORKS vs DOESN'T WORK (effectiveness)

### 12.1 — WORKS (tested at scale)

- **Clear hierarchy** — user knows where to look first
- **WCAG AA contrast** — comfortable reading in any condition
- **Mobile-first** — 70%+ of Brazilian traffic is mobile
- **44×44px touch target** — clickable without frustration
- **Fast loading** (LCP < 2.5s) — user doesn't abandon
- **Simple forms** (minimum of necessary fields)
- **Guiding empty state** ("Nothing here yet. Start by creating X.")
- **Clear confirmation** after action ("Saved")
- **Visually distinct primary action button** (1 per screen)
- **Breadcrumbs or contextual navigation** clear in large sites

### 12.2 — DOESN'T WORK (tested at scale)

- **3+ competing primary CTAs** — user paralyzed
- **Long forms with everything "required"** — massive abandonment
- **Intrusive pop-ups on load** — high bounce
- **Auto-play video with sound** — user closes tab
- **Hover states on mobile** — there is no hover on touch
- **Color as sole marker** (green = good, red = bad) — color-blind lost
- **Letters too small (12px or less) on mobile** — illegible
- **Automatic slider/carousel** — user catches meta-info in the middle
- **Mega-menu with 50 items** — paralysis
- **Modal on modal on modal** — user lost in context

---

## 13. What SELLS vs REPELS (visual conversion)

### 13.1 — SELLS (tested on landing pages, e-commerce, ads)

**Principles of visual conversion** (Brian Balfour, ConversionXL, Joanna Wiebe):

- **Hero with 1 clear message + 1 single CTA** (above the fold)
- **Realistic product photo, high quality, multiple angles** (e-commerce)
- **Short demo video < 60s** with caption (autoplay without sound OK)
- **Specific social proof** (real customer logos, testimonials with name+face+company)
- **Transparent price** — hiding price creates friction
- **Explicit guarantee** (return in 7-30 days)
- **Real urgency** (true limited stock, concrete deadline)
- **Reduced friction at checkout** (1-click if possible, multiple payment methods)
- **Legitimate trust badges** (SSL, payment methods, recognizable certifications)
- **Visible FAQ** answering common objections

**Aesthetics that sells in fashion e-commerce:**
- Product photo on neutral background (white/off-white)
- Model in natural movement, not rigid pose
- Details of fabric, stitching, finish (close-ups)
- Lifestyle context (product in real use)
- Video of 5-15s showing product worn

### 13.2 — REPELS (tested, drops conversion)

- **Email pop-up at second 0** — bounce
- **Generic hero** ("the best solution for you") without specificity
- **Stock photo of obvious "diversity"** (Getty catalog)
- **Vague CTAs** ("Learn more", "Check it out", "Click here")
- **Price upon request** without clear B2B justification
- **Long forms for free trial** (5+ fields = abandonment)
- **Autoplay video with sound** — user closes
- **Anonymous testimonials** ("Maria, satisfied customer")
- **False or exaggerated trust badges** ("#1 in the world", no source)
- **Carousel with 8+ slides** — no one sees after the 2nd
- **Light gray text on white background** — illegible, non-accessible
- **Auto-rotating carousel** — frustrates reading

### 13.3 — Central commercial principle

Visual conversion isn't "being beautiful". It's **removing friction + creating clarity + delivering proof + facilitating action**. A premium brand that fails at this sells less than an average brand that executes these 4 fundamentals.

---

## 14. What AGES WELL vs DATES FAST

### 14.1 — AGES WELL (choose when possible)

- **Well-designed classic typography** — Garamond, Caslon, Helvetica, Univers, Times: decades
- **Swiss modular system** — 70 years, still contemporary
- **Restricted palette (2-3 colors)** — Hermès orange-brown, Tiffany blue, Ferrari red
- **Simple geometry** — circle, square, triangle (classic logos)
- **Abundant negative space** — Apple 20 years ago, still current
- **Documentary editorial photography** — Magnum from the 60s still moves
- **Black and white** — timeless by design

### 14.2 — DATES FAST (caution when choosing)

- **Color trend of the season** (Pantone Color of the Year usually dates in 2-3 years)
- **"Y2K" style** (chrome, glitter, hologram) — lasted 2020-2022
- **"Corporate Memphis"** flat illustrations — dated 2018-2022
- **Purple-blue tech gradient** (SaaS 2018-2022) — dated
- **Extreme border radius** (>32px in almost everything) — fashion 2020-2022
- **Glassmorphism** (translucent frosted glass) — fashion 2020-2022
- **Neumorphism** (soft relief) — lasted 6 months
- **Deliberate brutalism** (default browser styles) — dangerous, easy to look amateur
- **3D illustration Notion style** — saturated in 2024-2025

### 14.3 — Principle of longevity

> "If you make something timeless, you only have to make it once."
>
> — Massimo Vignelli

A brand that pursues trend needs to redesign every 2-3 years. A brand that pursues classic updates every 10-15 years. Massive opportunity cost.

When it's worth risking trend: young brand that needs to make noise fast, with explicit plan to redesign in 2-3 years.
When NOT worth it: brand that wants to build heritage. Every trend decision is visual debt.

---

## 15. Exhaustive visual anti-patterns

List of EVERYTHING that NEVER appears in well-made design. Maestro actively audits each piece against this list.

### 15.1 Composition
- ❌ Centered text on content piece (only CTA can center)
- ❌ 2 elements of same visual weight competing (broken hierarchy)
- ❌ Image without overlay over text (bad contrast)
- ❌ Card inside card (heavy composition)
- ❌ Table with less than 3 rows (disproportionate)
- ❌ Slide with only 1 sentence + tag (looks incomplete)

### 15.2 Color
- ❌ Primary color in background of large text block
- ❌ 4+ colors in one piece (overload)
- ❌ Neon or Y2K color (wrong decade)
- ❌ Generic "Hollywood teal & orange" color grading
- ❌ Saturated Instagram filters (Lo-fi, Valencia)
- ❌ Exaggerated HDR
- ❌ 5+ different gradients per page

### 15.3 Typography
- ❌ Sentence case in headline (no weight)
- ❌ Uppercase in body paragraph (illegible)
- ❌ 4-5 different fonts
- ❌ Handwritten/brush script text in professional piece
- ❌ Italic in entire paragraph
- ❌ Positive letter-spacing in body
- ❌ Justified text (creates white rivers)
- ❌ Font-size < 14px in mobile body

### 15.4 Image
- ❌ Identifiable stock photo
- ❌ Catalog smile
- ❌ Corporate handshake
- ❌ "Pensive" person with hand on chin
- ❌ Lit lamp as idea metaphor (terminal cliché)
- ❌ Gears as strategy metaphor
- ❌ Puzzle with missing piece
- ❌ AI faces with glazed eyes

### 15.5 Motion / Interaction
- ❌ Bounce/elastic in main transitions
- ❌ Strong parallax (dated)
- ❌ Auto-rotating carousel
- ❌ Auto-playing video with sound
- ❌ Fake loading spinner
- ❌ Confetti in interaction
- ❌ Glitch transitions

### 15.6 Identity
- ❌ Logo rotated, distorted, with strong filter
- ❌ Generator watermark on final piece
- ❌ "Swipe →" arrows (swipe is native)
- ❌ Random decorative emoji
- ❌ Generic stock icons

---

## 16. Quality criteria

How to judge design work (own or third-party):

### 16.1 — The 7 criteria

1. **Clear hierarchy** — does eye know where to go first? (yes/no)
2. **Sufficient contrast** — WCAG AA minimum? (yes/no)
3. **Visible system** — does piece look like part of a coherent whole? (yes/no)
4. **Space breathes** — is composition not suffocated? (yes/no)
5. **Careful detail** — alignments, kerning, correct micro-decisions? (yes/no)
6. **Performance OK** — loads fast, works on mobile? (yes/no)
7. **Memory** — is piece distinctive? Would you remember it in 1 month? (yes/no)

5+ "yes" = competent design. 7/7 "yes" = excellent design.

### 16.2 — Feed test

Place the piece in a 3×3 grid next to 8 other random pieces of the category. Is your piece distinguishable? If it disappears, failed. If it positively draws attention, worked.

### 16.3 — Thumbnail test

Reduce the piece to 100×100px. If it still communicates the central message, hierarchy works. If it becomes a confusing blur, hierarchy failed.

### 16.4 — 24h memory test

Show the piece to someone. 24h later, ask what they remember. Bad memory = forgettable piece, even if "technically correct".

---

## 17. When the Maestro should call me

Explicit routing for interface with CLAUDE.md:

### 17.1 — Always call me for:

- **Complete color palette generation** (primary + neutrals + semantics + derivatives)
- **Typographic decision** (choice of display, body, mono — system)
- **Audit of graphic piece** (post, slide, page, ad)
- **Grid system and spacing definition**
- **Logo decision** (variants, clear space, anti-use)
- **Design token generation** for DNA.md
- **Response to questions like "is this good design?"** or "is this going to work?"
- **Analysis of visual references** the person dropped in `materiais/3-referencias-visuais/`

### 17.2 — I can be punctually consulted for:

- Border radius, shadow, motion decision
- Specific component (button, card, form)
- Hover, focus, active state
- Animation or micro-interaction
- Iconography (style, weight, size)

### 17.3 — Don't call me for:

- Photographic direction (call `09-Photography-Direction.md`)
- AI image generation (call `10-Image-Generation-Engine.md`)
- Copy or tone of voice (call `07-Voice-and-Tone.md`)
- Brand strategy (call `05-Brand-Strategy.md`)

---

## 18. Operational checklist (interface with Maestro)

### Before proposing visual system

1. Read this file (focus on sections 2, 3, 4, 5, 6)
2. Read current DNA.md (section 3 — Visual style)
3. Read visual references in `materiais/3-referencias-visuais/`
4. Apply Vignelli Canon as mental filter
5. Propose complete system (not punctual)

### Before auditing graphic piece

1. Apply 7 quality criteria (section 16.1)
2. Run feed, thumbnail, memory tests (sections 16.2-16.4)
3. Active scan of anti-patterns (section 15)
4. Diagnosis in prose + concrete suggestion

### Before generating design tokens for DNA.md

1. Define complete palette (section 4)
2. Define complete typographic system (section 5)
3. Define grid + spacing scale (section 6)
4. Document application rules (when to use each token, when NOT to use)
5. Justification for each important decision

---

## One-line summary

**Think like Vignelli, systematize like Müller-Brockmann, edit like Apple, validate like WCAG, durabilize like Hermès.**
