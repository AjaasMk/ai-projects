import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def summarize(text: str, tone: str = "concise") -> str:
    """
    Call Gemini and return a summary.

    Args:
        text: The text to summarize
        tone: Style of summary - 'concise', 'detailed', or 'simple'

    Returns:
        Summary as a string with 3 bullet points
    """
    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"Summarize the following text in 3 bullet points. Tone: {tone}.\n\n{text}"

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error calling Gemini: {e}"


if __name__ == "__main__":
    print("=== AI News Summarizer ===\n")
    print("Paste your news article or any text below.")
    print("When done, press Enter twice:\n")

    lines = []
    while True:
        line = input()
        if line == "":
            if lines:
                break
        else:
            lines.append(line)

    user_text = "\n".join(lines)

    if not user_text.strip():
        print("No text entered. Exiting.")
    else:
        print("\nSending to Gemini...\n")
        result = summarize(user_text)
        print("Summary:")
        print(result)