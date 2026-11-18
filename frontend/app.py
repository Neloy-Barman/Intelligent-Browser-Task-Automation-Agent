import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st

from crew import crew

st.set_page_config(page_title="Browser Automation Agent", layout="centered")

st.title("Browser Automation Agent")
st.write("Enter a browser automation task and run it.")

task = st.text_input("Task", placeholder="e.g. Visit https://example.com and report the page title.")

if st.button("Run"):
    if not task.strip():
        st.warning("Please enter a task.")
    else:
        with st.spinner("Running agent..."):
            try:
                result = crew.kickoff(inputs={"user_task": task.strip()})
                st.success("Done")
                st.subheader("Result")
                st.write(result)
            except Exception as e:
                st.error(f"Error: {e}")
