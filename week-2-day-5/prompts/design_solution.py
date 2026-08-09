import json


def build_solution_prompt(company_info, client_info, analysis):
    analysis_json = json.dumps(analysis, indent=2)

    return f"""
You are a senior business solution architect.

Design a practical solution based on the company information and the client's analyzed requirements.

COMPANY INFORMATION
{json.dumps(company_info, indent=2)}

CLIENT INFORMATION
{json.dumps(client_info, indent=2)}

CLIENT ANALYSIS
{analysis_json}

Create a solution containing:

1. Proposed solution
2. Features
3. Implementation approach
4. Expected benefits
5. Timeline
6. Deliverables

Important:
- The solution must directly address the client's requirements.
- Use only services that the company actually provides.
- Do not invent certifications, customers, technologies, statistics, or guarantees.
- Keep the solution realistic for the stated budget.
- Make the output useful for a professional sales proposal.
"""
