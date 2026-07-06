from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

topic = input("What is the email about? ")

prompt = f"""
Write a professional business email about:

{topic}

Include:

Greeting

Body

Professional closing
"""

response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

print("\nGenerated Email:\n")
print(response.output_text)