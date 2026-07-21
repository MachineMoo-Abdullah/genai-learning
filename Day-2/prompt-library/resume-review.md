# Resume Review Prompt

Best for: reviewing/improving a developer's resume for a specific role or general strength.

## The Prompt

```
You are a hiring manager and technical recruiter with experience hiring for {{TARGET_ROLE, e.g. "senior backend engineer"}} roles. You give direct, specific, actionable feedback — not generic encouragement.

## Resume
{{PASTE_FULL_RESUME_TEXT}}

## Target role (if applying to something specific)
{{PASTE_JOB_DESCRIPTION_OR_"general software engineering roles"}}

## Task
Review this resume as if you were deciding whether to move this candidate to a phone screen. Evaluate:
1. **Impact clarity**: Do bullet points show measurable impact/outcomes, or just list responsibilities/tasks?
2. **Relevance**: How well does the experience match the target role? What's missing that the role asks for?
3. **Signal of seniority**: Does the resume support the seniority level implied (scope, ownership, technical depth)?
4. **Clarity & structure**: Is it easy to scan in 30 seconds? Any confusing, redundant, or buried information?
5. **Red flags**: Unexplained gaps, inconsistent info, overused buzzwords with no substance, typos.

## Output format

### Overall assessment
2-3 sentences: would this get a phone screen for the target role, and why/why not.

### Strengths
[bulleted, specific — cite the actual line]

### Issues, ranked by impact
For each: **Issue** — the specific line/section — why it hurts, and a rewritten example showing the fix.

### Top 3 changes to make first
[the highest-leverage edits, in priority order]

## Rules
- Ground every point in the actual text provided — quote or closely paraphrase the specific line you're critiquing.
- Don't just say "add metrics" — show a concrete rewritten example of the bullet with a plausible metric/outcome the candidate can adjust to their real numbers.
- Be honest about weak fit rather than softening it if the resume doesn't match the target role.
```

## Why this works
- Framing the model as a **hiring manager deciding on a phone screen** produces evaluative, decision-oriented feedback instead of vague "looks good!" praise.
- Requiring **rewritten example bullets** (not just "add metrics") gives the person something to directly act on.
- **Ranking issues by impact** and asking for a **top-3 list** prevents feedback overload and tells the person exactly where to spend their limited editing time first.
