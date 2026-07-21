# Code Generation

## Prompt 1
```
You are a senior {{LANGUAGE}} engineer. Write {{WHAT_TO_BUILD}} that does the following: {{REQUIREMENTS}}. Handle edge cases explicitly (empty input, null, invalid types). Return only the complete, ready-to-run code in a single code block, followed by a short list of any assumptions you made.
```

## Prompt 2
```
Write production-quality {{LANGUAGE}} code for: {{TASK_DESCRIPTION}}. Constraints: {{CONSTRAINTS}}. Match this existing style: {{EXISTING_CODE_SNIPPET}}. Include error handling for all edge cases. Output: one paragraph explaining your approach, then the full code block, then how to test it.
```
