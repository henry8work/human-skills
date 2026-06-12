# -*- coding: utf-8 -*-
"""Generates the 7 human-skills briefing PDFs (WeasyPrint).

Run:  DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib ../.venv-pdf/bin/python generate_briefings.py
"""
import os
from weasyprint import HTML

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

SKILLS = [
    {
        "name": "human-image",
        "num": "01",
        "tagline": "Cinematic photo direction that turns a one-line brief into a director-grade prompt — and renders it.",
        "tools": "Claude + Magnific (free) or Higgsfield (paid)",
        "what": "Takes a short idea, a reference image, or a loose description and works like a director of photography. It builds a structured, physics-based prompt — camera, lens, light, texture, composition — and renders it through the provider you choose, saving the prompt and metadata alongside every run.",
        "why": "Casual prompts produce casual images: flat lighting, generic framing, the unmistakable “AI look.” The gap between a throwaway keyword dump and a stop-the-scroll still is workflow. This skill encodes the prompt discipline a real DP uses, so every render starts from structure instead of improvisation.",
        "strong": "It describes physics, not adjectives. It bans empty words like “cinematic” or “epic” and instead specifies focal length, T-stop, Kelvin, shadow direction and tonal curve — which is what modern models (Nano Banana) actually respond to. It always asks Magnific (free) vs Higgsfield (paid) before spending, and never renders silently on the paid path.",
        "when": [
            "A key visual or hero image for a campaign",
            "Editorial or product stills",
            "Static ads",
            "Reproducing or transforming a reference you paste in",
            "Any time “generate an image of X” deserves real art direction",
        ],
        "triggers": [
            '"create an image" / "make a photo"',
            '"image prompt" / "key visual"',
            '"product photo" / "editorial image"',
            '"crie uma imagem" / "foto de produto"',
        ],
        "steps": [
            "Confirm specs — ratio, resolution, references, purpose",
            "Ask the provider (Magnific or Higgsfield)",
            "Build the structured prompt",
            "Render",
            "Save a per-run folder with prompt + params",
        ],
        "example_case": "Image bank for a bank — taken from a real session",
        "example_prompt": "I want to generate an image bank of 20 beautiful, advertising-grade images for a bank. No bank name or branding needed. Lifestyle images, candid, with very diverse people, diverse lighting, in diverse settings. I want the angles to always be unusual — the angles that aren’t the standard ones.",
        "example_flow": [
            "The skill turns the loose brief into 20 distinct scenarios — breakfast, skatepark, motoboy, dancing elders, rooftop, fisherman — each with its own demographic, setting and light",
            "Writes a structured cinematic prompt per image: specific focal length, camera position (ground level, overhead, through-objects), light source and color temperature — no “beautiful photo” adjectives",
            "Renders the set and saves a per-run folder for each image with image.png + prompt.txt, so any shot can be re-rendered or tweaked later",
        ],
        "example_result": "A 20-image lifestyle bank — diverse people, settings and lighting, every frame on an unusual angle — each delivered in its own folder with the exact prompt that produced it.",
        "result_images": [f"assets/human-image-results/{n}.jpg" for n in ["01_breakfast", "02_skatepark", "06_dad_baby", "08_motoboy", "11_pool", "12_dancing_elders", "16_braiding", "19_fisherman"]],
        "result_images_caption": "8 of the 20 generated images — note the angles: ground level, overhead, through objects, never eye-level.",
        "honest": "The skill writes the prompt and fires the render, but it doesn’t replace your eye. The first pass lands around 80% — expect one to three seed iterations to dial it in. If the provider isn’t connected, it hands you the finished prompt plus the exact command instead of failing.",
    },
    {
        "name": "human-product-ad",
        "num": "02",
        "tagline": "Turns an amateur phone photo of a product into a 15-second cinematic vertical ad — hero-first, frames approved before any video.",
        "tools": "Claude + Magnific (free via Run Unlimited, or plan credits) / Higgsfield + Kling video + ffmpeg",
        "what": "You drop a phone photo of a product in a folder; the skill returns a 9:16 cinematic ad. It proposes 3 creative directions, generates ONE hero image, you approve it, and only then derives 4 variations anchored to that hero (same scene, light, palette and texture — different angles). The 5 frames become 5 video takes (Kling) and are stitched in ffmpeg with no quality loss.",
        "why": "A casual prompt gives you 5 disconnected images that don’t look like one film. The hero-first flow exists so the whole ad shares one look: you lock it once on the hero, approve it with your own eye, and every later frame inherits it — instead of burning render budget discovering the look five times.",
        "strong": "Hero-first continuity (the approved hero anchors all 4 variations), a hard rule that video only renders after you approve the frames, and render-path discipline: before anything renders it offers three paths and asks — Magnific MCP (plan credits), Magnific Hybrid “Run Unlimited” (zero credits, you click once in the browser), or Higgsfield (paid). It never assumes a default.",
        "when": [
            "Turning an amateur product photo into a premium ad",
            "A 9:16 cinematic vertical ad from a single product shot",
            "“I have an ugly photo of my product, I want a top-tier ad”",
            "A short product film built from approved frames",
            "An IMAX-look video of a product",
        ],
        "triggers": [
            '"cinematic product ad" / "product ad cinematic"',
            '"IMAX video of my product"',
            '"premium vertical product video"',
            '"foto de produto pra ad" / "anúncio premium"',
        ],
        "steps": [
            "Propose 3 creative directions from the photo",
            "Generate ONE hero image → human approval",
            "Derive 4 variations anchored to the hero (5 frames)",
            "Animate each frame into a video take (Kling)",
            "Stitch the takes + soundtrack in ffmpeg → final MP4",
        ],
        "example_case": "Lagunitas IPA — taken from a real session: a folder of photos → World Cup ad",
        "example_action_label": "You give it",
        "example_action_quoted": False,
        "example_prompt": "Just a folder of reference images, dropped in — no prompt, no art direction. “These are the images I have for the campaign.” The skill drives the rest from there.",
        "example_images": ["assets/human-product-ad-thumbs/ref-1.jpg", "assets/human-product-ad-thumbs/ref-2.jpg", "assets/human-product-ad-thumbs/ref-3.jpg", "assets/human-product-ad-thumbs/ref-4.jpg"],
        "example_images_caption": "The only input: the reference photos dropped in the folder — the Lagunitas bottle plus a few celebration vibes. No prompt was written.",
        "example_flow": [
            "The skill reads the folder, identifies the product (the Lagunitas IPA bottle) and the vibe references, then proposes 3 creative directions (Golden Hour Taproom · Hop Storm · Petaluma Dust) — the user picks the World Cup lifestyle angle",
            "It generates ONE hero for approval — the bottle held up like a trophy at golden hour, label kept 100% faithful to the photo — then asks the render path; the user takes the zero-credit one, so the skill builds a Magnific Space with pre-filled nodes, the user clicks “Run Unlimited” in the browser, and the 4 variations + 5 video takes (Kling 2.5) come back at 0 credits",
            "Each approved frame is animated into a 5s take; ffmpeg stitches them (no re-encode) and muxes a generated soundtrack into the final cut",
        ],
        "example_result": "A finished 9:16 vertical ad — 5 frames (hook · reveal · detail · action · hero) animated and stitched into a full cut plus a punchy 10s music edit — the frame set rendered at 0 credits via the Magnific Run Unlimited flow.",
        "result_images": ["assets/human-product-ad-thumbs/seq-01-hook.jpg", "assets/human-product-ad-thumbs/seq-02-reveal.jpg", "assets/human-product-ad-thumbs/seq-03-detail.jpg", "assets/human-product-ad-thumbs/seq-04-action.jpg", "assets/human-product-ad-thumbs/seq-05-hero.jpg"],
        "result_images_caption": "The 5 frames derived from the approved hero (hook · reveal · detail · action · hero) — one film, then animated into the final video.",
        "honest": "This is a multi-step pipeline with human checkpoints — deliberately not one-click. Video only renders after you approve the frames. The zero-credit “Run Unlimited” path needs one manual click in the Magnific browser tab; music generation does debit plan credits even on that path.",
    },
    {
        "name": "human-dna",
        "num": "03",
        "tagline": "Builds and operates a brand’s Creative DNA so every asset stays on-brand.",
        "tools": "Claude + Magnific / Higgsfield",
        "what": "Creates, edits and audits a brand’s Creative DNA — visual identity, tone of voice, strategy, audience, anti-patterns, photography direction — and generates a canonical DNA.md plus a per-project CLAUDE.md so Claude follows the brand style across every material. Multi-project: each brand lives in its own folder.",
        "why": "Brand consistency dies when it lives only in people’s heads. Without a written DNA, every designer — and every AI render — reinterprets the brand slightly differently. This skill turns the brand into a documented source of truth the tools can actually follow.",
        "strong": "A one-question-at-a-time discovery (no overwhelming forms), specialist “doctors” per discipline (strategy, voice, photography, anti-patterns), and — crucially — it operationalizes the DNA. It doesn’t just describe the brand; it makes Claude render and audit against it.",
        "when": [
            "Creating a new brand from scratch",
            "Auditing an existing brand",
            "Building a brand book or manifesto",
            "A rebrand",
            "Any time materials must respect a specific brand",
        ],
        "triggers": [
            '"create brand" / "creative DNA"',
            '"brand audit" / "manifesto"',
            '"rebrand"',
            '"DNA criativo" / "manual da marca"',
        ],
        "steps": [
            "List or choose the brand project",
            "Conversational briefing, one question at a time",
            "Generate DNA.md + per-project CLAUDE.md",
            "Test a small piece against the DNA",
            "Refine, then reuse across materials",
        ],
        "example_case": "Dengo chocolate — taken from a real session: website + Instagram → DNA → assets",
        "example_prompt": "Build the Creative DNA for Dengo from their website and Instagram: dengo.com.br and instagram.com/dengochocolates. Then, using that DNA, generate brand textures and illustrated patterns with animals and plants in the Dengo style.",
        "example_flow": [
            "The skill studies the two links — website and Instagram — and runs a guided briefing, extracting the brand world (cacao, cabruca agroforest, jute, artisanal warmth, cream-paper palette) into a canonical DNA.md plus a per-project CLAUDE.md",
            "With the DNA written, every render is driven by it (not by a generic “chocolate brand” prompt); the skill asks which provider to use (Magnific free vs Higgsfield paid) before spending anything",
            "Renders the texture set first, then the illustrated wildlife set — each image audited against the same DNA so the whole library feels like one brand",
        ],
        "example_result": "From two links: a written DNA, and then a coherent asset library generated from it — brand textures (cut cacao, almonds on jute, melted chocolate, cabruca canopy) and wildlife illustrations (golden lion tamarin, toucan, jaguar, morpho butterflies), all unmistakably Dengo.",
        "result_images": [f"assets/dna-dengo/tex-{i}.jpg" for i in range(1, 5)] + [f"assets/dna-dengo/ill-{i}.jpg" for i in range(1, 5)],
        "result_images_caption": "From the DNA → top: brand textures · bottom: illustrated wildlife — one brand language across both sets.",
        "honest": "Building a real DNA is a conversation, not a button — expect a guided briefing. The output is only as good as the inputs you give it: vague answers produce a vague DNA.",
    },
    {
        "name": "human-carrossel",
        "num": "04",
        "tagline": "Editorial Instagram carousels at scale — researched, written, and rendered.",
        "tools": "Claude + Higgsfield CLI + GPT Image 2",
        "what": "Produces editorial Instagram carousels on demand (from a theme or your own text) or fully automated (R1 News Scout finds the story, R2 builds and renders it). It handles news research, editorial angle, headline, narrative spine, slide-by-slide copy, and the visual render.",
        "why": "Carousels at volume usually mean one of two bad outcomes: generic AI-slop, or hours of manual layout. This skill packages the editorial discipline — headline engine, narrative spine, anti-slop rules — so the output reads like a real editorial team made it.",
        "strong": "A dedicated headline engine and narrative architecture, strict anti-AI-slop editorial rules, and an automation path (Notion + Routines) for daily output. Slide rendering is pinned to GPT Image 2 via Higgsfield for visual consistency across a set.",
        "when": [
            "Daily or weekly editorial carousels",
            "News-to-carousel posts",
            "Setting up the automated pipeline",
            "Re-rendering today’s carousel or swapping a single slide",
        ],
        "triggers": [
            '"carousel" / "carrossel"',
            '"editorial carousel"',
            '"news-to-carousel post"',
            '"re-render today’s carousel" / "adjust a slide"',
        ],
        "steps": [
            "Setup — brand identity + trusted sources",
            "Pick the topic or news",
            "Headline engine + narrative spine",
            "Slide-by-slide copy",
            "Render slides and deliver",
        ],
        "example_case": "Moove Running — taken from a real session: 3 design references + one news link",
        "example_images": ["assets/carrossel-refs/ref-1.jpg", "assets/carrossel-refs/ref-2.jpg", "assets/carrossel-refs/ref-3.jpg"],
        "example_images_caption": "The 3 design references pasted into the chat — decoded by the skill into the visual brief.",
        "example_prompt": "Here are 3 design references for the visual style I want [pastes 3 kinetic running shots]. And here’s the source article: https://www.jornalcorrida.com.br/post/aprenda-a-correr-melhor — let’s build a carousel for Moove Running from this.",
        "example_flow": [
            "The skill decodes the 3 references into a visual brief: body always in motion, extreme angles (ground-level close-up, fisheye low-angle), directional motion blur — never a neutral eye-level shot",
            "Reads the article and calls it honestly — too generic to follow as-is — but extracts the real angle hiding inside it (“the new urban elite runs at 6 am”) and backs the headline pick with the engine’s lift data (+155% Brazil/Context)",
            "Renders the cover first for approval, then fires the remaining 8 slides in parallel using the approved cover as the reference image for visual consistency",
        ],
        "example_result": "A complete 9-slide editorial carousel (3:4, 2K) in the brand’s terracotta palette, delivered with a per-slide verdict table that flags the one slide needing a re-render.",
        "result_images": [f"assets/carrossel-slides/slide-0{i}.jpg" for i in range(1, 10)],
        "result_images_caption": "The 9 rendered slides — cover approved first, the other 8 generated in parallel from it.",
        "honest": "Unlike the other skills, this one is pinned to Higgsfield + GPT Image 2 (paid) — it does not offer the free Magnific path, because the slide pipeline depends on that specific model. Editorial quality depends on good sources configured during setup.",
    },
    {
        "name": "human-social",
        "num": "05",
        "tagline": "Unfolds one folder of content into native pieces for Instagram and LinkedIn.",
        "tools": "Claude + Magnific / Higgsfield",
        "what": "Takes a folder containing text plus images and creates native pieces — Instagram Feed, Instagram Stories (multi-card), and LinkedIn Feed. Each is a fresh image (not a resize) with a platform-specific caption.",
        "why": "Resizing one asset across platforms reads as lazy and underperforms. Each network has its own format, tone and behavior. This skill produces purpose-built pieces per platform instead of stretching a single image to fit everywhere.",
        "strong": "No resize — a fresh image per platform with a reference chain back to the original. A per-platform caption strategy (visual IG feed, conversational Stories, professional LinkedIn). It writes a manifest for traceability and can be triggered as a sub-flow by other skills.",
        "when": [
            "Turning a finished piece or folder into social content",
            "Adapting a campaign for Instagram + LinkedIn",
            "Making feed / stories / LinkedIn versions from one source",
        ],
        "triggers": [
            '"unfold this folder"',
            '"adapt for Instagram and LinkedIn"',
            '"desdobrar pasta"',
            '"criar versões pra redes"',
        ],
        "steps": [
            "Confirm the input folder path",
            "Validate text + at least one image",
            "Ask the provider",
            "Render IG Feed, Stories, LinkedIn",
            "Save back into the folder with a manifest",
        ],
        "example_case": "Aerial yoga post — taken from a real session: one folder in, native pieces out",
        "example_prompt": "Unfold this folder for Instagram and LinkedIn — it has the original post image and the briefing text.",
        "example_images": ["assets/human-social-thumbs/in-post.jpg"],
        "example_images_caption": "The input: one finished post (aerial yoga, pink/lilac palette) plus a .txt brief — that’s all the skill needs.",
        "example_flow": [
            "The skill identifies the “mother art” — the hero image carrying the brand identity — and extracts its visual language (palette, mood, typography) to anchor every new piece",
            "Dispatches the generations in parallel: a 3-card Stories sequence with a narrative arc, and a LinkedIn piece reframed with a professional angle (yoga + nervous-system science)",
            "Writes a platform-specific caption per piece and a manifest.json tracing every output back to the source",
        ],
        "example_result": "Native pieces saved back into the folder — a 3-card Stories sequence and a LinkedIn feed image, each a fresh render (not a resize) with its own caption, plus the manifest.",
        "result_images": ["assets/human-social-thumbs/out-story1.jpg", "assets/human-social-thumbs/out-story2.jpg", "assets/human-social-thumbs/out-story3.jpg", "assets/human-social-thumbs/out-linkedin.jpg"],
        "result_images_caption": "The outputs: 3 sequential Stories (9:16) and the LinkedIn feed piece (16:9) — same brand language, new compositions per platform.",
        "honest": "It needs a tidy input folder — a .txt brief plus at least one image. It writes results inside that input folder (not under human-output), so point it at the right place. Captions follow the audience language; tell it if that isn’t obvious.",
    },
    {
        "name": "human-motion",
        "num": "06",
        "tagline": "Video and motion graphics from the terminal via Remotion.",
        "tools": "Claude + Remotion (Node) + Magnific / Higgsfield for stills",
        "what": "Creates motion-graphics Reels and edits existing videos — beat sheet, timeline, caption design, pacing and beat-matching — then renders MP4 with Remotion. Any AI stills (frames, textures, backgrounds) are rendered through your chosen provider before Remotion reads them.",
        "why": "Motion work usually means an editor and a timeline app. This skill turns a brief into a reproducible Remotion project, so motion graphics become code you can re-render and tweak — not a one-off manual edit that’s painful to revise.",
        "strong": "Real motion discipline: beat sheet, timeline, caption design, and a QC pass on pacing, legibility and audio sync. It generates a local Remotion project (or a reproducible technical plan) and renders MP4. It ships with a deep “decupagem” case study as a method reference.",
        "when": [
            "Motion-graphics Reels from a prompt",
            "Editing a video with titles, captions or cuts",
            "Beat-matching a cut to audio",
            "Rendering an MP4 from the terminal",
        ],
        "triggers": [
            '"Reel" / "motion graphics"',
            '"Remotion"',
            '"edit video with caption" / "beat-match"',
            '"render MP4" / "vídeo no terminal"',
        ],
        "steps": [
            "Brief — new Reel or edit?",
            "Beat sheet with timing",
            "Timeline + caption design",
            "Asset plan — render any stills",
            "Remotion project → render MP4 → QC",
        ],
        "example_case": "Nubank “This is efficiency” — taken from a real session, with the actual brief used",
        "example_prompt": "Briefing — Nubank commercial ‘This is efficiency’. Brand: Nubank, Brazilian digital bank, 100M+ clients. Visual identity: clean, spacious, solid purple #820AD1 + white/cream — no dark luxury tech, no neon glow. Format: vertical 1080×1920, 30fps, ~25s, 250px safe padding top and bottom. Structure in 7 scenes: purple opening with the giant ‘nu’ logo, two fullscreen lifestyle photos with badges, 3 ecosystem cards, a ‘100M’ typographic hero with an animated 0→100 counter, the floating-cards video fullscreen, final lockup with the white pill button ‘Open your account →’. Sound: minimal ambient electronic, BPM 90–100, whooshes on transitions, ticks on the counter — no human voice. Motion: text enters word by word, exits in alternating directions, fluid animation with no violent shake, micro-breathing on idle elements. Assets are in the nubank folder.",
        "example_flow": [
            "The skill turns the brief into a visual screenplay — 7 scenes with copy, asset and animation specs per scene — and validates the asset folder against it",
            "Processes the assets: crops the lifestyle photos to 1080×1920 frames, extracts design elements from the official screenshots",
            "Scaffolds a Remotion React project with proper animation code (frame-based interpolation, springs) and renders a test of scene 1 for approval before the full cut",
        ],
        "example_result": "A rendered MP4 (Nubank_Isso_e_Eficiencia.mp4) built scene by scene from the brief — a 25-second motion-graphics commercial that lives as code, so any scene can be tweaked and re-rendered without redoing the edit.",
        "honest": "This is the most technical skill of the set — it needs Node + npm (and Remotion) on the machine. Renders take real compute and a QC pass; it won’t skip the quality check before declaring a cut done.",
    },
    {
        "name": "human-team",
        "num": "07",
        "tagline": "A multi-agent creative team (OpenSquad) that delivers a full campaign.",
        "tools": "Claude + Magnific / Higgsfield + Notion + Playwright (optional)",
        "what": "Turns an idea, reference or existing material into a structured full production: brief, plan, dossier, concept, script, art direction, storyboard, production sheet, teaser / main / secondary assets, ads in 9:16, 4:5 and 16:9, a copy-pack, a Notion calendar and a handoff. Images via Magnific / Higgsfield; video always Higgsfield.",
        "why": "A full campaign is many roles — planner, art director, producer, social, copy. Doing it solo means dropped continuity and missing deliverables. This skill runs a coordinated agent team with human checkpoints so the whole package ships consistently.",
        "strong": "It routes straight to the creative squad (no generic menu), enforces human checkpoints and frame-approval-before-video, keeps outfit / look / product continuity across assets, and closes with a Notion-ready calendar plus a handoff. It bundles its own helper skills (image, publishing and more).",
        "when": [
            "Full campaigns end-to-end",
            "Turning a reference into a campaign",
            "Finishing an in-progress production",
            "Improving a script with the team",
            "“The whole package — images, ads, copies, emails, calendar”",
        ],
        "triggers": [
            '"full campaign" / "creative team"',
            '"OpenSquad" / "agência virtual"',
            '"campanha completa"',
            '"finish this campaign"',
        ],
        "steps": [
            "Pick the entry mode",
            "Planner scopes the package",
            "Art director sets identity + continuity",
            "Producer organizes assets and folders",
            "Social builds the calendar → handoff",
        ],
        "example_case": "Budweiser × Primavera Sound 2026 — taken from a real session",
        "example_prompt": "I want a campaign for Budweiser at Primavera Sound Barcelona 2026. Audience is 18–34 festival-goers who screenshot posters and hate corporate sponsorship aesthetics. I’ve dropped 3 visual references and the Budweiser logo in the folder — give me the concept plus 2–3 key visuals to validate the direction before we expand.",
        "example_images": ["assets/human-team-refs/ref-1.jpg", "assets/human-team-refs/ref-2.jpg", "assets/human-team-refs/ref-3.jpg"],
        "example_images_caption": "The 3 client references dropped in the folder — BRUTAL—ISM, (FAUX) and the DEEKAPZ ticket — the poster language the audience already worships.",
        "example_flow": [
            "The squad reads the brief and references, then locks a single ownable concept — “THE LOUDEST COLOUR”: the whole world is black-and-white grain, the only thing in colour is Budweiser red",
            "The Art Director sets the system (giant condensed red type, em-dash break, single-colour discipline) and the Producer runs the renders — auditing each frame, rejecting and re-rendering the portrait KV twice until it stopped cloning the reference",
            "Derives ads in multiple ratios (4:5, 16:9) from the approved key visuals, keeping crowd, bottle and red consistent across every piece",
        ],
        "example_result": "An approved concept plus poster-ready key visuals and ads — three KVs (the crowd, the portrait, the ticket) and 4:5 / 16:9 ad cuts, all on the single-red system, organized under human-output/team/.",
        "result_images": ["assets/human-team-thumbs/kv1-crowd.jpg", "assets/human-team-thumbs/kv2-portrait.jpg", "assets/human-team-thumbs/kv3-ticket.jpg", "assets/human-team-thumbs/ad-b-16x9.jpg"],
        "result_images_caption": "Three key visuals (the crowd · the portrait · the ticket) and the 16:9 ad cut — one red across the whole system.",
        "honest": "This is the heaviest skill — a multi-agent pipeline with checkpoints, not a quick render. It expects you to approve at each gate. Notion and the local dashboard are optional extras, not requirements.",
    },
]

