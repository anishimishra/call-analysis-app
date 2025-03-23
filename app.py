import streamlit as st
import yaml
from utils import profanity, compliance, metrics
from utils.visualization import compute_silence_overtalk, plot_silence, plot_overtalk

st.title("Debt Collection Call Analysis")

uploaded_file = st.file_uploader("Upload Conversation YAML", type="yaml")
approach = st.selectbox("Select Approach", ["Pattern Matching", "LLM/ML"])
analysis = st.selectbox("Select Analysis", ["Profanity Detection", "Privacy & Compliance"])

if uploaded_file:
    conversation = yaml.safe_load(uploaded_file)

    if analysis == "Profanity Detection":
        profane_words = open('profanity_list.txt').read().splitlines()
        result = profanity.detect_profanity(conversation, profane_words)
        st.write("Profanity Result:", result)

    if analysis == "Privacy & Compliance":
        violation = compliance.detect_compliance_violation(conversation)
        st.write("Compliance Violation Detected:", violation)

    # Metrics Calculation
    overtalk = metrics.calculate_overtalk(conversation)
    silence = metrics.calculate_silence(conversation)
    st.write(f"Overtalk Percentage: {overtalk:.2f}%")
    st.write(f"Silence Percentage: {silence:.2f}%")

    # Compute silence and overtalk
    metrics_df = compute_silence_overtalk(conversation)

    # Display Visualizations
    st.subheader("Silence Duration Visualization")
    plot_silence(metrics_df)

    st.subheader("Overtalk Duration Visualization")
    plot_overtalk(metrics_df)