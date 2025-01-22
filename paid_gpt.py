import openai
from config import GPT_KEY, GPT_MODEL

def gpt_paid(prompt: str) -> str:
    openai.api_key = GPT_KEY
    try:
        response = openai.ChatCompletion.create(
            model= GPT_MODEL,
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Ошибка: {str(e)}"