CSS = """
@page {
    size: A4;
    margin: 22mm 20mm 20mm 20mm;
    @top-left { content: string(crumb); font: 600 7pt Helvetica, Arial, sans-serif; letter-spacing: 1px; color: #8a8a8a; }
    @top-right { content: "PAGE\\A " counter(page) " / " counter(pages); white-space: pre; font: 600 7pt Helvetica, Arial, sans-serif; letter-spacing: 1px; color: #8a8a8a; text-align: right; }
    @bottom-left { content: "Internal use —Eightpoint Technologies"; font: 400 7.5pt Helvetica, Arial, sans-serif; color: #999; }
    @bottom-right { content: "June 2026"; font: 400 7.5pt Helvetica, Arial, sans-serif; color: #999; }
}
body { font-family: Helvetica, Arial, sans-serif; color: #333; font-size: 10pt; line-height: 1.45; }
.crumb-set { string-set: crumb content(); display: block; font-size: 0; line-height: 0; height: 0; overflow: hidden; }
.kicker { color: #a31621; font-size: 8.5pt; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; margin: 0 0 6pt 0; }
h1 { font-size: 30pt; font-weight: 800; color: #111; margin: 0 0 14pt 0; letter-spacing: -0.5pt; }
.tagline { font-size: 14pt; color: #777; line-height: 1.45; margin: 0 0 26pt 0; max-width: 90%; }
.redrule { border: none; border-top: 1.6pt solid #a31621; margin: 0 0 22pt 0; }
.label { color: #a31621; font-size: 8.5pt; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; margin: 13pt 0 5pt 0; }
p { margin: 0 0 7pt 0; }
table.meta { margin-top: 26pt; border-collapse: collapse; }
table.meta td { padding: 9pt 0; vertical-align: top; }
table.meta td.k { width: 165pt; color: #a31621; font-size: 8.5pt; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; }
.page2, .page3 { page-break-before: always; }
h2 { font-size: 20pt; font-weight: 800; color: #111; margin: 2pt 0 8pt 0; padding-bottom: 8pt; border-bottom: 0.7pt solid #ddd; }
ul.when { margin: 2pt 0 0 0; padding: 0; list-style: none; }
ul.when li { margin: 0 0 4pt 0; padding-left: 14pt; position: relative; }
ul.when li::before { content: "•"; color: #a31621; position: absolute; left: 2pt; }
.codeblock { background: #f1f1f1; padding: 10pt 12pt; margin: 6pt 0 2pt 0; font-family: "Courier New", Courier, monospace; font-size: 9pt; color: #7a3b3b; line-height: 1.6; }
ol.steps { margin: 2pt 0 0 0; padding: 0; list-style: none; counter-reset: step; }
ol.steps li { counter-increment: step; margin: 0 0 5pt 0; padding-left: 28pt; position: relative; }
ol.steps li::before { content: "0" counter(step); color: #a31621; font-weight: 800; position: absolute; left: 0; }
.case { color: #888; font-size: 9pt; font-style: italic; margin: 0 0 6pt 0; }
.youtype { background: #f1f1f1; border-left: 2.5pt solid #a31621; padding: 12pt 14pt; margin: 6pt 0 12pt 0; font-family: "Courier New", Courier, monospace; font-size: 9.5pt; color: #444; line-height: 1.7; }
.refrow { margin: 4pt 0 4pt 0; }
.refrow img { height: 112pt; margin-right: 7pt; vertical-align: top; }
.refcap { color: #888; font-size: 8.5pt; font-style: italic; margin: 2pt 0 10pt 0; }
.resultrow { margin: 6pt 0 2pt 0; }
.resultrow img { height: 60pt; margin: 0 2.5pt 2.5pt 0; vertical-align: top; }
.honest-wrap { margin-top: 11pt; }
.honest-wrap h3 { font-size: 12pt; font-weight: 800; color: #111; margin: 0 0 8pt 0; }
.endrule { border: none; border-top: 1.2pt solid #a31621; margin: 14pt 0 0 0; }
"""

