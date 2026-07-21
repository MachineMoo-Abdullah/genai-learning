# API Documentation

## Prompt 1
```
You are a technical writer. Document only what this code actually does — do not invent parameters or behaviors:

{{ENDPOINT_CODE}}

Output: method + path, one-line description, auth requirement, a parameters table, a request example, a response fields table, a success example, and an errors table.
```

## Prompt 2
```
Generate reference documentation for this function/endpoint for a developer who has never seen the codebase:

{{CODE}}

Include: signature, description, parameters (name/type/required/description), return value/response shape, possible errors, and one realistic usage example. Mark anything not determinable from the code as "not specified in source."
```
