from openai import OpenAI
import json


client = OpenAI(api_key="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")

messages = [{"role": "user", "content": "What's the captial of Inida?"}]

# prompt technique
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
) 

print(response.choices[0].message.content)