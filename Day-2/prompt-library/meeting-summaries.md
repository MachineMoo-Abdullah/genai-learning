# Meeting Summary Prompt

Best for: turning raw notes or a transcript into a clean, actionable summary.

## The Prompt

```
You are summarizing a meeting for people who were NOT there and need to understand what was decided and what to do next, without reading the full transcript.

## Raw input
{{PASTE_TRANSCRIPT_OR_RAW_NOTES}}

## Task
Extract and organize:
1. Decisions made (not just discussed — actual decisions)
2. Action items, each with an owner and deadline if stated (mark "unassigned"/"no deadline given" if missing — do not invent one)
3. Open questions / unresolved issues that need follow-up
4. Key context worth preserving that isn't a decision or action item (e.g. important disagreements, reasoning behind a decision)

## Output format

### Summary
2-4 sentences: what was this meeting about and what was the overall outcome.

### Decisions
- [decision] — brief rationale if given

### Action items
| Owner | Action | Deadline |
|---|---|---|

### Open questions
- [question / unresolved issue]

### Notable context
- [anything important that doesn't fit above]

## Rules
- Do not invent owners, deadlines, or decisions that weren't actually stated — mark them as missing instead.
- Do not include a "notable context" item just to fill the section — omit it if there's nothing worth preserving.
- Preserve disagreements/dissent if they occurred — don't smooth them into false consensus.
- Keep it dense: this should be readable in under a minute.
```

## Why this works
- Separating **decisions** from **action items** from **open questions** prevents the common failure of a flat, hard-to-scan bullet dump.
- Explicitly forbidding **invented owners/deadlines** is critical — this is the single most damaging hallucination type in meeting summaries, since people will act on wrong assignments.
- Requiring **preserved disagreement** stops the model from over-smoothing a summary into artificial consensus that misrepresents what actually happened.
