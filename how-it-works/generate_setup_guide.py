# -*- coding: utf-8 -*-
"""Generates the Human Skills — Setup & Render Guide PDF (WeasyPrint).

Matches the house style of generate_briefings.py (Eightpoint red, Helvetica, A4).

Run:  DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib ../.venv-pdf/bin/python generate_setup_guide.py
"""
import os
from weasyprint import HTML

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ---- Shared house style (kept in sync with generate_briefings.py) ----
CSS = """
@page {
    size: A4;
    margin: 22mm 20mm 20mm 20mm;
    @top-left { content: string(crumb); font: 600 7pt Helvetica, Arial, sans-serif; letter-spacing: 1px; color: #8a8a8a; }
    @top-right { content: "PAGE\\A " counter(page) " / " counter(pages); white-space: pre; font: 600 7pt Helvetica, Arial, sans-serif; letter-spacing: 1px; color: #8a8a8a; text-align: right; }
    @bottom-left { content: "Internal use — Eightpoint Technologies"; font: 400 7.5pt Helvetica, Arial, sans-serif; color: #999; }
    @bottom-right { content: "June 2026"; font: 400 7.5pt Helvetica, Arial, sans-serif; color: #999; }
}
body { font-family: Helvetica, Arial, sans-serif; color: #333; font-size: 10pt; line-height: 1.45; }
.crumb-set { string-set: crumb content(); display: block; font-size: 0; line-height: 0; height: 0; overflow: hidden; }
.kicker { color: #a31621; font-size: 8.5pt; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; margin: 0 0 6pt 0; }
h1 { font-size: 30pt; font-weight: 800; color: #111; margin: 0 0 14pt 0; letter-spacing: -0.5pt; }
.tagline { font-size: 14pt; color: #777; line-height: 1.45; margin: 0 0 26pt 0; max-width: 92%; }
.redrule { border: none; border-top: 1.6pt solid #a31621; margin: 0 0 22pt 0; }
.label { color: #a31621; font-size: 8.5pt; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; margin: 13pt 0 5pt 0; }
p { margin: 0 0 7pt 0; }
strong { color: #222; }
table.meta { margin-top: 26pt; border-collapse: collapse; }
table.meta td { padding: 9pt 0; vertical-align: top; }
table.meta td.k { width: 165pt; color: #a31621; font-size: 8.5pt; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; }
.newpage { page-break-before: always; }
h2 { font-size: 20pt; font-weight: 800; color: #111; margin: 2pt 0 10pt 0; padding-bottom: 8pt; border-bottom: 0.7pt solid #ddd; }
h3 { font-size: 12pt; font-weight: 800; color: #111; margin: 14pt 0 4pt 0; }
ul.when { margin: 2pt 0 7pt 0; padding: 0; list-style: none; }
ul.when li { margin: 0 0 4pt 0; padding-left: 14pt; position: relative; }
ul.when li::before { content: "\\2022"; color: #a31621; position: absolute; left: 2pt; }
.codeblock { background: #f1f1f1; padding: 10pt 12pt; margin: 6pt 0 8pt 0; font-family: "Courier New", Courier, monospace; font-size: 9pt; color: #7a3b3b; line-height: 1.7; }
.codeblock .cmt { color: #999; }
ol.steps { margin: 2pt 0 7pt 0; padding: 0; list-style: none; counter-reset: step; }
ol.steps li { counter-increment: step; margin: 0 0 7pt 0; padding-left: 28pt; position: relative; }
ol.steps li::before { content: "0" counter(step); color: #a31621; font-weight: 800; position: absolute; left: 0; }
table.paths { width: 100%; border-collapse: collapse; margin: 6pt 0 8pt 0; }
table.paths th { text-align: left; font-size: 8pt; letter-spacing: 1px; text-transform: uppercase; color: #a31621; border-bottom: 1pt solid #a31621; padding: 5pt 8pt 5pt 0; vertical-align: bottom; }
table.paths td { font-size: 9pt; padding: 7pt 8pt 7pt 0; vertical-align: top; border-bottom: 0.5pt solid #e3e3e3; line-height: 1.4; }
table.paths td.path { font-weight: 700; color: #111; width: 120pt; }
.callout { border-left: 2.5pt solid #a31621; background: #faf2f2; padding: 11pt 14pt; margin: 8pt 0 10pt 0; font-size: 9.5pt; line-height: 1.55; }
.callout strong { color: #a31621; }
.endrule { border: none; border-top: 1.2pt solid #a31621; margin: 16pt 0 0 0; }
.mini { color: #888; font-size: 8.5pt; font-style: italic; margin: 2pt 0 8pt 0; }
.shot { margin: 8pt 0 4pt 0; }
.shot img { width: 100%; border: 0.7pt solid #ddd; }
.shot-cap { color: #888; font-size: 8.5pt; font-style: italic; margin: 4pt 0 10pt 0; }
.shot-ph { margin: 8pt 0 4pt 0; border: 1pt dashed #c9a0a4; background: #faf2f2; color: #a31621;
           text-align: center; padding: 34pt 12pt; font-size: 9pt; font-weight: 700; letter-spacing: 0.5px; }
"""

