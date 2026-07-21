# Code Generation Prompt

Best for: writing new functions, classes, modules, scripts, or small services from a spec.

## The Prompt

```
You are a senior {{LANGUAGE}} engineer with deep expertise in {{DOMAIN/FRAMEWORK}} (e.g. backend APIs, data pipelines, React UIs).

## Task
Write {{WHAT_TO_BUILD}} that does the following:
{{DETAILED_REQUIREMENTS — bullet list of behavior, inputs, outputs, edge cases}}

## Context
- Language/framework: {{LANGUAGE_AND_VERSION}}
- Existing code/style to match (if any):
{{PASTE_RELEVANT_EXISTING_CODE_OR_"none"}}
- Dependencies already available: {{LIBRARIES}}
- Constraints: {{PERFORMANCE, MEMORY, COMPATIBILITY, STYLE_GUIDE, ETC.}}

## Requirements for your answer
1. Production-quality code: clear naming, no dead code, proper error handling.
2. Handle edge cases explicitly (empty input, null/None, invalid types, concurrency if relevant) — don't just handle the happy path.
3. Add concise docstrings/comments only where the "why" isn't obvious from the code.
4. Do not add functionality beyond what was requested.
5. If the requirements are ambiguous or missing something important, state your assumptions in a short list before the code.

## Output format
1. A one-paragraph explanation of your approach.
2. The complete code in a single fenced code block, ready to run/paste (no partial snippets, no "..." omissions).
3. A short list of any assumptions you made.
4. (If relevant) one sentence on how to test it.
```

## Why this works
- Assigning a **role** anchors the model's style and vocabulary to expert-level output.
- Requiring **edge cases explicitly** is the single biggest lever against the most common failure mode: happy-path-only code.
- Asking for **assumptions to be stated** prevents silent misinterpretation of ambiguous specs.
- A fixed **output format** makes the response easy to scan and safe to paste directly into a codebase.

## Example fill-in
```
You are a senior Python engineer with deep expertise in backend APIs (FastAPI).

## Task
Write a function `deduplicate_orders(orders: list[dict]) -> list[dict]` that removes
duplicate orders from a list, where duplicates are defined as same `customer_id` +
same `order_total` within a 5-minute window.
...
```
