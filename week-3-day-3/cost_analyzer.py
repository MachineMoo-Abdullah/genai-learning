"""
Streamlit Tokenizer Cost & Context Analyzer

Run:
    streamlit run cost_analyzer.py

Notes:
- Context windows and API prices can change.
- Defaults below are editable in the UI.
- Token counts are generated locally by Hugging Face tokenizers.
"""

import streamlit as st
from transformers import AutoTokenizer

MODEL_IDS = {
    "Phi-4": "microsoft/phi-4",
    "DeepSeek-V3": "deepseek-ai/DeepSeek-V3",
    "Qwen2.5-Coder": "Qwen/Qwen2.5-Coder-0.5B-Instruct",
}

# Educational defaults, intentionally editable.
# Do not treat these as guaranteed API limits/prices for a provider.
DEFAULT_CONTEXT = {
    "Llama 3.1": 131072,
    "Phi-4": 16384,
    "DeepSeek-V3": 131072,
    "Qwen2.5-Coder": 32768,
}


@st.cache_resource
def load_tokenizer(label):
    model_id = MODEL_IDS[label]
    return AutoTokenizer.from_pretrained(
        model_id,
        trust_remote_code=(label == "DeepSeek-V3"),
    )


st.set_page_config(page_title="Tokenizer Analyzer", layout="centered")
st.title("Tokenizer Analyzer")
st.caption("Compare characters, words, tokens, context usage, and estimated input cost.")

selected = st.selectbox("Tokenizer", list(MODEL_IDS.keys()))

text = st.text_area(
    "Enter text",
    value="Generative AI is changing software development.",
    height=180,
)

col1, col2 = st.columns(2)
with col1:
    context_window = st.number_input(
        "Context window (tokens)",
        min_value=1,
        value=DEFAULT_CONTEXT[selected],
        step=1024,
        help="Editable because context limits depend on the exact model/deployment.",
    )
with col2:
    price_per_million = st.number_input(
        "Input price ($ per 1M tokens)",
        min_value=0.0,
        value=0.0,
        step=0.01,
        format="%.4f",
        help="Enter the current provider price. Zero means cost calculation is disabled.",
    )

try:
    tokenizer = load_tokenizer(selected)
    ids = tokenizer.encode(text, add_special_tokens=False)

    chars = len(text)
    words = len(text.split())
    tokens = len(ids)
    context_pct = (tokens / context_window * 100) if context_window else 0.0
    estimated_cost = tokens / 1_000_000 * price_per_million

    a, b, c = st.columns(3)
    a.metric("Characters", chars)
    b.metric("Words", words)
    c.metric("Tokens", tokens)

    st.metric("Estimated Context Usage", f"{context_pct:.4f}%")
    st.metric("Estimated Input Cost", f"${estimated_cost:.8f}")

    with st.expander("Show token pieces and IDs"):
        pieces = tokenizer.convert_ids_to_tokens(ids)
        rows = [
            {"#": i, "Token": repr(piece), "Token ID": token_id}
            for i, (piece, token_id) in enumerate(zip(pieces, ids), start=1)
        ]
        st.dataframe(rows, use_container_width=True)

    st.info(
        "Token counts are exact for the selected tokenizer and text. "
        "Context limits and API prices should be verified for the exact model/provider."
    )

except Exception as e:
    st.error(str(e))
    if selected == "Llama 3.1":
        st.warning(
            "If Llama access is gated, accept the model license on Hugging Face "
            "and authenticate locally using `huggingface-cli login`."
        )