REPO = "henry8work/human-skills"

HTML_DOC = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>{css}</style></head>
<body>
<span class="crumb-set">HUMAN / SETUP &amp; RENDER GUIDE / TEAM</span>

<!-- ============ COVER ============ -->
<div class="cover">
  <p class="kicker">Internal — Human Skills</p>
  <h1>Setup &amp; Render Guide</h1>
  <p class="tagline">How to install the Human Skills plugin, connect the render providers, and run the
  zero-credit Spaces flow where Claude builds every prompt and you just press play.</p>
  <hr class="redrule">
  <p class="label">What's Inside</p>
  <ul class="when">
    <li><strong>Part 1</strong> — Install the plugin in three clicks: upload one file in the Customize panel. The nine skills come inside it.</li>
    <li><strong>Part 2</strong> — The render setup every skill uses: the three paths (Magnific MCP, Hybrid Run Unlimited, Higgsfield) and why there's no raw API key.</li>
    <li><strong>Part 3</strong> — The Spaces flow: Claude writes the prompts and pre-fills a free, unlimited model; you open the link and click <em>Run Unlimited</em>.</li>
  </ul>
  <table class="meta">
    <tr><td class="k">Plugin</td><td>human-skills · v0.7.0 · nine skills</td></tr>
    <tr><td class="k">Audience</td><td>Human design &amp; creative team</td></tr>
    <tr><td class="k">Providers</td><td>Magnific (plan credits / zero-credit Spaces) · Higgsfield (paid)</td></tr>
    <tr><td class="k">Time to Read</td><td>8 minutes</td></tr>
  </table>
</div>

<!-- ============ PART 1 ============ -->
<div class="newpage">
  <p class="kicker">Part 1</p>
  <h2>Install the plugin</h2>

  <p>Human Skills ships as a <strong>single file</strong> — <code>human-skills-v0.7.0.plugin</code>. The nine skills
  — <em>human-setup, human-image, human-product-ad, human-cinematic, human-dna, human-carrossel,
  human-social, human-team, human-motion</em> — all live <strong>inside it</strong>. You install the plugin once and
  every skill comes with it. You never call a skill by name: you describe what you want — <em>"make me a key
  visual", "turn this product photo into a cinematic ad", "build a brand DNA"</em> — and Claude routes to the
  right one automatically.</p>

  <p class="label">The easy way — upload the file in Customize</p>
  <p>No terminal, no GitHub. If a teammate sent you the <code>.plugin</code> file, just upload it:</p>
  <ol class="steps">
    <li>Open <strong>Customize</strong> in the Claude desktop app.</li>
    <li>Next to <strong>Plugins pessoais</strong>, click <strong>+</strong> &rarr; <strong>Criar plugin</strong> &rarr; <strong>Fazer upload de plugin</strong>.</li>
    <li>Pick the <code>human-skills-v0.7.0.plugin</code> file. <strong>Done</strong> — "Human skills" shows up under your plugins, with all nine skills inside.</li>
  </ol>
  {install_image_html}

  <p class="label">Where the file comes from</p>
  <p>Someone on the team shares the <code>.plugin</code> with you (Slack, Drive, AirDrop) — that's the whole
  hand-off. To build a fresh one from the repo, run <code>./build-plugin.sh</code>; it writes
  <code>dist/human-skills-v0.7.0.plugin</code>, ready to upload.</p>

  <p class="label">Prerequisites (only when a skill needs them)</p>
  <ul class="when">
    <li><strong>At least one render provider</strong> — Magnific or Higgsfield (Part 2). Install the plugin first, connect a provider later; every skill checks and guides you if one is missing.</li>
    <li><strong>Node.js LTS + npm</strong> — for the Higgsfield CLI, human-motion (Remotion) and human-team helpers.</li>
    <li><strong>Python 3</strong> — for the human-social and human-dna helper scripts.</li>
  </ul>

  <p class="label">Advanced — for teammates who want one-command updates</p>
  <p>Optional, terminal-based. A GitHub marketplace lets the whole team install and update from one source:</p>
  <div class="codeblock">/plugin marketplace add {repo}<br>/plugin install human-skills@human-skills<br><span class="cmt"># later: /plugin marketplace update human-skills &amp;&amp; /reload-plugins</span></div>
  <p class="mini">For local development you can also start the CLI with <code>claude --plugin-dir /path/to/plugin-folder</code> (loads for that session only). Most people don't need either — the upload above is enough.</p>
