import requests
from config import OLLAMA_URL, MODEL


def check_ollama():
    """
    Check whether Ollama is available.
    """
    try:
        response = requests.get(
            f"{OLLAMA_URL}/api/tags",
            timeout=10
        )
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException:
        return False


def ask_llm(prompt, model=MODEL):
    """
    Send a prompt to the local LLM.
    """

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json=payload,
        timeout=120
    )

    response.raise_for_status()

    return response.json()["response"]
