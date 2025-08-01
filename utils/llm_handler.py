import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
# TOGETHER_MODEL = os.getenv("TOGETHER_MODEL", "openchat/openchat-3.5-1210")
TOGETHER_MODEL = os.getenv("TOGETHER_MODEL", "mistralai/Mistral-7B-Instruct-v0.1")
if TOGETHER_API_KEY is None:
    raise EnvironmentError("TOGETHER_API_KEY is not set in your .env file")

print("🔑 Together API Key (starts with):", TOGETHER_API_KEY[:12])

def query_llm(prompt: str) -> str:
    url = "https://api.together.xyz/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    payload = {
        "model": TOGETHER_MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful education assistant."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 512,
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=payload)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("❌ API Error Response:", response.text)
        raise e

    return response.json()["choices"][0]["message"]["content"].strip()