</div>

<!-- ============ PART 2 ============ -->
<div class="newpage">
  <p class="kicker">Part 2</p>
  <h2>The render setup — three paths</h2>

  <p>Every skill that makes an image asks <strong>one question before rendering</strong>: which render
  path to use. It never assumes — you choose per job. Here are the three, and how to set each one up.</p>

  <table class="paths">
    <tr><th>Path</th><th>Cost</th><th>What it is &amp; when to use it</th></tr>
    <tr>
      <td class="path">1. Magnific MCP direct</td>
      <td>Plan credits<br>(~75 / image at 1k)</td>
      <td>Claude generates straight from chat through the Magnific MCP. Fast, no clicks. Best for one-offs and quick iterations. Uses the credits already included in your Magnific subscription — <strong>never</strong> pay-per-use money.</td>
    </tr>
    <tr>
      <td class="path">2. Magnific Hybrid — Run Unlimited</td>
      <td><strong>Zero credits</strong></td>
      <td>Claude builds a Space and pre-fills the prompts; you open the link and click <em>Run Unlimited</em>. Best for batches and zero spend. This is the flow in Part 3.</td>
    </tr>
    <tr>
      <td class="path">3. Higgsfield</td>
      <td>Paid (your Higgsfield credits)</td>
      <td>Your own Higgsfield account via its CLI. Needed for Higgsfield-exclusive models and some video. The carousel and product-ad pipelines ship with Higgsfield scripts.</td>
    </tr>
  </table>

  <p class="label">Set up Magnific (paths 1 &amp; 2) — the official MCP</p>
  <p>Magnific connects through its official MCP server with a one-time browser login. <code>mcp-remote</code> is the
  bridge that always works (including locked-down enterprise plans):</p>
  <div class="codeblock"><span class="cmt"># 1. install the bridge</span><br>npm install -g mcp-remote<br><br><span class="cmt"># 2. register the server (user scope, every project)</span><br>claude mcp add --scope user magnific-mcp -- mcp-remote https://mcp.magnific.com<br><br><span class="cmt"># 3. trigger the one-time OAuth login (browser opens, sign in, approve)</span><br>mcp-remote https://mcp.magnific.com<br><br><span class="cmt"># 4. verify</span><br>claude mcp list   <span class="cmt"># magnific-mcp ... Connected</span></div>
  <p class="mini">Each teammate connects their own Magnific account and spends their own plan credits. In a new session, <code>account_balance</code> confirms the plan and remaining credits.</p>

  <p class="label">Set up Higgsfield (path 3) — the CLI</p>
  <div class="codeblock">npm install -g @higgsfield/cli<br>higgsfield auth login        <span class="cmt"># browser/device login</span><br>higgsfield account status    <span class="cmt"># verify (there is no "whoami")</span></div>

  <div class="callout"><strong>"What about an API key?"</strong> The skills deliberately route through the
  Magnific <em>MCP</em> (your plan credits) and the Higgsfield <em>CLI</em> (your account credits) — never a raw,
  pay-per-use API. That's the whole point: you spend the subscription you already pay for, or nothing at all
  via Run Unlimited. There's no separate API billing to manage.</div>

  <p class="label">Model names (so the wrong one never gets picked)</p>
  <table class="paths">
    <tr><th>Model</th><th>Magnific (param is <code>mode</code>)</th><th>Higgsfield CLI slug</th></tr>
    <tr><td class="path">Nano Banana 2 — default image</td><td>imagen-nano-banana-2-flash</td><td>nano_banana_flash</td></tr>
    <tr><td class="path">Nano Banana Pro — max fidelity</td><td>imagen-nano-banana-2</td><td>nano_banana_2</td></tr>
    <tr><td class="path">GPT Image 2 — text/layout, carousels</td><td>gpt-2</td><td>gpt_image_2</td></tr>
    <tr><td class="path">Kling — video</td><td>kling-25 / kling-30</td><td>kling3_0</td></tr>
  </table>
  <p class="mini">Naming trap: on Higgsfield, <code>nano_banana_2</code> is "Nano Banana Pro" and <code>nano_banana_flash</code> is "Nano Banana 2". On Magnific the parameter is always <code>mode</code>, never <code>model</code>.</p>
