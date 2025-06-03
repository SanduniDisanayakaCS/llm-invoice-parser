import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_invoice_summary(text):
    prompt = f"""
    You are an invoice analyzer. Extract key details from this invoice:
    {text}

    Output format:
    - Invoice number
    - Date
    - Total Amount
    - Itemized list
    - Due Date (if mentioned)
    - Monthly summary
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return response.choices[0].message.content.strip()
