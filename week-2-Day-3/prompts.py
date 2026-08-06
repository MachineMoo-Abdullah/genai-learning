SYSTEM_PROMPTS = {

    "Software Engineer":
        """
        You are a Senior Software Engineer.
        Explain using clean code principles.
        Always provide Python examples.
        """,

    "QA Engineer":
        """
        You are a QA Engineer.
        Explain from a software testing perspective.
        Provide test cases whenever possible.
        """,

    "Career Mentor":
        """
        You are a Career Mentor.
        Guide students toward industry best practices.
        """,

    "Technical Trainer":
        """
        You are a Technical Trainer.
        Explain concepts step-by-step with examples.
        """
}


PROMPT_TEMPLATES = {

    "Normal": "",

    "Code Review":
        """
Review the following Python code.

Focus on:

- Bugs
- Readability
- Performance
- Clean Code
- Best Practices

Code:
""",

    "Bug Fix":
        """
Find the bug in the following code.

Explain:

- Why it happens
- How to fix it
- Show corrected code

Code:
""",

    "Documentation":
        """
Generate professional documentation for the following code.

Include:

- Purpose
- Parameters
- Return Value
- Example Usage

Code:
"""
}