PAGE_TMPL = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>{css}</style></head>
<body>
<span class="crumb-set">HUMAN / {NAME} / TEAM BRIEFING</span>

<div class="page1">
  <p class="kicker">Internal — Human Skills Briefing</p>
  <h1>{name}</h1>
  <p class="tagline">{tagline}</p>
  <hr class="redrule">
  <p class="label">What’s Inside</p>
  <p>What this skill does, why it exists, what makes it strong, exactly when to reach for it, the phrases that trigger it, a real first-run example, and an honest note on its limits.</p>
  <table class="meta">
    <tr><td class="k">Skill</td><td>{name} · #{num} of 7</td></tr>
    <tr><td class="k">Audience</td><td>Human design &amp; creative team</td></tr>
    <tr><td class="k">Tools Used</td><td>{tools}</td></tr>
    <tr><td class="k">Time to Read</td><td>5 minutes</td></tr>
  </table>
</div>

<div class="page2">
  <p class="kicker">Skill {num}</p>
  <h2>{name}</h2>
  <p class="label">What It Does</p>
  <p>{what}</p>
  <p class="label">Why It Was Built</p>
  <p>{why}</p>
  <p class="label">What Makes It Strong</p>
  <p>{strong}</p>
  <p class="label">When To Call It</p>
  <ul class="when">{when_lis}</ul>
  <p class="label">Trigger Phrases</p>
  <div class="codeblock">{trigger_lines}</div>
  <p class="label">How It Runs</p>
  <ol class="steps">{step_lis}</ol>
