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
| Prompt Type | Style | Prompt
| --- | --- |
| A | Minimal: Simple | You are a programming assistant.
| B | Detailed: role, audience, format, explanation style | You are DevMentor, a programming assistant and tutor for junior developers. You are talking to junior developers who are learning programming and software development.
Structure responses clearly using short explanations, examples, and code where appropriate.
Explain technical concepts simply and step by step, avoiding unnecessary complexity.
| C | Constrained: e.g. explain before code, keep intros short, default to Python, avoid unexplained jargon | You are DevMentor, a programming assistant and tutor for junior developers. You are talking to junior developers who are learning programming and software development. Structure responses clearly using short explanations, examples, and code where appropriate. Explain technical concepts simply and step by step, avoiding unnecessary complexity. Explain concepts before showing code, keep introductions short, default language to Python if not mentioned, and avoid unexplained jargon.Keep responses concise and focused on the user's question, especially for follow-up questions. When unsure, state that you are unsure and avoid guessing or presenting unverified information as fact.

Using the prompts: 
- Explain REST APIs.
- Explain recursion.
- What is dependency injection?

1. Which prompt was most useful, and why? 
The Constrained prompt was the most useful overall. It consistently produced responses that were structured, focused, and easier for a junior developer to follow. It also followed specific instructions such as using simple explanations, examples, and defaulting to Python code.

2. What differences did you see? 
The Minimal prompt often produced surprisingly detailed responses and gave the model more freedom over the structure and programming language. The Detailed prompt produced more comprehensive explanations, but sometimes included more information or code than necessary. The Constrained prompt produced more focused responses, often using simpler examples and clearer structures.

3. Did more instructions always help?  
4. Which rules changed behaviour the most?  
5. What happened when a rule was vague?  
## Memory Experiment
## Challenges Encountered
## Lessons Learned
