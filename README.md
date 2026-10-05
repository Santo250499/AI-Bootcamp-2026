# AI Bootcamp 2026

Personal Python practice repo from an AI bootcamp. It mixes small console exercises with a few OpenAI-backed scripts (resume analysis, chatbot menu, email draft). This is a learning workspace from the bootcamp.

## Purpose

Exercises covering:

- Basic Python (dicts, menus, input/output)
- Calling a public HTTP API (`requests`)
- Loading secrets from `.env` with `python-dotenv`
- Using the OpenAI Responses API for text tasks

## Files

| File | What it does |
|---|---|
| `resume_analyzer.py` | Menu-driven CLI: compare `sample_resume.txt` to `job_description.txt`, improve the summary, generate a cover letter, and rewrite bullet points via OpenAI. |
| `Chatbot.py` | Menu CLI (ask, summarize, translate, explain code, exit). Option **6 (IT Helpdesk Assistant)** is listed but has an empty body, so choosing it does nothing. |
| `email_writer.py` | Prompts for a topic and prints one professional email from OpenAI. |
| `employee_system.py` | In-memory employee list (add, search, view). No database and no AI. |
| `ICT_Device.py` | Asks for username, device type, and encryption and MFA yes/no answers; prints compliant or not compliant. Local logic only. |
| `github_API.py` | `GET https://api.github.com/users/octocat` and prints the status code, login, followers, public repos, and location. |
| `json_practice.py` | Prints a hard-coded employee dict, then name, department, and each skill. |
| `sample_resume.txt` / `job_description.txt` | Sample inputs for the resume analyzer. |
| `Resume_Analyzer_README.txt` | Notes for the Day 4 resume analyzer challenge. Separate from this README. |
| `Day 2` | Empty placeholder file. |
| `Programming with Mosh – Python for Begin.py` | Single line: `print("Hello AI")`. |
| `.env.example` | `OPENAI_API_KEY=your_api_key_here` |
| `requirements.txt` | `openai`, `python-dotenv`, and `requests`. |

## Tech stack

- Python 3
- `openai` (Responses API)
- `python-dotenv`
- `requests` (`github_API.py`)

## Environment variables

`.env.example` only contains the API key:

```env
OPENAI_API_KEY=your_api_key_here
```

`resume_analyzer.py` also reads `OPENAI_MODEL` and defaults to `gpt-4.1-mini` when it is unset. `Chatbot.py` and `email_writer.py` hard-code model `gpt-4.1-mini` and only need the API key. `.env` is gitignored. `venv/` is gitignored as well.

Optional override, used only by `resume_analyzer.py`:

```env
OPENAI_MODEL=gpt-4.1-mini
```

## How to run

```bash
git clone https://github.com/Santo250499/AI-Bootcamp-2026.git
cd AI-Bootcamp-2026
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then paste your real key locally
python resume_analyzer.py
# or: python email_writer.py
# or: python Chatbot.py
```

`employee_system.py`, `ICT_Device.py`, `json_practice.py`, and `Programming with Mosh – Python for Begin.py` do not need an API key. `github_API.py` only needs network access.

## Project structure

```text
AI-Bootcamp-2026/
├── resume_analyzer.py
├── Chatbot.py
├── email_writer.py
├── employee_system.py
├── ICT_Device.py
├── github_API.py
├── json_practice.py
├── sample_resume.txt
├── job_description.txt
├── Resume_Analyzer_README.txt
├── Day 2
├── Programming with Mosh – Python for Begin.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```
