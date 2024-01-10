import openai
import json
import time
import os

openai.api_key="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"

timestamp = time.strftime("%Y_%m_%d-%H_%M_%S", time.gmtime())
filename = timestamp + ".txt"

if not os.path.exists(filename):
    with open(filename, 'w') as f:
        f.write("User: Welcome to OpenAI chat!\n")

discussions=[{"role": "system", 
              "content": "You are a helpful assistant."}]

while (True):
    p=input("Enter quit to quit, or enter your prompt: ")
    if (p=="quit"):
        break
    
    discussions.append({"role": "user", "content":p})
    
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=discussions
        )

    response = completion.choices[0].message.content
        
    discussions.append({"role": "assistant", "content": response})
    
    with open(filename, 'a') as f:
        f.write("User: " + p + "\n")
        f.write("AI: " + response + "\n")
    
    print("\nAI says: ", response, "\n")

print("Have a nice day!")