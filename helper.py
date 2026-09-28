import pathlib
import json
from datetime import datetime
import requests
from config import OLLAMA_URL, MODEL


def return_available_models() -> list[str]:
    """
    Return locally available Ollama models.
    """
    response = requests.get(
        f"{OLLAMA_URL}/api/tags",
        timeout=10
    )
    response.raise_for_status()

    data = response.json()

    return [model["name"] for model in data["models"]]


# def check_ollama() -> bool:
#     """
#     Check whether Ollama is available.
#     """
#     try:
#         response = requests.get(
#             f"{OLLAMA_URL}/api/tags",
#             timeout=10
#         )
#         response.raise_for_status()
#         return True
#     except requests.exceptions.RequestException:
#         return False


def ask_llm(messages: list[dict[str, str]], model: str = MODEL) -> str:
    """
    Send a conversation to the local Ollama model.

    Parameters
    ----------
    messages : list
        A list containing the conversation history.
    model : str
        The name of the model selected.

    Returns
    -------
    str
        The assistant's response.
    """

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


def reset_chat(system_prompt: str) -> list[dict]:
    messages = [{"role": "system", "content": system_prompt}]
    return messages


def show_chat_history(messages: list[dict]) -> str:
    lines = []
    for message in messages:
        if message["role"] != "system":
            lines.append(f"[{message['role']}] {message['content']}")
    return "\n".join(lines)


def show_help() -> str:

    return """
    Available commands:

        /help     Show available commands
        /reset    Start a fresh conversation
        /history  Show full chat history
        /save     Save chat to JSON
        /load     Load chat from JSON
        /exit     Exit chat
    """


def save_chat(system_prompt: str, model: str, messages: list[dict]) -> None:

    datetime_now = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    # timestamp added to allow multiple chat saves from the same day
    path = f"conversations/chat_{datetime_now}.json"

    file_path = pathlib.Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    file_path.write_text(
        json.dumps(
            {
                "system": system_prompt,
                "model": model,
                "messages": messages
            },
            indent=2
        )
    )
    print(f"Saved to: {file_path}\n")


def load_chat(path: str) -> list[dict]:
    data = json.loads(pathlib.Path(path).read_text())
    return data["messages"]