</div>

<div class="page3">
  <p class="label">First Run — A Real Example</p>
  <p class="case">{example_case}</p>
  <p><strong>{action_label}:</strong></p>
  <div class="youtype">{action_text}</div>
  {example_images_html}
  <p><strong>What happens next:</strong></p>
  <ul class="when">{example_flow_lis}</ul>
  <p><strong>What comes out:</strong> {example_result}</p>
  {result_images_html}
  <div class="honest-wrap">
    <h3>HONEST CALL</h3>
    <p>{honest}</p>
    <hr class="endrule">
  </div>
</div>
</body></html>
"""


def render(skill):
    html = PAGE_TMPL.format(
        css=CSS,
        NAME=skill["name"].upper(),
        name=skill["name"],
        num=skill["num"],
        tagline=skill["tagline"],
        tools=skill["tools"],
        what=skill["what"],
        why=skill["why"],
        strong=skill["strong"],
        when_lis="".join(f"<li>{w}</li>" for w in skill["when"]),
        trigger_lines="<br>".join(skill["triggers"]),
        step_lis="".join(f"<li>{s}</li>" for s in skill["steps"]),
        example_case=skill["example_case"],
        example_prompt=skill["example_prompt"],
        action_label=skill.get("example_action_label", "You type"),
        action_text=(skill["example_prompt"] if skill.get("example_action_quoted") is False
                     else f'&ldquo;{skill["example_prompt"]}&rdquo;'),
        example_images_html=(
            '<div class="refrow">' + "".join(f'<img src="{p}">' for p in skill["example_images"]) + "</div>"
            + f'<p class="refcap">{skill.get("example_images_caption", "")}</p>'
        ) if skill.get("example_images") else "",
        result_images_html=(
            '<div class="resultrow">' + "".join(f'<img src="{p}">' for p in skill["result_images"]) + "</div>"
            + f'<p class="refcap">{skill.get("result_images_caption", "")}</p>'
        ) if skill.get("result_images") else "",
        example_flow_lis="".join(f"<li>{f}</li>" for f in skill["example_flow"]),
        example_result=skill["example_result"],
        honest=skill["honest"],
    )
    out = os.path.join(OUT_DIR, f"{skill['name']}-briefing.pdf")
    HTML(string=html, base_url=OUT_DIR + "/").write_pdf(out)
    print("wrote", out)


if __name__ == "__main__":
    for s in SKILLS:
        render(s)
