import streamlit as st
from agent import run_research

st.set_page_config(page_title="Research Agent", page_icon="🔍")
st.title("🔍 AI Research Agent")
st.caption("Powered by Groq (Llama 3) + Tavily — 100% free")

topic = st.text_input("Enter a research topic", placeholder="e.g. The impact of AI on healthcare in 2025")

if st.button("Research", type="primary") and topic:
    with st.spinner("Searching and analyzing... (this takes ~30 seconds)"):
        try:
            report = run_research(topic)
            st.markdown(report)
        except Exception as e:
            st.error(f"Something went wrong: {e}")