import requests
from config import OLLAMA_URL, MODEL
from prompts import SYSTEM_PROMPT

conversation = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]


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


def ask_llm(messages: list[dict]) -> str:
    payload = {
        "model": MODEL,
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


print("======================================== DevMentor AI Assistant ========================================")


# run app
if not check_ollama():
    print("\nOllama is not running.")
else:

    print("\nOllama is running.")

    print("Type 'exit' to stop.\n")

    while True:
        prompt = input("You: ")

        if prompt.lower() == "exit":
            break

        # Add the user's message to the conversation.
        conversation.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        assistant_response = ask_llm(conversation)
        # Add the assistant's response to the conversation.
        conversation.append(
            {
                "role": "assistant",
                "content": assistant_response
            }
        )

        print("\nDevMentor:")
        print(assistant_response)
        print()
