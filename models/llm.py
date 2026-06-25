import requests
from utils.config import *

def ask_request(prompt):
    return call_model(DEFAULT_CONTROLLER_MODEL,prompt)

def ask_responce(prompt):
    return call_model(DEFAULT_CHAT_MODEL, prompt)

def ask_coder(prompt):
    return call_model(DEFAULT_CODER_MODEL, prompt)

def call_model(model, prompt):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            }
        )
        return response.json()["response"]
    
    except Exception as e:
        return f"ERROR: {e}"
    
