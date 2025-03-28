# huggingface_api.py

from huggingface_hub import InferenceClient
import streamlit as st

def get_client():
    HF_TOKEN = st.secrets["HUGGINGFACE_API_TOKEN"]
    return InferenceClient(provider="hyperbolic", api_key=HF_TOKEN)

def query(message: str, style: str):
    client = get_client()
    prompt = (
        "You are a rap battle MC. Only respond with raw rap lyrics, without any explanations, analysis, or labels like 'Verse 1' or 'Chorus'. "
        "Do not repeat the user input. Continue this line in a consistent rhyme and flow, using the specified style.\n\n"
        f"User line: \"{message}\"\n"
        f"Style: {style}\n\n"
        "Now generate 4 more rap lines:"
    )

    try:
        completion = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-R1",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
        )
        return {"response": completion.choices[0].message.content}
    except Exception as e:
        return {"error": str(e)}
