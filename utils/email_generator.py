import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_email(points, tone, recipient, sender, subject):

    subject_text = "Include subject line." if subject else "No subject line."

    prompt = f"""
Write a {tone} email to a {recipient}.

{subject_text}

Use these bullet points:
{points}

Sign from {sender}

Only write email.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text