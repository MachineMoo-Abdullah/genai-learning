def build_prompt(

    document,
    question

):

    if not document:

        return question

    prompt = f"""
You are answering ONLY from the uploaded document.

If the answer does not exist in the document,
say:

"I could not find that in the uploaded document."

Document:

{document}

Question:

{question}
"""

    return prompt