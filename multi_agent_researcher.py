import re
import streamlit as st
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_ollama import ChatOllama

# Cache search to avoid repeated API calls
@st.cache_data
def search_duckduckgo(query):
    return DuckDuckGoSearchRun().run(query)

# Clean text: remove extra spaces
def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip()

# Single model for everything
model = ChatOllama(model="qwen3:8b")

query = st.text_input("Enter your query:")

if query:
    query = clean_text(query)

    # Step 1: Search online (cached)
    with st.spinner("Searching online..."):
        search_results = search_duckduckgo(query)

    # Step 2: Single LLM call: refine + summarize
    st.subheader("Research Result:")
    result_placeholder = st.empty()
    streamed_text = ""

    with st.spinner("Refining & summarizing..."):
        for token in model.stream(
            f"""Refine the following user query for better clarity, then summarize the search results.

User query: {query}

Search results:
{search_results}

Respond ONLY with a clear, concise research summary (max 200 words).
"""
        ):
            if token.content:
                streamed_text += token.content
                result_placeholder.markdown(streamed_text)
