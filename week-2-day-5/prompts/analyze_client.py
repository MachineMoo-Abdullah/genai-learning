def build_analysis_prompt(
    company_name,
    company_description,
    products_services,
    client_name,
    client_requirements,
    budget,
    tone,
):
    return f"""
You are a professional B2B sales consultant.

Analyze the prospective client's requirements and identify what they actually need.

COMPANY INFORMATION
Company Name: {company_name}
Company Description: {company_description}
Products / Services: {products_services}

CLIENT INFORMATION
Client Name: {client_name}
Client Requirements: {client_requirements}
Budget: {budget}
Preferred Tone: {tone}

Return ONLY valid JSON with exactly these fields:

{{
    "client_needs": [],
    "pain_points": [],
    "recommended_services": [],
    "key_benefits": [],
    "target_outcomes": []
}}

Rules:
- client_needs must contain specific needs identified from the client's requirements.
- pain_points must describe business problems the client may be facing.
- recommended_services must only recommend services relevant to the company.
- key_benefits must explain practical business value.
- target_outcomes must describe measurable or meaningful results.
- Do not invent facts about the client.
- Keep every list concise and useful.
"""