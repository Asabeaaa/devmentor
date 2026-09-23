from parts.part1 import check_ollama, ask_llm


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

        answer = ask_llm(prompt)

        print("\nAssistant:")
        print(answer)
        print()
