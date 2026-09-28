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

### 4. Create and activate virtual environment

```bash
python3 -m venv venv
. venv/bin/activate
```

### 5. Install Python Dependencies

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

DevMentor uses system prompts to define the assistant's role, behaviour, and response style. The system prompt is sent to the Ollama model as part of the conversation and guides how the model should respond to the user.

The project includes four interaction modes, each using a different system prompt:

| Mode                 | Purpose                                                                                                                      |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **Beginner Tutor**   | Explains programming concepts simply and step by step for beginners.                                                         |
| **Senior Engineer**  | Provides technically precise guidance and considers factors such as maintainability, performance, security, and scalability. |
| **Code Reviewer**    | Reviews code for correctness, readability, maintainability, performance, security, and potential bugs.                       |
| **Socratic Teacher** | Guides the learner using questions and hints instead of immediately providing the complete solution.                         |

All modes include a common baseline to keep responses concise, focused on the user's question, and avoid guessing when the model is unsure.

The selected mode determines which system prompt is used for the conversation. The prompt remains active throughout the session unless the application is restarted with a different mode.


## How Conversation Memory Works

### What is Conversation Memory?

Conversation memory is the ability of an AI assistant to use previous messages from the current conversation when responding to a new message. This allows the assistant to maintain context across multiple turns instead of treating each message as a completely separate request.

For example, if a user asks:

```text
You: What is a Python list?

DevMentor: A Python list is a collection that can store multiple values...

You: How do I add an item to it?
```

The second question depends on the previous conversation. By providing the earlier messages as context, the model can understand that "it" refers to a Python list and answer with that context in mind.

### How DevMentor Implements Conversation Memory

Most LLM APIs are stateless, meaning they do not automatically remember previous requests after generating a response (they do not preserve an internal memory). Each request is treated independently unless the application sends previous messages back as context.

DevMentor therefore manages conversation memory in the Python application by storing the conversation history in a list and sending the full history with each request. The conversation includes the system prompt, user messages, and assistant responses.

When the user sends a new message, the application adds it to the conversation history and sends the full conversation to the Ollama API. This gives the local model the previous messages as context when generating its response.

The flow is:

```text
User message
     ↓
Add message to conversation history
     ↓
Send full conversation to Ollama
     ↓
Local LLM generates response
     ↓
Add response to conversation history
     ↓
Display response to user
```

This means DevMentor's memory is **application-managed** so the model does not update or retrain itself from the conversation.


## Prompt Engineering Experiment
| | Style | Prompt |
| --- | --- | --- |
| A | Minimal: Simple, vague | You are a programming assistant. |
| B | Detailed: Role, audience, format, explanation style | You are DevMentor, a programming assistant and tutor for junior developers. You are talking to junior developers who are learning programming and software development. Structure responses clearly using short explanations, examples, and code where appropriate. Explain technical concepts simply and step by step, avoiding unnecessary complexity. |
| C | Constrained: Explain before code, keep intros short, default to Python, avoid unexplained jargon | You are DevMentor, a programming assistant and tutor for junior developers. You are talking to junior developers who are learning programming and software development. Structure responses clearly using short explanations, examples, and code where appropriate. Explain technical concepts simply and step by step, avoiding unnecessary complexity. Explain concepts before showing code, keep introductions short, default language to Python if not mentioned, and avoid unexplained jargon. Keep responses concise and focused on the user's question, especially for follow-up questions. When unsure, state that you are unsure and avoid guessing or presenting unverified information as fact. |

**Using the prompts:**
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

### 1. Designing Effective System Prompts

I realized every time I asked a question, DevMentor gave the initial elaborate explanations with examples and code examples, but when I asked follow-up questions, it still did the same, even if it was a simple response question.

So now all modes have a baseline prompt to keep responses concise and focused on the user's question, especially for follow-up questions. It is also to prevent unnecessary repetition of previous explanations unless the user explicitly asks for more detail.


## Lessons Learned

### 1. Context Window
I learnt about context windows and the Lost in the Middle phenomenon, and why it is important to manage context so the model's performance is not impacted and the available tokens are not exhausted.


## Challenge questions

1. Why does the app send previous messages to the LLM?

Most LLM API requests are stateless. The model does not automatically remember previous requests, so DevMentor sends the previous messages as part of the next request to provide the model with conversation context.

2. What is the difference between `system`, `user`, and `assistant` messages?  

system: Defines the assistant's role, behaviour, and instructions on how to respond to the user. In DevMentor, this contains the selected mode's system prompt.

user: Contains the user's messages or questions.

assistant: Contains the responses generated by the LLM.

3. If you close Python and restart, why does the assistant “forget”?  

DevMentor's memory is application-managed, which means it is stored in the Python application's memory while the program is running. When Python closes, that in-memory conversation list is lost. When the application starts again, it creates a new conversation unless a previously saved conversation is loaded.

4. Is memory stored inside the LLM or inside your application? Explain.

The Python application maintains the conversation list and sends it to the LLM as context. The LLM itself is not being retrained or permanently updated by the conversation.

5. What happens when the conversation becomes extremely long? Research the term **context window**. 

The conversation uses part of the model's context window, which is the maximum amount of information the model can process in a request, measured in tokens. As more messages are added, the conversation consumes more tokens. Eventually, the context limit can be reached, meaning the application cannot continue sending the entire conversation.

Long contexts can also affect how well the model understands the history it receives. This is related to the Lost in the Middle effect, where an LLM may attend to information at the beginning and end of a long context more effectively than information located in the middle. As a conversation becomes very long, important details from earlier messages may therefore receive less attention, even though they are still included in the context window. This is one reason why very long conversations can become less reliable over time.

**Two strategies for managing long chats are:**

* **Limit Active Conversation History:** Instead of sending the entire conversation with every request, the application can keep only the most recent messages within a defined limit. This reduces token usage and keeps the model's active context focused on recent messages. However, older messages may contain information that is still relevant, so removing them from the active context can cause the model to lose important information and potentially generate incorrect or hallucinated responses.

* **Externalize Conversation Context:** As users of AI assistants, before a chat becomes too long, create a summary or handoff file containing key decisions, architecture, finalized code, and outstanding tasks. Start a new chat and provide the handoff file as context, allowing the project to continue without relying on one long conversation history.

6. Why is `You are helpful.` a weak system prompt? How would you improve it?

`You are helpful.` is too vague as a system prompt. It does not tell the model who it is, who it is helping, how it should respond, or what behaviour is expected. I would improve it by clearly stating its role, who its audience is, how it should explain or present outputs, and the behaviour expected from it.

7. After the LLM replies, what should happen to `messages` before the next user turn, and why?

The assistant's response should be added to messages before the next user message:
```python
messages.append({
    "role": "assistant",
    "content": assistant_response
})
```
to become:

```python
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": question},
    {"role": "assistant", "content": assistant_response}
]
```

This is important because the assistant's response becomes part of the conversation history. When the next user message is sent, the LLM receives both the previous user question and its previous response, allowing it to maintain the conversation context.
