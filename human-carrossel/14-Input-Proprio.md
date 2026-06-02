# 14 — Carousel from a topic or original content

This mode exists for when the person doesn't want to wait for the news feed. They can ask in a simple way:

```text
/carrossel I want a carousel about electric bicycles in São Paulo
```

or paste a text, an idea, a short brief, a transcript, a stand-alone news item, a long post or a draft. The agent must not require the person to know how to structure the carousel. The system's job is to research, frame, organize and turn the idea into a finished piece.

---

## When to activate

Activate this mode when the request:

- brings a simple topic;
- pastes original content;
- asks for a carousel without mentioning the News Feed, R1, R2 or a specific news item;
- says "I want to talk about", "make a carousel about", "turn this into a carousel";
- asks for a one-off piece outside the daily routine.

If the request is news swap, re-render, specific slide or automatic routine, use `15-Como-usar.md`.

---

## Main rule

Simple input is not a weak brief. Simple input is a signal that the agent needs to do the heavy lifting.

With a short sentence, the agent must:

1. understand the subject;
2. research current context;
3. separate data from opinion;
4. find a human or cultural tension;
5. pick the best angle;
6. create a strong headline;
7. assemble the 9-slide narrative architecture;
8. suggest a visual per slide;
9. render or prepare for render.

Only ask if something is missing that blocks execution, like an active brand/project or a mandatory audience. Don't ask "what angle do you want?" when the system itself can figure it out.

---

## Internal pipeline

Use these roles, even if they don't surface to the user:

| Role | Function in this mode |
|---|---|
| Scout | Researches the topic, trends, recent data, examples and counter-examples. |
| Creative Director | Picks the tension, the big idea and the editorial framing. |
| Scriptwriter | Writes headline, slides and caption. |
| Art Director | Defines visual direction, metaphor and image per slide. |
| Producer | Organizes what needs to be rendered and saves the local state. |
| Social Manager | Closes caption, CTA, format and status for publishing. |

The user sees a simple delivery. Complexity stays behind the scenes.

---

## Flow for a short topic

Example input:

```text
/carrossel I want a carousel about electric bicycles in São Paulo
```

Execute:

1. **Silently clarify the likely scope.**
   - Topic: electric bicycles.
   - Local angle: São Paulo.
   - Possible tensions: mobility, cost, safety, traffic, legislation, delivery riders, bike lanes, theft, sustainability.

2. **Research before writing.**
   - Search recent, reliable sources.
   - Look for local data where it exists.
   - Look for signs of real behavior: complaints, debates, trends, doubts.
   - If there isn't enough recent data, declare it in the internal logic and use a more conceptual angle.

3. **Pick a winning angle.**
   The angle needs to be more specific than the topic.

   Bad:
   ```text
   Electric bicycles are growing in São Paulo.
   ```

   Better:
   ```text
   The e-bike has become a practical answer for a city that got expensive, gridlocked and impatient.
   ```

4. **Build the 9-slide structure.**
   - Slide 1: headline with tension.
   - Slides 2-3: problem or cultural change.
   - Slides 4-6: explanation, evidence, mechanism.
   - Slides 7-8: practical consequence or new behavior.
   - Slide 9: brand signature with featured logo/name and short CTA.

5. **Generate the caption.**
   The caption should provide context, not repeat the slides.

6. **Create visual direction.**
   Each slide needs a visual function. Don't use a generic image.

7. **If there's a configured environment**, proceed to render with the project's visual engine.
   If not, deliver the copy + visual plan and guide setup.

---

## Flow for pasted content

When someone pastes a text, don't mechanically summarize. First find:

- central thesis;
- most interesting tension;
- repeated parts;
- points that become slides;
- data that needs verification;
- strong sentences that can become a headline;
- gaps that need complementary research.

Then transform into:

- headline;
- 9-slide narrative architecture;
- caption;
- visual direction;
- render checklist.

---

## Minimum output without render

When there's still no setup for the brand, Notion, Drive or Higgsfield, deliver:

```text
Headline:

Slides:
1. ...
2. ...
...
9. ...

Caption:

Visual direction:
- Slide 1:
- Slide 2:
...

Render checklist:
- 3:4 format via Higgsfield (`--aspect_ratio "3:4"` + `--resolution "2k"`), keeping the original downloaded PNG without normalizing/cropping;
- 9 slides;
- palette;
- typography;
- images/metaphors per slide;
- cover as master reference + visual refs on every internal slide;
- no visible slide number;
- final CTA.
```

Don't block creation just because the visual automation isn't configured yet.

---

## Integration with the Local Routine

When R2 is configured, it must accept a first message in natural language.

Examples:

```text
I want a carousel about electric bicycles in São Paulo
```

```text
turn this text into a carousel: [pasted text]
```

```text
--topic="Claude Opus 4.7 and the impact on creative teams"
```

In these cases, the Routine creates a manual pitch of the day and skips the News Feed dependency. The rest of the pipeline stays the same: research, headline, narrative architecture, visual brief, render, Drive and Notion.

---

## Quality criteria

A carousel from original input is only good if:

- it doesn't look like a school summary;
- it has a specific angle;
- it has tension or discovery;
- each slide advances the idea;
- the headline promises something the slides deliver;
- the caption complements;
- the visual helps understanding, not just decorates;
- the CTA closes with a clear action and the last slide keeps the brand as the protagonist;
- any important factual data has been verified.
