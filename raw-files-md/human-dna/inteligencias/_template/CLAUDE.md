# CLAUDE.md — {{BRAND_NAME}}

This file guides Claude Code in working with the **{{BRAND_NAME}}** brand.

Before creating, editing or auditing any piece for this brand, read the entire file:

```text
resultado/DNA.md
```

The `DNA.md` is the source of truth. It defines visual style, tone of voice, references, anti-references, tools, workflow and quality criteria. The `resultado/DNA.pdf` is the presentable editorial version. This `CLAUDE.md` is just the operational layer for Claude Code.

---

## Brand summary

Fill in this block from the `DNA.md` when the project is created.

```text
Brand: {{BRAND_NAME}}
What it does: {{BRAND_DOES}}
Promise: {{BRAND_PROMISE}}
Aesthetic: {{VISUAL_ANCHOR}}
Voice: {{VOICE_ANCHOR}}
Workflow: {{WORKFLOW_SUMMARY}}
```

## How to act

1. Read the entire `DNA.md` before responding.
2. Before creating, identify which section of the DNA governs the request: visual, voice, audience, workflow, channel, image or behavior.
3. Use the DNA's rules to create, review or refine pieces.
4. If the user asks for something that contradicts the DNA, flag the tension and propose a coherent path.
5. If the user approves a change in style, voice or workflow, update the `DNA.md`.
6. After any relevant adjustment, regenerate `resultado/DNA.pdf`.
7. After any relevant adjustment, test by generating a new short version.
8. If the request involves real image or video, follow the project premise: Higgsfield CLI as the main base.

---

## Quick brand rules

Replace the placeholders with specific synthesis from the DNA.

### Visual

```text
Core palette: {{PALETTE_SUMMARY}}
References: {{VISUAL_REFERENCES}}
Anti-references: {{VISUAL_ANTI_REFERENCES}}
Photographic direction: {{PHOTO_DIRECTION}}
```

### Voice

```text
The brand sounds like: {{VOICE_DESCRIPTION}}
Uses: {{PREFERRED_WORDS}}
Avoids: {{AVOIDED_WORDS}}
Never use: {{FORBIDDEN_CONSTRUCTIONS}}
```

### Workflow

```text
How a piece is born: {{WORKFLOW_STEPS}}
Main tools: {{TOOLS}}
Steps with human review: {{HUMAN_REVIEW_GATES}}
```

## Natural commands

The user can ask:

```text
create a post following my DNA
write an email in the brand's tone
audit this piece against the DNA
adjust the tone to be less formal
refine the DNA with this feedback
test my DNA with a small piece
```

## Testing rule

When the DNA is freshly created, make a small piece to validate adherence:

- caption;
- short email;
- bio;
- simple ad;
- post idea;
- visual prompt.

Then ask what landed and what fell off. Approved feedback becomes an adjustment to the `DNA.md`.

## Refinement rule

Feedback doesn't stay loose in the conversation. Turn feedback into a rule.

Examples:

- "too formal" -> adjust the register ruler and voice examples.
- "generic" -> reinforce proprietary vocabulary, anti-patterns and references.
- "doesn't feel like the brand" -> revise the anchor aesthetic, approved examples and quality criteria.
- "image off-style" -> update photographic direction and engine instructions.

After the adjustment, generate a second short version to prove the improvement.

## Flow completion

Only consider the flow complete if:

- `resultado/DNA.md` exists;
- `resultado/DNA.pdf` exists;
- this `CLAUDE.md` is personalized;
- a small piece was tested;
- feedback was applied or the user confirmed adherence;
- the user knows how to ask for creation, audit and refinement.
