# AI Resume Analyzer

This is a Python-based AI Resume Analyzer project built as part of my AI Bootcamp Day 4.

## What It Does

This tool compares a resume with a job description and provides:

- Resume match score
- Best matching skills
- Missing keywords
- ATS improvement suggestions
- Improved professional summary
- Cover letter draft
- Rewritten resume bullet points

## Tools Used

- Python
- OpenAI API
- python-dotenv
- GitHub

## Project Files

- resume_analyzer.py
- sample_resume.txt
- job_description.txt
- requirements.txt
- .gitignore
- README.md

## How To Run

1. Install dependencies:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

2. Add your OpenAI API key inside a .env file:

\`\`\`env
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4.1-mini
\`\`\`

3. Run the app:

\`\`\`bash
python resume_analyzer.py
\`\`\`

## Features

### 1. Analyze Resume Against Job Description

Compares the resume with the job description and gives a match score, strengths, weaknesses, and missing keywords.

### 2. Improve Resume Summary

Creates stronger professional summaries based on the resume.

### 3. Generate Cover Letter

Generates a short cover letter for the job role.

### 4. Rewrite Resume Bullet Points

Rewrites resume bullet points using stronger, more professional, ATS-friendly language.

## Security Note

The .env file is ignored using .gitignore so the API key is not uploaded to GitHub.

## Status

Day 4 Challenge Completed.
EOF