import sys
from prompts import SYSTEM_PROMPT
from helper import check_ollama, ask_llm, reset_chat, show_chat_history


BANNER = """
Commands:
  /reset        start a fresh conversation
  /history      show full history
  /exit         exit chat
"""


def main() -> None:
    conversation = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]
    print("======================================== DevMentor AI Assistant ========================================")
    print(BANNER)

    # run app
    if not check_ollama():
        print("\nOllama is not running.")
    else:

        print("\nOllama is running.")

        while True:
            prompt = input("You: ")

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
                else:
                    print("Unknown command\n")
                continue

            else:
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


if __name__ == "__main__":
    sys.exit(main())
