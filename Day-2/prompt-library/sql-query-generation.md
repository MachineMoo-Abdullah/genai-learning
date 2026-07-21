# SQL Query Generation

## Prompt 1
```
You are a senior database engineer. Dialect: {{SQL_DIALECT}}. Schema:

{{SCHEMA}}

Write a query that: {{REQUEST}}. Use only the given tables/columns. State any assumptions about ambiguous terms, then output the formatted query, then a brief explanation.
```

## Prompt 2
```
Given this schema:

{{SCHEMA}}

Write an efficient {{SQL_DIALECT}} query to: {{REQUEST}}. Use explicit JOINs and qualified column names. Flag any potential performance issues (missing indexes, full scans) given table sizes: {{ROW_COUNTS}}.
```
