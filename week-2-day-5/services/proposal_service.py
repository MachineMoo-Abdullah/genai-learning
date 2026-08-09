from prompts.analyze_client import build_analysis_prompt
from prompts.design_solution import build_solution_prompt
from prompts.generate_proposal import build_proposal_prompt

from services.json_parser import parse_json_response
from services.llm_service import LLMService


MAX_INPUT_LENGTH = 10000


class ProposalService:

    def __init__(self):
        self.llm = LLMService()

    @staticmethod
    def validate_inputs(
        company_name,
        company_description,
        products_services,
        client_name,
        client_requirements,
        budget,
        tone,
    ):
        if not company_name or not company_name.strip():
            raise ValueError("Company name is required.")

        if not client_requirements or not client_requirements.strip():
            raise ValueError("Client requirements are required.")

        fields = {
            "Company Name": company_name,
            "Company Description": company_description,
            "Products / Services": products_services,
            "Client Name": client_name,
            "Client Requirements": client_requirements,
            "Budget": budget,
        }

        for field_name, value in fields.items():
            if value and len(value) > MAX_INPUT_LENGTH:
                raise ValueError(
                    f"{field_name} is too long. "
                    f"Please keep it under {MAX_INPUT_LENGTH} characters."
                )

        if not tone:
            raise ValueError("Please select a preferred tone.")

    def analyze_client(
        self,
        company_name,
        company_description,
        products_services,
        client_name,
        client_requirements,
        budget,
        tone,
    ):
        prompt = build_analysis_prompt(
            company_name,
            company_description,
            products_services,
            client_name,
            client_requirements,
            budget,
            tone,
        )

        raw_json = self.llm.generate_json(prompt)

        return parse_json_response(raw_json)

    def design_solution(
        self,
        company_name,
        company_description,
        products_services,
        client_name,
        client_requirements,
        budget,
        tone,
        analysis,
    ):
        company_info = {
            "company_name": company_name,
            "company_description": company_description,
            "products_services": products_services,
        }

        client_info = {
            "client_name": client_name,
            "requirements": client_requirements,
            "budget": budget,
            "tone": tone,
        }

        prompt = build_solution_prompt(
            company_info,
            client_info,
            analysis,
        )

        return self.llm.generate_text(prompt)

    def build_proposal_prompt(
        self,
        company_name,
        company_description,
        products_services,
        client_name,
        client_requirements,
        budget,
        tone,
        analysis,
        solution,
    ):
        company_info = {
            "company_name": company_name,
            "company_description": company_description,
            "products_services": products_services,
        }

        client_info = {
            "client_name": client_name,
            "requirements": client_requirements,
            "budget": budget,
            "tone": tone,
        }

        return build_proposal_prompt(
            company_info,
            client_info,
            analysis,
            solution,
        )

    def stream_proposal(self, prompt):
        return self.llm.stream_text(prompt)