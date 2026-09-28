# DevMentor

## Description
DevMentor is a local AI programming assistant and tutor built with Python and Ollama run from the command line. It allows users to select an available local language model and choose a mode that controls how the assistant responds. 
It is designed to help developers learn programming concepts, solve problems, understand code, and improve their programming skills using locally hosted language models.


## Features
* **Local Language Model Support:** Run locally hosted language models through Ollama.
* **Language Model Selection:** View available Ollama models and select a model when the application starts.
* **Interaction Modes:** Choose how DevMentor responds using Beginner Tutor, Senior Engineer, Code Reviewer, or Socratic Teacher modes. Each mode uses a different system prompt that guides the model's behaviour and response style.
* **Conversation Memory:** Maintains the conversation history and sends it as context with each request.
* **Reset Conversation:** Start a fresh conversation while keeping the selected mode (system prompt).
* **View History:** Display the current conversation history.
* **Save Conversations:** Save the current conversation to a JSON file.
* **Load Conversations:** Load a previously saved conversation from a JSON file.
* **Command Interface:** Use commands such as `/help`, `/reset`, `/history`, `/save`, `/load`, and `/exit`.


## Architecture

```text
                         ┌─────────────────────┐
                         │        User         │
                         └──────────┬──────────┘
                                    │
                                    │ User prompt
                                    v
                         ┌─────────────────────┐
                         │ Python Application: │
                         │                     │
                         │ Conversation state  │
                         │ lives here          │
                         └──────────┬──────────┘
                                    │
                                    │ Full conversation history
                                    │ + selected model
                                    v
                         ┌─────────────────────┐
                         │     Ollama API:     │
                         │                     │
                         │ Sends requests to   │
                         │ the selected model  │
                         └──────────┬──────────┘
                                    │
                                    │ Prompt + conversation
                                    v
                         ┌─────────────────────┐
                         │      Local LLM:     │
                         │                     │
                         │ Model runs locally  │
                         │ through Ollama      │
                         └──────────┬──────────┘
                                    │
                                    │ Generated response
                                    v
                         ┌─────────────────────┐
                         │ Python Application: │
                         │                     │
                         │ Adds response to    │
                         │ conversation state  │
                         └──────────┬──────────┘
                                    │
                                    │ Response
                                    v
                         ┌─────────────────────┐
                         │        User         │
                         └─────────────────────┘
```

### Architecture Notes

* **Model location:** The selected LLM runs locally on the user's computer through Ollama.
* **Conversation state:** The Python application stores the conversation history in the conversation list.
* **Ollama API:** The API receives the conversation and selected model, sends the request to the local LLM, and returns the generated response.
* **Every request:** The application sends the full conversation history, including the system prompt, previous user messages, and previous assistant responses, along with the selected model.


## Installation

### Prerequisites

Before running DevMentor, make sure you have:

* Python 3.10 or later installed.
* Ollama installed on your computer.
* At least one Ollama model downloaded.

### 1. Install Ollama

Download and install Ollama from the official website based on your operating system.

After installation, make sure Ollama is running.

### 2. Install an Ollama Model

For example, to install Llama 3.2:

```bash
ollama pull llama3.2
```

You can check which models are installed with:

```bash
ollama list
```

### 3. Clone the Repository

```bash
git clone https://github.com/Asabeaaa/devmentor.git
cd devmentor
```

### 4. Install Python Dependencies

```bash
pip install -r requirements.txt
```


## Running the Application

From the project directory, run:

```bash
python3 main.py
```

When the application starts, DevMentor will:

1. Check for available local Ollama models.
2. Display the available models and prompt you to select one.
3. Display the available interaction modes and prompt you to select one.
4. Start the conversation using the selected model and mode.

### Available Commands

During the application run, you can use the `/help` command to view the available commands and actions.

| Command    | Description                                    |
| ---------- | ---------------------------------------------- |
| `/help`    | Show available commands                        |
| `/reset`   | Start a fresh conversation                     |
| `/history` | Display the current conversation history       |
| `/save`    | Save the current conversation to JSON          |
| `/load`    | Load a previously saved conversation from JSON |
| `/exit`    | Exit DevMentor                                 |

The model and interaction mode are selected when the application starts and cannot currently be changed during an active session.


## System Prompt
## How Conversation Memory Works

