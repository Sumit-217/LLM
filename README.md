# LLM Learning Projects

This repository contains my Week 1 learning projects while working with Python, prompt engineering, structured LLM output, token usage, and resume parsing.

## Projects

| Day   | Topic                                 | Main file          |
| ----- | ------------------------------------- | ------------------ |
| Day 1 | First Groq API request                | `hello_llm.py`     |
| Day 2 | System prompts and temperature        | `sys_temp.py`      |
| Day 3 | Prompt token usage                    | `tokens.py`        |
| Day 4 | JSON output with Pydantic             | `json_pydantic.py` |
| Day 5 | Job and resume parsing                | `resume_parser.py` |
| Day 6 | Prompt engineering and classification | `prompt.py`        |

## Setup

Each day is a separate Python project. Open a day folder and install its dependencies with `uv`:

```powershell
uv sync
```

Create a `.env` file in the project folder with your Groq API key:

```text
GROQ_API_KEY=your_api_key_here
```

Run an example with:

```powershell
python .\prompt.py
```

Never commit `.env` or expose your API key. These files are excluded by `.gitignore`.
