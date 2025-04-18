import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="AI Sentiment Dashboard")

# Load the sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

st.title("🧠 AI Sentiment Analyzer")

# Input box to enter text
user_input = st.text_area("Enter text to analyze:", "GitHub Codespaces is awesome!")

if st.button("Analyze"):
    with st.spinner("Running model..."):
        result = classifier(user_input)
        label = result[0]['label']
        score = result[0]['score']
        st.success(f"Prediction: **{label}** ({score:.2f} confidence)")