## Prompt Engineering Experiment
| | Style | Prompt |
| --- | --- | --- |
| A | Minimal: Simple, vague | You are a programming assistant. |
| B | Detailed: Role, audience, format, explanation style | You are DevMentor, a programming assistant and tutor for junior developers. You are talking to junior developers who are learning programming and software development. Structure responses clearly using short explanations, examples, and code where appropriate. Explain technical concepts simply and step by step, avoiding unnecessary complexity. |
| C | Constrained: Explain before code, keep intros short, default to Python, avoid unexplained jargon | You are DevMentor, a programming assistant and tutor for junior developers. You are talking to junior developers who are learning programming and software development. Structure responses clearly using short explanations, examples, and code where appropriate. Explain technical concepts simply and step by step, avoiding unnecessary complexity. Explain concepts before showing code, keep introductions short, default language to Python if not mentioned, and avoid unexplained jargon. Keep responses concise and focused on the user's question, especially for follow-up questions. When unsure, state that you are unsure and avoid guessing or presenting unverified information as fact. |

Using the prompts: 
- Explain REST APIs.
- Explain recursion.
- What is dependency injection?

1. Which prompt was most useful, and why?:

The Constrained prompt was the most useful overall. It consistently produced responses that were structured, focused, and easier for a junior developer to follow. It also followed specific instructions such as using simple explanations, examples, and defaulting to Python code.

2. What differences did you see?:

The Minimal prompt often produced surprisingly detailed responses and gave the model more freedom over the structure and programming language. The Detailed prompt produced more comprehensive explanations, but sometimes included more information or code than necessary. The Constrained prompt produced more focused responses, often using simpler examples and clearer structures.

3. Did more instructions always help?:

No. The results show that more instructions did not always produce a better response. The Detailed prompt generally produced more information, but that did not necessarily make the explanation more suitable for a junior developer. The Constrained prompt used fewer but more specific instructions to control the response's style and format.

4. Which rules changed behaviour the most?:

The rules that had the clearest effect were:

- Explain concepts simply and step by step
- Explain before showing code
- Keep responses concise
- Default to Python
- Use examples where appropriate
- Avoid unexplained jargon

5. What happened when a rule was vague?:

When instructions were vague, the model had more freedom to decide the length, structure, programming language, and level of technical detail. For example, the Minimal prompt produced lengthy responses despite being minimal, and it chose Java for the Dependency Injection example. This shows that vague instructions may still produce a technically relevant answer, but the output may not match the intended audience or teaching style.

## Memory Experiment
This is a memory experiment to test whether DevMentor can remember information from earlier messages and use it correctly in later messages and the impact of resetting the chat on the memory.

**Before resetting memory**
User: My favorite programming language is Python.:

Python is a popular and versatile language, widely used in various domains such as web development, data analysis, artificial intelligence, and more. What specifically about Python do you enjoy about it? Is it the simplicity of its syntax, the large number of libraries available, or something else?

User: Explain interfaces.:

In programming, an interface is a contract that defines a set of methods that a class or object must implement. It's like a blueprint or a specification for a class, outlining what methods it must have, but not how they're implemented.

Think of an interface as a promise: "I'll give you a class that does X, Y, and Z, no matter how I implement them." An interface provides a way for different classes to work together without worrying about the implementation details.

In Python, you can define an interface using a class with a `_interface` suffix and methods that are not implemented (i.e., they raise a `NotImplementedError` exception). For example:
```python
class Printable:
    def __init__(self, name):
        self.name = name

    def print(self):
        raise NotImplementedError("Must be implemented by subclass")

class Document(Printable):
    def print(self):
        print(f"Printing {self.name}")
```
In this example, the `Printable` interface defines a `print` method that must be implemented by any subclass. The `Document` class implements this method, while any other class would need to do the same to be considered `Printable`.

Does that make sense?

User: What is my favorite programming language?:

You mentioned earlier that your favorite programming language is Python.

**After resetting memory**
User: What is my favorite programming language?:

I'm happy to help you with your question, but I'm a bit unsure... This conversation just started, and we haven't discussed any programming languages yet. Could you please tell me, what programming languages have you tried, and which ones you're interested in learning more about?

**Does the LLM actually “remember” the conversation?**:

Yes. The LLM was able to use the information about my favorite programming language from an earlier message in the conversation to answer the follow-up question correctly.

This is done by the application maintaining the conversation as application state using the conversation variable. This variable stores the message history, including previous user and assistant messages. On each request, the application sends this message history as part of the context to the LLM. This allows the LLM to access earlier information, such as my favorite programming language being Python, and use it when answering later questions.



## Challenges Encountered

## Lessons Learned
