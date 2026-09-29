import sys
import json
import requests
from prompts import SYSTEM_PROMPT, MODES
from helper import ask_llm, reset_chat, show_chat_history, show_help, return_available_models, \
    save_chat, load_chat


def main() -> None:
    """
    Run the DevMentor command-line application.

    Checks for available Ollama models, allows the user to
    select a model and interaction mode, and manages the
    conversation until the user exits.
    """
    # conversation = [
    #     {
    #         "role": "system",
    #         "content": SYSTEM_PROMPT
    #     }
    # ]

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

    print("\nAvailable modes:")

    mode_names = list(MODES.keys())

    for i, mode_name in enumerate(mode_names, start=1):
        print(f"{i}. {mode_name}")

    while True:
        try:
            choice = int(input("\nSelect mode number: "))

            if 1 <= choice <= len(mode_names):
                mode_name = mode_names[choice - 1]
                system_prompt = MODES[mode_name]

                print(f"Using mode: {mode_name}\n")
                break

            print("Invalid mode number. Please try again.")

        except ValueError:
            print("Please enter a number.")

    conversation = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

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
                conversation = reset_chat(system_prompt)
                print("Conversation reset\n")

            elif prompt == "/exit":
                print("Bye.")
                return

            elif prompt == "/history":
                print(show_chat_history(conversation) + "\n")

            elif prompt == "/help":
                print(show_help())

            elif prompt == "/save":
                save_chat(system_prompt, model, conversation)

            elif prompt == "/load":
                path = input("Enter the chat path: ").strip()

                try:
                    conversation = load_chat(path)
                    print("Conversation loaded\n")
                except (FileNotFoundError, json.JSONDecodeError, KeyError):
                    print(
                        "Could not load the conversation. Check the file path and format.\n")
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
