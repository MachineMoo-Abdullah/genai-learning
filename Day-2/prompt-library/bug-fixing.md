# Bug Fixing

## Prompt 1
```
You are an expert debugger. Expected behavior: {{EXPECTED}}. Actual behavior: {{ACTUAL}}. Error/stack trace: {{ERROR}}. Relevant code:

{{CODE}}

Diagnose the root cause first, then give the minimal fix as a full corrected code block, then explain why it works and any regression risk.
```

## Prompt 2
```
Here is a bug: {{BUG_DESCRIPTION}}. Code:

{{CODE}}

Walk through the execution path to find the root cause. If multiple causes are possible, rank them by likelihood. Then provide the fixed code and note any edge cases the fix must also handle.
```
