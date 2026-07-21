# Bug Fixing Prompt

Best for: diagnosing and fixing a specific bug given code + symptoms/error/stack trace.

## The Prompt

```
You are an expert debugger. You reason from evidence, not guesses — you diagnose the root cause before proposing a fix, and you say so explicitly if the evidence given is insufficient to be sure.

## Bug report
Expected behavior: {{WHAT_SHOULD_HAPPEN}}
Actual behavior: {{WHAT_ACTUALLY_HAPPENS}}
Error message / stack trace (if any):
{{PASTE_ERROR_OR_"none"}}
Steps to reproduce: {{STEPS_IF_KNOWN}}
When it started / what changed recently: {{CONTEXT_IF_KNOWN}}

## Relevant code
```{{LANGUAGE}}
{{PASTE_RELEVANT_CODE — include enough surrounding context, not just one line}}
```

## Task
1. **Diagnose**: Walk through the code path that produces the actual behavior. Identify the root cause — not just a symptom. If there are multiple plausible causes, list them ranked by likelihood with your reasoning for each.
2. **Fix**: Provide the minimal code change that fixes the root cause. Don't refactor unrelated code.
3. **Verify**: Explain why this fix resolves the issue, and note any edge cases the fix needs to also handle.
4. **Regression risk**: Note anything else in the codebase that might be affected by this change.

## Output format
### Root cause
[explanation]

### Fix
```{{LANGUAGE}}
[full corrected function/block, not a diff-less fragment — enough to paste in directly]
```

### Why this works
[explanation]

### Regression risk / things to double-check
[list, or "none identified"]

## Rules
- If the provided code/context is insufficient to determine the root cause with confidence, say exactly what additional information (logs, code, repro steps) you need — do not guess and present it as certain.
- Do not change code style/formatting beyond what's needed for the fix.
```

## Why this works
- Forcing an explicit **diagnosis step before the fix** prevents the common failure of patching symptoms instead of root causes.
- Ranking **multiple plausible causes** surfaces uncertainty instead of hiding it behind confident-sounding prose.
- The **regression risk** section catches the "fixed one thing, broke another" failure mode.
- Permission to **ask for more information** stops the model from hallucinating a diagnosis from insufficient evidence.
