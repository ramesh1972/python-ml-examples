from openai import OpenAI
import json

client = OpenAI(api_key="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")

messages = [{"role": "system", "content": "you are a math teacher!"},
            {"role": "user", "content": "you are good at math problems"},
            {"role": "user", "content": "what is 5!"},]

# prompt technique
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
) 

for message in messages:
    print(message)

print("---------------------")
print("response");

print(response.choices[0].message.content)