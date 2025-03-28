# huggingface_api.py

from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()
HF_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

client = InferenceClient(
    provider="hyperbolic",
    api_key=HF_TOKEN,
)


def query(message: str, style: str):
    prompt = f"Finish this rap in {style} style: {message}"
    try:
        completion = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-R1",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
        )
        return {"response": completion.choices[0].message.content}
    except Exception as e:
        return {"error": str(e)}
