# AGENTS.md — Jindal Stainless case study, shared rules

Antigravity reads this file automatically and applies it to every agent in this
project. Rules here don't need to be repeated inside each individual agent file.

## Non-negotiables for every agent

- **STRICT: Do NOT use Opus 4.6 (inherit model) unless it is absolutely necessary
  for judgment, verification, or critic/integrator-level review.** All routine
  research, drafting, reading, and exploration MUST be done on Flash or Pro.
  Opus is reserved ONLY for the critic, integrator, and final verification passes.
- Never state a fact about Jindal Stainless, the stainless steel industry, or the
  competition rules from memory. Everything traces to a file in `research/`.
- Check `research/_index.md` before starting any research task, self-search or deep
  research. Reuse an existing file before creating a new one.
- Don't return a task as "done" just because you produced output. Check it against
  what was actually asked before handing it back — see each agent's own
  "Definition of done" section for specifics.
- This is a competition submission. Format, word/page limits, and evaluation criteria
  (captured from `competition-brief.md` by explorer) are hard constraints, not
  suggestions.

## Project structure

- `competition-brief.md` — the Unstop brief, pasted by the user
- `research/` — one file per topic, `_index.md` tracks all of them
- `ideation/` — ideator/critic rounds, until an angle is approved
- `case-study/draft.md` → `case-study/final.md`

## Model tiers in this tree

Explorer and researcher run on `flash` (cheap model, still thorough). Worker and
ideator run on `pro` (balanced). Critic and integrator run on `inherit` (uses the
user's selected model — typically the strongest available) — they are the two
judgment layers in this tree and are where quality actually gets decided.
