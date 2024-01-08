from openai import OpenAI
import json

client = OpenAI(api_key="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")

response = client.models.list()

print(response.data)

for model in response.data:
    print(model.id)
    print(model.owned_by)
    print("--------------")