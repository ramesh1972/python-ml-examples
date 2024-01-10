from openai import OpenAI
import json

client = OpenAI(api_key="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")

messages = [{"role": "user", "content": "Prime Minister of India?"}]

# prompt technique
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
) 

print(response.choices[0].message.content)