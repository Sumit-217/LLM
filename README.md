# LLM Learning Projects

This repository contains my Week 1 learning projects while working with Python, prompt engineering, structured LLM output, token usage, resume parsing, and agent-style workflows.

## Projects

| Day   | Topic                                 | Main file          |
| ----- | ------------------------------------- | ------------------ |
| Day 1 | First Groq API request                | `hello_llm.py`     |
| Day 2 | System prompts and temperature        | `sys_temp.py`      |
| Day 3 | Prompt token usage                    | `tokens.py`        |
| Day 4 | JSON output with Pydantic             | `json_pydantic.py` |
| Day 5 | Job and resume parsing                | `resume_parser.py` |
| Day 6 | Prompt engineering and classification | `prompt.py`        |
| Day 7 | Tool-using agent / shopping assistant | `react.py`         |
| Day 8 | Resume-to-job matching with Groq      | `chain.py`         |
| Day 9 | Streaming LLM responses               | `streaming.py`     |

## Setup

Each day is a separate Python project. Open a day folder and install dependencies using `uv`:

```powershell
uv sync
```

Create a `.env` file in the project folder with your Groq API key:

```text
GROQ_API_KEY=your_api_key_here
```

Run a script from inside the day folder:

```powershell
uv run python .\streaming.py
```

Never commit `.env` or expose your API key. These files are excluded by the local `.gitignore` in each day folder.

## Notes

- This week focuses on learning how LLMs can be used for simple workflows, extraction, matching, tool-based reasoning, and streaming responses.
- The structure is intentionally modular so each day can be explored independently.
- The root project is a learning log, while each day folder contains its own isolated setup and examples.
