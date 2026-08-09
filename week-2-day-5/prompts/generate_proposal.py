import json


def build_proposal_prompt(
    company_info,
    client_info,
    analysis,
    solution,
):
    return f"""
You are an expert B2B sales proposal writer.

Write a highly personalized sales proposal.

COMPANY INFORMATION
{json.dumps(company_info, indent=2)}

CLIENT INFORMATION
{json.dumps(client_info, indent=2)}

CLIENT ANALYSIS
{json.dumps(analysis, indent=2)}

PROPOSED SOLUTION
{json.dumps(solution, indent=2)}

Write the proposal using exactly these sections:

# Sales Proposal

## Executive Summary

## Understanding Your Requirements

## Proposed Solution

## Key Features

## Business Benefits

## Implementation Plan

## Timeline

## Investment

## Why Choose Us?

## Next Steps

Requirements:

- Address the client by name where appropriate.
- Connect the proposal directly to the client's requirements.
- Mention the client's budget in the Investment section.
- Use the requested tone.
- Be persuasive but professional.
- Do not make unsupported claims.
- Do not invent company history or client information.
- Do not use placeholder text.
- Make the proposal read like a real business proposal.
"""