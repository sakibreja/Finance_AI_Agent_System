# llm_utils.py

from openai import OpenAI

def init_llm():
    return OpenAI(api_key="your-api-key")

def call_llm(prompt, llm):
    response = llm.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
