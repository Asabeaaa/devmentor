import sys
import requests
from prompts import SYSTEM_PROMPT
from helper import check_ollama, ask_llm, reset_chat, show_chat_history, show_help


def main() -> None:
    conversation = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]
    print("======================================== DevMentor AI Assistant ========================================")
    print(show_help())

    # run app
    if not check_ollama():
        print("\nUnable to connect to Ollama. Make sure Ollama is running and try again.")
    else:

        print("\nOllama is running.")

        while True:
            try:
                prompt = input("You: ").strip()

            except (EOFError, KeyboardInterrupt):
                print("\nbye.")
                return

            if not prompt:
                continue

            if prompt.startswith("/"):

                # reset
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

            # actual chat
            try:
                assistant_response = ask_llm(conversation)

            except requests.exceptions.RequestException:
                conversation.pop()
                print(
                    "DevMentor: I couldn't connect to the AI model. Please try again.")
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
