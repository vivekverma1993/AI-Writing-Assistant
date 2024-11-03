import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_text(prompt):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',  # Use the appropriate model like 'gpt-4' if available
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.7
    )
    return response['choices'][0]['message']['content'].strip()
