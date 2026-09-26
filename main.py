import sys
from datetime import datetime
import requests
from prompts import SYSTEM_PROMPT
from helper import ask_llm, reset_chat, show_chat_history, show_help, return_available_models, \
    save_chat


def main() -> None:
    conversation = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    print("======================================== DevMentor AI Assistant ========================================")
    print(show_help())

    # Check Ollama and get available models
    try:
        models = return_available_models()

        print("\nOllama is running.")
        print("Available models:")

        for i, model in enumerate(models, start=1):
            print(f"{i}. {model}")

        # Select model
        while True:
            try:
                choice = int(input("\nSelect model number: "))

                if 1 <= choice <= len(models):
                    model = models[choice - 1]
                    print(f"Using model: {model}\n")
                    break

                print("Invalid model number. Please try again.")

            except ValueError:
                print("Please enter a number.")

    except requests.exceptions.RequestException:
        print(
            "\nUnable to connect to Ollama. Make sure Ollama is running and try again."
        )
        return

    while True:
        try:
            prompt = input("You: ").strip()

        except (EOFError, KeyboardInterrupt):
            print("\nbye.")
            return

        if not prompt:
            continue

        if prompt.startswith("/"):
            if prompt == "/reset":
                conversation = reset_chat()
                print("Conversation reset\n")

            elif prompt == "/exit":
                print("Bye.")
                return

            elif prompt == "/history":
                print(show_chat_history(conversation) + "\n")

            elif prompt == "/help":
                print(show_help())

            elif prompt == "/save":
                save_chat(SYSTEM_PROMPT, model, conversation)
            else:
                print("Unknown command\n")

            continue

        # Add the user's message to the conversation.
        conversation.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        # Send the conversation and selected model to the LLM.
        try:
            assistant_response = ask_llm(conversation, model)

        except requests.exceptions.RequestException:
            conversation.pop()
            print(
                "DevMentor: I couldn't connect to the AI model. Please try again."
            )
            continue

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


if __name__ == "__main__":
    sys.exit(main())
