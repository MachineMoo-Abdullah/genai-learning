import os
import time
from pathlib import Path

import gradio as gr

from services.proposal_service import ProposalService


from pathlib import Path

# Get the folder containing app.py
BASE_DIR = Path(__file__).resolve().parent

# Always save inside Week2-Day5/outputs/proposals/
OUTPUT_DIR = BASE_DIR / "outputs" / "proposals"

# Create the folder if it doesn't exist
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

service = ProposalService()


def save_proposal_files(proposal, client_name):

    if not proposal or not proposal.strip():
        raise ValueError("Cannot save an empty proposal.")

    safe_name = "".join(
        c if c.isalnum() or c in "-_"
        else "_"
        for c in client_name.strip()
    )

    timestamp = int(time.time())

    md_path = OUTPUT_DIR / f"proposal_{safe_name}_{timestamp}.md"
    txt_path = OUTPUT_DIR / f"proposal_{safe_name}_{timestamp}.txt"

    md_path.write_text(proposal, encoding="utf-8")
    txt_path.write_text(proposal, encoding="utf-8")

    print("Saved Markdown:", md_path)
    print("Saved TXT:", txt_path)

    return str(md_path), str(txt_path)


# --------------------------------------------------
# Main generation workflow
# --------------------------------------------------

def generate_proposal(
    company_name,
    company_description,
    products_services,
    client_name,
    client_requirements,
    budget,
    tone,
):
    """
    Three-stage LLM workflow.

    LLM #1 -> Client Analysis
    LLM #2 -> Solution Design
    LLM #3 -> Final Proposal Streaming
    """

    try:

        # ------------------------------------------
        # Validate input
        # ------------------------------------------

        service.validate_inputs(
            company_name,
            company_description,
            products_services,
            client_name,
            client_requirements,
            budget,
            tone,
        )

        # ------------------------------------------
        # LLM #1
        # Client Analysis
        # ------------------------------------------

        analysis = service.analyze_client(
            company_name,
            company_description,
            products_services,
            client_name,
            client_requirements,
            budget,
            tone,
        )

        analysis_display = (
            "### Client Analysis\n\n"
            f"**Client Needs**\n"
            + "\n".join(
                f"- {item}"
                for item in analysis["client_needs"]
            )
            + "\n\n**Pain Points**\n"
            + "\n".join(
                f"- {item}"
                for item in analysis["pain_points"]
            )
            + "\n\n**Recommended Services**\n"
            + "\n".join(
                f"- {item}"
                for item in analysis["recommended_services"]
            )
            + "\n\n**Key Benefits**\n"
            + "\n".join(
                f"- {item}"
                for item in analysis["key_benefits"]
            )
            + "\n\n**Target Outcomes**\n"
            + "\n".join(
                f"- {item}"
                for item in analysis["target_outcomes"]
            )
        )

        # ------------------------------------------
        # LLM #2
        # Solution Design
        # ------------------------------------------

        solution = service.design_solution(
            company_name,
            company_description,
            products_services,
            client_name,
            client_requirements,
            budget,
            tone,
            analysis,
        )

        # ------------------------------------------
        # LLM #3
        # Proposal Generation
        # ------------------------------------------

        proposal_prompt = service.build_proposal_prompt(
            company_name,
            company_description,
            products_services,
            client_name,
            client_requirements,
            budget,
            tone,
            analysis,
            solution,
        )

        # Start streaming
        proposal = ""

        for chunk in service.stream_proposal(
            proposal_prompt
        ):
            proposal += chunk

            # Yield progressively
            yield (
                analysis_display,
                solution,
                proposal,
                None,
                None,
                "Generating proposal..."
            )

        # ------------------------------------------
        # Save files
        # ------------------------------------------

        md_path, txt_path = save_proposal_files(
            proposal,
            client_name,
        )

        yield (
            analysis_display,
            solution,
            proposal,
            str(md_path),
            str(txt_path),
            "Proposal generated successfully."
        )

    except ValueError as exc:

        yield (
            "",
            "",
            f"### Error\n\n{exc}",
            None,
            None,
            f"Error: {exc}"
        )

    except Exception as exc:

        print("Application error:", repr(exc))

        yield (
            "",
            "",
            "### Error\n\n"
            "Something went wrong while generating the proposal.\n\n"
            "Please check your API key, internet connection, "
            "and try again.",
            None,
            None,
            "Generation failed."
        )


