# app.py

import streamlit as st
from huggingface_api import query

st.set_page_config(page_title="Rap Battle Bot", page_icon="🎤")
st.title("🎤 Rap Battle Bot")
st.subheader("Drop your line, and the bot will clap back in rhyme!")

user_input = st.text_input(
    "Your line:", placeholder="E.g., 'I'm the king of code, don't test my flow.'"
)
style = st.selectbox(
    "Rap Style", ["Freestyle", "Old School", "Trap", "Shakespearean 😅"]
)

if st.button("Drop the Beat"):
    if user_input:
        result = query(
            """
You are a rap battle MC. Only respond with raw rap lyrics, without any explanations, analysis, or labels like "Verse 1" or "Chorus". Do not repeat the user input. Continue this line in a consistent rhyme and flow, using the specified style. User line: "{user_input}". Now generate 4 more rap lines:
""",
            style,
        )
        if "error" in result:
            st.error(f"❌ Error: {result['error']}")
        else:
            st.write("🎶 **Bot's bars:**")
            # Extract content after </think>
            raw_output = result["response"].strip()
            if "</think>" in raw_output:
                bars = raw_output.split("</think>")[-1].strip()
            else:
                bars = raw_output  # fallback if </think> not present

            st.success(bars)

    else:
        st.warning("Please enter a line to battle with!")
