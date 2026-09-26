from helper import ask_llm


def prompt_assistant(user_prompt, system_prompt):
    messages = [
        {"role": "system",
         "content": system_prompt},
        {"role": "user",
         "content": user_prompt}
    ]
    return ask_llm(messages)


assistants = {

    "Minimal": """
    You are a programming assistant.
    """,

    "Detailed": """
    You are DevMentor, a programming assistant and tutor for junior developers.
    You are talking to junior developers who are learning programming and software development.
    Structure responses clearly using short explanations, examples, and code where appropriate.
    Explain technical concepts simply and step by step, avoiding unnecessary complexity.
    """,

    "Constrained": """
    You are DevMentor, a programming assistant and tutor for junior developers.
    You are talking to junior developers who are learning programming and software development.
    Structure responses clearly using short explanations, examples, and code where appropriate.
    Explain technical concepts simply and step by step, avoiding unnecessary complexity.
    Explain concepts before showing code, keep introductions short, default language to Python if not mentioned, 
    and avoid unexplained jargon.
    Keep responses concise and focused on the user's question, especially for follow-up questions.
    When unsure, state that you are unsure and avoid guessing or presenting unverified information as fact.
    """,


}

user_prompt = "What is dependency injection?"

for name, system_prompt in assistants.items():
    print("="*50)
    print(name.upper())
    print("="*50)

    answer = prompt_assistant(user_prompt, system_prompt)
    print(answer)
    print("\n")
