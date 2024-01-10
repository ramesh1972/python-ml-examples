from openai import OpenAI
import json


client = OpenAI(api_key="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")

messages = [{"role": "system", "content": "you are a census officer"},
            {"role": "assistant", "content": "you provide data on demographics"},
            {"role": "user", "content": "provide in json format the population of each state in united states"}]

# prompt technique
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
) 

print(response.choices[0].message.content)