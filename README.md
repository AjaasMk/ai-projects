# AI Projects — Learning Journal

Building AI automation projects from scratch. Documenting every day.

## Day 1 — News Summarizer with Gemini

A CLI tool that takes any news article as input and summarizes it 
into 3 bullet points using Google Gemini 2.5 Flash.

**Stack:** Python 3.11 · google-generativeai · python-dotenv

**How to run:**
1. Clone the repo
2. Create a virtual environment: `python -m venv env`
3. Activate it: `env\Scripts\activate` (Windows) or `source env/bin/activate` (Mac/Linux)
4. Install dependencies: `pip install google-generativeai python-dotenv`
5. Create a `.env` file and add: `GOOGLE_API_KEY=your-key-here`
6. Run: `python news_summarizer.py`

**What I learned:**
- Setting up Python virtual environments
- Calling the Gemini API from scratch
- Securing API keys with .env files
- Handling multi-line terminal input