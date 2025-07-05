import streamlit as st
import csv
import os
from dotenv import load_dotenv

load_dotenv()

from agent_wrapper import analyze_issue

st.set_page_config(page_title="Application Feedback Form", layout="centered")
st.title("📝 Application Feedback Form")

username = st.text_input("Username")
email = st.text_input("Email")
issue = st.text_area("Issue Faced")
suggestions = st.text_area("Suggestions (optional)")

if st.button("Submit Feedback"):
    if not username or not email or not issue:
        st.error("✔️ Please fill Username, Email, and Issue fields.")
    else:
        causes = analyze_issue(issue)
        
        # Format causes for multiline CSV cell (replace ". " with ".\n" for line breaks)
        causes_formatted = causes.replace(". ", ".\n").strip()

        file_exists = os.path.isfile("feedback_data.csv")
        with open("feedback_data.csv", "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Username", "Email", "Issue", "Suggestions", "Possible Causes"])
            writer.writerow([username, email, issue, suggestions, causes_formatted])

        st.success("🎉 Feedback submitted successfully! Thank you for your time, Our team will review it.")
        st.write("🛠️ Possible causes identified:")
        st.text_area("Possible Causes", value=causes, height=200, max_chars=None, key="causes_display")
