# Gen AI Agent

A simple Agentic AI project built with Python that demonstrates how an LLM can reason, choose tools, maintain memory, and solve user requests through a multi-step execution loop.

## Features

- LLM-powered reasoning
- Tool calling (Calculator & Weather)
- Agent memory using state/history
- Think → Act → Observe workflow
- JSON-based decision making

## Tech Stack

- Python
- Groq API (OpenAI-compatible SDK)
- python-dotenv

## Setup

1. Clone the repository.
2. Create a virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

5. Run the agent:

```bash
python agent.py
```

## Example

```
Enter Goal:
What is 25 * 40?
```

The agent decides whether to use a tool, executes it if needed, stores the result in memory, and returns the final answer.