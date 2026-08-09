
---

# 14. `Week2_Day5_Business_AI.md`

```markdown
# Week 2 - Day 5: Business AI

## What are business applications of Generative AI?

Generative AI can create useful business content such as:

- Sales proposals
- Marketing content
- Product descriptions
- Customer support responses
- Reports
- Business emails
- Meeting summaries
- Advertisements
- Documentation
- Personalized recommendations

It can reduce repetitive work and help employees create content faster.

---

## What is structured prompting?

Structured prompting means giving an LLM a clear format, instructions, context, constraints, and expected output.

For example, instead of saying:

"Analyze this client."

we can specify:

- What information the model should analyze.
- What fields it should return.
- What format should be used.
- What information it should not invent.

This makes the response more predictable.

---

## Why is JSON useful when working with LLMs?

JSON allows an application to treat an LLM response as structured data.

For example:

```json
{
    "client_needs": [
        "AI customer support"
    ],
    "pain_points": [
        "Slow customer response"
    ]
}