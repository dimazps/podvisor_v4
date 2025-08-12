import streamlit as st
from analyzer.core import analyze_logs
from analyzer.agent import query_agent

st.set_page_config(page_title="Log Analyzer with GenAI", layout="wide")
st.title("🔍 Log Analyzer with GenAI Agents")

uploaded_file = st.file_uploader("Upload a log file", type=["log", "txt"])
user_prompt = st.text_area("Enter your question or prompt", height=100)

if st.button("Analyze"):
    if uploaded_file and user_prompt:
        log_data = uploaded_file.read().decode("utf-8")
        parsed_output = analyze_logs(log_data)
        agent_response = query_agent(user_prompt, parsed_output)

        st.subheader("🧠 GenAI Agent Response")
        st.markdown(agent_response)

        st.subheader("📄 Parsed Log Summary")
        st.json(parsed_output)

        st.subheader("📊 Duration Analytics")
        durations = parsed_output.get("durations", [])
        if durations:
            duration_labels = [f"{d['start']} → {d['end']}" for d in durations]
            duration_values = [int(d["duration"].replace("s", "")) for d in durations]
            st.bar_chart({label: value for label, value in zip(duration_labels, duration_values)})
        else:
            st.info("No durations found.")
    else:
        st.warning("Please upload a log file and enter a prompt.")