</div>

<!-- ============ PART 3 ============ -->
<div class="newpage">
  <p class="kicker">Part 3</p>
  <h2>The Spaces flow — you just press play</h2>

  <p>This is path 2 (Magnific Hybrid, "Run Unlimited") in detail — the way to generate at
  <strong>zero credits</strong>. The split is simple: Claude does all the thinking and setup, you do one click.</p>

  <p class="label">How it works</p>
  <ol class="steps">
    <li><strong>You</strong> describe the job and pick "Hybrid / Run Unlimited" when asked the render path.</li>
    <li><strong>Claude</strong> builds a Magnific Space and pre-fills one generator node per image — each loaded with the prompt it wrote, the aspect ratio, and a <strong>free, unlimited-eligible model</strong> (Nano Banana 2 at 1k for images; a free-eligible model for video).</li>
    <li><strong>Claude</strong> shares the Space link (<code>webUrl</code>) with you.</li>
    <li><strong>You</strong> open the link in the browser, select the nodes, and click <strong>Run Unlimited</strong>. This costs <strong>zero credits</strong>.</li>
    <li><strong>Claude</strong> collects the finished images back from the Space and continues the pipeline — assembling the carousel, the ad, the social pieces, whatever the skill was doing.</li>
  </ol>

  <div class="callout">In this flow the model is <strong>always pinned to a free, unlimited option</strong> —
  Nano Banana 2 at 1k for stills, and the free-eligible models for video. You never spend credits, and you never
  write a prompt. Run Unlimited eligibility depends on your Magnific plan.</div>

  <p class="label">Direct from Claude vs. the Spaces flow</p>
  <table class="paths">
    <tr><th></th><th>MCP direct (path 1)</th><th>Spaces / Run Unlimited (path 2)</th></tr>
    <tr><td class="path">Who clicks</td><td>Nobody — Claude renders in chat</td><td>You click Run Unlimited once in the browser</td></tr>
    <tr><td class="path">Cost</td><td>Plan credits (~75/image)</td><td>Zero credits</td></tr>
    <tr><td class="path">Free models</td><td>Not available — direct can't run the free unlimited models</td><td>Yes — that's the whole point</td></tr>
    <tr><td class="path">Best for</td><td>One-offs, urgency, a single quick image</td><td>Batches, carousels, anything where you don't want to spend</td></tr>
  </table>

  <p>Both are real options and you can mix them: a quick test direct from Claude (a few credits), then
  the full batch through Spaces at zero cost. The rule of thumb — <strong>direct when it's one image and you're in a
  hurry; Spaces when it's a batch or you want to spend nothing.</strong></p>

  <p class="label">What to say to Claude</p>
  <div class="codeblock">"Use the Hybrid Run Unlimited flow — set up the Space with Nano Banana 2<br>at 1k, send me the link, I'll hit play."</div>

  <div style="margin-top:11pt">
    <h3>HONEST CALL</h3>
    <p>Run Unlimited is a browser feature — it can't be triggered through the MCP, which is exactly why the
    flow needs your one click. If your Magnific plan doesn't include unlimited on a given model, that model
    simply won't be free; Claude will tell you and offer the direct path or Higgsfield instead. Everything else —
    the prompts, the Space, collecting the results — is automated.</p>
    <hr class="endrule">
  </div>
</div>
</body></html>
"""


INSTALL_IMG = "assets/customize-upload.png"


def install_image_html():
    if os.path.exists(os.path.join(OUT_DIR, INSTALL_IMG)):
        return (f'<div class="shot"><img src="{INSTALL_IMG}"></div>'
                '<p class="shot-cap">Customize &rarr; Plugins pessoais + &rarr; Criar plugin &rarr; '
                'Fazer upload de plugin.</p>')
    return ('<div class="shot-ph">[ screenshot: Customize &rarr; Criar plugin &rarr; Fazer upload de plugin ]<br>'
            f'<span style="font-weight:400;font-style:italic">save it to how-it-works/{INSTALL_IMG} and rebuild</span></div>')


def main():
    html = HTML_DOC.format(css=CSS, repo=REPO, install_image_html=install_image_html())
    out = os.path.join(OUT_DIR, "human-skills-setup-guide.pdf")
    HTML(string=html, base_url=OUT_DIR + "/").write_pdf(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