# --------------------------------------------------
# Clear form
# --------------------------------------------------

def clear_form():
    return (
        "",
        "",
        "",
        "",
        "",
        "",
        "Professional",
        "",
        "",
        "",
        None,
        None,
        "",
    )


# --------------------------------------------------
# Gradio UI
# --------------------------------------------------

with gr.Blocks(
    title="AI Sales Proposal Generator"
) as demo:

    gr.Markdown(
        """
# 💼 AI Sales Proposal Generator

Create personalized B2B sales proposals using a
**three-stage AI workflow**.

**Client Analysis → Solution Design → Proposal Writer**
"""
    )

    with gr.Row():

        # ------------------------------------------
        # Company information
        # ------------------------------------------

        with gr.Column():

            gr.Markdown("## Company Information")

            company_name = gr.Textbox(
                label="Company Name",
                placeholder="TechSolutions",
            )

            company_description = gr.Textbox(
                label="Company Description",
                placeholder=(
                    "Describe your company and its expertise."
                ),
                lines=4,
            )

            products_services = gr.Textbox(
                label="Products / Services",
                placeholder=(
                    "Custom AI Development, "
                    "Chatbots, Data Analytics..."
                ),
                lines=4,
            )

        # ------------------------------------------
        # Client information
        # ------------------------------------------

        with gr.Column():

            gr.Markdown("## Client Information")

            client_name = gr.Textbox(
                label="Client Name",
                placeholder="ABC Healthcare",
            )

            client_requirements = gr.Textbox(
                label="Client Requirements",
                placeholder=(
                    "Build an AI-powered "
                    "customer support system."
                ),
                lines=5,
            )

            budget = gr.Textbox(
                label="Budget",
                placeholder="$20,000",
            )

            tone = gr.Dropdown(
                label="Preferred Tone",
                choices=[
                    "Professional",
                    "Formal",
                    "Friendly",
                    "Persuasive",
                    "Technical",
                ],
                value="Professional",
            )

    # ----------------------------------------------
    # Generate button
    # ----------------------------------------------

    with gr.Row():

        generate_btn = gr.Button(
            "🚀 Generate Proposal",
            variant="primary",
        )

        clear_btn = gr.Button(
            "Clear",
        )

    status = gr.Markdown(
        "Ready to generate a proposal."
    )

    # ----------------------------------------------
    # Client Analysis
    # ----------------------------------------------

    gr.Markdown("---")
    gr.Markdown("## 🔎 Client Analysis")

    analysis_output = gr.Markdown(
        "Client analysis will appear here."
    )

    # ----------------------------------------------
    # Solution
    # ----------------------------------------------

    gr.Markdown("---")
    gr.Markdown("## 🛠 Proposed Solution")

    solution_output = gr.Markdown(
        "The proposed solution will appear here."
    )

    # ----------------------------------------------
    # Final Proposal
    # ----------------------------------------------

    gr.Markdown("---")
    gr.Markdown("## 📄 Generated Proposal")

    proposal_output = gr.Markdown(
        "Your proposal will appear here."
    )

    # ----------------------------------------------
    # Downloads
    # ----------------------------------------------

    gr.Markdown("### Download")

    with gr.Row():

        markdown_download = gr.DownloadButton(
            label="⬇ Download Markdown",
            value=None,
        )

        txt_download = gr.DownloadButton(
            label="⬇ Download TXT",
            value=None,
        )

    # ----------------------------------------------
    # Button events
    # ----------------------------------------------

    inputs = [
        company_name,
        company_description,
        products_services,
        client_name,
        client_requirements,
        budget,
        tone,
    ]

    outputs = [
        analysis_output,
        solution_output,
        proposal_output,
        markdown_download,
        txt_download,
        status,
    ]

    generate_btn.click(
        fn=generate_proposal,
        inputs=inputs,
        outputs=outputs,
    )

    clear_btn.click(
        fn=clear_form,
        inputs=[],
        outputs=[
            company_name,
            company_description,
            products_services,
            client_name,
            client_requirements,
            budget,
            tone,
            analysis_output,
            solution_output,
            proposal_output,
            markdown_download,
            txt_download,
            status,
        ],
    )


# --------------------------------------------------
# Launch
# --------------------------------------------------

if __name__ == "__main__":
    demo.launch()