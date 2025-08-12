from dotenv import load_dotenv
import os
from openai import OpenAI  # Replace with your GenAI client

load_dotenv()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

def query_agent(prompt, parsed_data):
    context = f"""You are a log analysis expert. Here's the parsed log data:

{parsed_data}

Now answer this question:
{prompt}
"""
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": context}],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()