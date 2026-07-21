# Email Writing Prompt

Best for: drafting professional emails developers commonly need (status updates, incident comms, asking for a review, pushing back on scope, etc.).

## The Prompt

```
You are helping me write a professional email. Write in a natural, direct, human voice — not corporate-sounding, no filler phrases like "I hope this finds you well" unless I ask for a formal tone.

## Situation
Who I'm emailing and our relationship: {{E.G. "my manager", "a teammate on another team", "a vendor"}}
Goal of this email: {{WHAT_I_WANT_TO_HAPPEN_AS_A_RESULT}}
Key facts/context to include: {{BULLET_LIST_OF_FACTS}}
Tone: {{CASUAL / NEUTRAL / FORMAL / URGENT}}
Length: {{SHORT (3-5 sentences) / MEDIUM / DETAILED}}

## Requirements
1. Lead with the point — don't bury the ask or the key information in paragraph three.
2. One clear call-to-action or next step, stated explicitly (what I need from them, by when, if applicable).
3. Match the specified tone and length exactly — don't pad a "short" request into five paragraphs.
4. No corporate filler ("touching base", "circle back", "per my last email") unless I explicitly used that voice in my context.
5. If information needed to write this well is missing (e.g. a deadline, a specific error, a name), ask me rather than inventing it.

## Output format
Subject: [subject line]

[email body]

(If useful, offer one alternate version with a different tone/framing — e.g. more assertive vs. more collaborative — labeled clearly.)
```

## Why this works
- Specifying **goal + audience relationship** separately from tone lets the model calibrate directness correctly (an email to your manager reads differently than one to a vendor, even at the same "tone" setting).
- Banning **corporate filler by default** is necessary because models default to it heavily; explicitly forbidding it produces noticeably more natural output.
- **"Ask rather than invent"** stops the model from fabricating deadlines, names, or specifics you didn't provide.
- Offering an **alternate version** is useful specifically for higher-stakes emails (pushback, escalation) where tone choice matters.
