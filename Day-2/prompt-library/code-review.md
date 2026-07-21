# Code Review

## Prompt 1
```
You are a principal engineer reviewing this {{LANGUAGE}} code for correctness, security, performance, and maintainability:

{{CODE_OR_DIFF}}

For each issue found, give: severity (Critical/High/Medium/Low), the problem, why it matters, and a concrete fix. End with a one-line merge verdict.
```

## Prompt 2
```
Review the following pull request diff as a strict senior reviewer. Focus only on bugs, security issues, and missing edge-case handling — ignore style/formatting.

{{DIFF}}

Output a numbered list of issues ranked by severity, each with a suggested fix.
```
