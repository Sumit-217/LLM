# Day 8: Resume-to-Job Match Evaluator

This project uses the Groq API to compare a resume against a job description and return a structured match summary. The script loads the API key from a local `.env` file, extracts key details from the resume and JD, and checks how well the candidate matches the role.

## What it does

- Reads the `GROQ_API_KEY` from `.env`
- Sends the resume text to an LLM for structured extraction
- Sends the job description to an LLM for structured extraction
- Compares both results and provides a score and verdict

## Setup

1. Open the `day8` folder.
2. Create a `.env` file in the root directory with your Groq key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

3. Install the project dependencies:

```powershell
uv sync
```

## Run

```powershell
uv run python chain.py
```

This script will print:

- extracted resume information
- extracted job description information
- final matching score and verdict

## Notes

- Never commit `.env` to Git.
- Keep the `.venv` folder and local environment files out of version control.
- The project is intended as a simple LLM-based screening workflow and can be expanded with file input, scoring rules, or a web UI.
