# Day 9: Streaming LLM Responses

This project demonstrates how to stream a response from the Groq API as it is generated. Instead of waiting for the complete answer, the script prints each content chunk immediately.

## What it does

- Loads `GROQ_API_KEY` from a local `.env` file
- Sends a prompt to the Groq chat completions API
- Enables streaming with `stream=True`
- Prints response chunks progressively to the terminal

## Setup

1. Open the `day9` folder.
2. Create a `.env` file with your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

3. Install the project dependencies:

```powershell
uv sync
```

## Run

```powershell
uv run python streaming.py
```

The example prompt asks the model to explain how the internet works. Update `prompt` in `streaming.py` to try another question.

## Notes

- Never commit `.env` or expose your API key.
- Streaming is useful for improving perceived response speed in interactive applications.
- The script uses the `openai/gpt-oss-120b` model through Groq.
