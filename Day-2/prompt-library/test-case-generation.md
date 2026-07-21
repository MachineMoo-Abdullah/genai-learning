# Test Case Generation

## Prompt 1
```
You are a QA engineer. Subject under test:

{{CODE_OR_SPEC}}

Generate test cases covering happy path, boundary conditions, invalid input, and state/interaction cases. Output as a table: ID, category, description, input, expected output.
```

## Prompt 2
```
Generate {{TEST_FRAMEWORK}} unit tests for this code:

{{CODE}}

Cover every logic branch, including edge cases and error conditions. Avoid redundant tests. Output runnable test code in a single code block.
```
