# DevMentor

## Description
This is a local programming assistant for junior developers called Dev Mentor run using the command line.

## Features
## Architecture
## Installation
## Running the Application
## System Prompt
## How Conversation Memory Works

## Prompt Engineering Experiment
| | Style | Prompt |
| --- | --- | --- |
| A | Minimal: Simple | You are a programming assistant. |
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
