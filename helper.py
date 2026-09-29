import pathlib
import json
from datetime import datetime
import requests
from config import OLLAMA_URL, MODEL


def return_available_models() -> list[str]:
    """
    Return the Ollama models available locally.

    Returns
    -------
    list[str]
        A list of available Ollama model names.
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
#
#     Returns
#     -------
#     bool
#         True if Ollama is available, otherwise False.
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
    Send a conversation to the selected local Ollama model.

    Parameters
    ----------
    messages : list[dict[str, str]]
        A list containing the conversation history.
    model : str
        The name of the selected Ollama model.

    Returns
    -------
    str
        The assistant's generated response.
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
    """
    Start a new conversation using the selected system prompt.

    Parameters
    ----------
    system_prompt : str
        The system prompt that defines the assistant's behaviour.

    Returns
    -------
    list[dict]
        A new conversation containing the system prompt.
    """
    messages = [{"role": "system", "content": system_prompt}]
    return messages


def show_chat_history(messages: list[dict]) -> str:
    """
    Display the conversation history.

    The system prompt is excluded from the returned history.

    Parameters
    ----------
    messages : list[dict]
        A list containing the conversation history.

    Returns
    -------
    str
        The formatted conversation history.
    """
    lines = []

    for message in messages:
        if message["role"] != "system":
            lines.append(f"[{message['role']}] {message['content']}")

    return "\n".join(lines)


def show_help() -> str:
    """
    Return the list of available DevMentor commands.

    Returns
    -------
    str
        A formatted list of available commands.
    """
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
    """
    Save the current conversation to a JSON file.

    Parameters
    ----------
    system_prompt : str
        The system prompt used for the conversation.
    model : str
        The Ollama model used for the conversation.
    messages : list[dict]
        The conversation history to save.
    """
    datetime_now = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

    # Timestamp added to allow multiple chat saves from the same day.
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
    """
    Load a saved conversation from a JSON file.

    Parameters
    ----------
    path : str
        The path to the saved conversation file.

    Returns
    -------
    list[dict]
        The conversation history loaded from the file.
    """
    data = json.loads(pathlib.Path(path).read_text())
    return data["messages"]
