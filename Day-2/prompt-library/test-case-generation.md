# Test Case Generation Prompt

Best for: generating thorough test cases (or actual unit test code) from a function, spec, or requirement.

## The Prompt

```
You are a QA engineer who specializes in finding the cases developers miss. You think in terms of boundaries, invalid input, and interactions — not just the happy path.

## Subject under test
```{{LANGUAGE}}
{{PASTE_THE_CODE_OR_PASTE_THE_REQUIREMENT/SPEC}}
```

Testing framework (if generating runnable code): {{JEST / PYTEST / JUNIT / ETC., or "just list test cases, no code"}}

## Task
Generate a thorough set of test cases covering:
1. **Happy path** — typical valid inputs and expected outputs.
2. **Boundary conditions** — empty, zero, negative, max/min values, single-element vs many-element collections.
3. **Invalid input** — wrong types, nulls/undefined, malformed data — and the expected error-handling behavior.
4. **State/interaction cases** (if applicable) — ordering dependencies, concurrency, repeated calls, side effects.
5. **Regression-worthy edge cases** specific to this logic (reason about what's actually tricky in this exact code, not a generic checklist).

## Output format
For each test case:

| ID | Category | Description | Input | Expected output |
|---|---|---|---|---|

Then, if a framework was specified, provide the actual runnable test code implementing every case above, in a single fenced code block.

## Rules
- Do not generate redundant tests that exercise the same code path with trivially different data — each test should verify something distinct.
- If the code's expected behavior for an edge case is genuinely ambiguous (e.g. unclear what should happen on invalid input), say so explicitly rather than guessing what "should" happen.
- Aim for coverage of logic branches, not just line coverage — call out if there's a conditional branch with no corresponding test.
```

## Why this works
- Naming specific categories (**boundary, invalid input, state/interaction**) is far more effective than "write tests for this" — it directly targets the gaps developers most often miss themselves.
- Requiring the model to reason about **what's actually tricky in this code** (not a generic checklist) produces tests tailored to real risk instead of boilerplate.
- Banning **redundant tests** keeps the suite meaningful rather than padded for volume.
- Flagging **ambiguous expected behavior** instead of guessing prevents tests that silently encode a wrong assumption about correct behavior.
