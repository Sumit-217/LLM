# Day 7: Tool-Using Shopping Agent

This project demonstrates a simple shopping assistant that can call tools to
look up product prices and calculate the remaining balance.

## Setup

Requirements:

- Python 3.13+
- uv
- A Groq API key

Create a `.env` file in the repository root:

```env
GROQ_API_KEY=your_groq_api_key
```

Install the project dependencies from the `day7` directory:

```powershell
uv sync
```

## Run

From `week2/day7`, run the script with the project environment:

```powershell
uv run python react.py
```

The `.env` file must contain `GROQ_API_KEY`. Never commit the `.env` file or
your API key to Git.
