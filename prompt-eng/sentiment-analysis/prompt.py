from openai import OpenAI
import json

client = OpenAI(api_key="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")

messages = [{"role": "system", "content": "you are a sentiment analsyer"},
            {"role": "user", "content": "   "},
            {"role": "user", "content": "the product is working well"},]

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