import requests
from config import OLLAMA_URL, MODEL
from prompts import SYSTEM_PROMPT


def return_available_models() -> list[str]:
    response = requests.get(
        f"{OLLAMA_URL}/api/tags",
        timeout=10
    )
    response.raise_for_status()

    data = response.json()

    return [model["name"] for model in data["models"]]


def check_ollama() -> bool:
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


def ask_llm(messages: list[dict[str, str]], model: str = MODEL) -> str:
    payload = {
        "model": model,
        "messages": messages,
        "stream": False
    }

    # Send the request to Ollama.
    response = requests.post(
        f"{OLLAMA_URL}/api/chat",
        json=payload,
        timeout=120
    )

    # Raise an error if Ollama returns an unsuccessful response.
    response.raise_for_status()

    # Convert Ollama's JSON response into a Python dictionary.
    data = response.json()

    # Return only the generated text.
    return data["message"]["content"]


def reset_chat() -> list[dict]:
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    return messages


def show_chat_history(messages: list[dict]) -> str:
    lines = []
    for m in messages:
        lines.append(f"[{m['role']}] {m['content']}")
    return "\n".join(lines)


def show_help() -> str:

    return """
    Available commands:

        /help       Show this help message
        /reset      Start a fresh conversation
        /history    Show full chat history
        /exit       Exit chat
    """
