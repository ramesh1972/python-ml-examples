from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

# Create an instance of the OpenAI class
def generate_pet_name(animal_type="dog"):
    
    prompt_template = PromptTemplate(
        input_variables=['animal_type'],
        template="I have a {animal_type} as my pet. Suggest me a name for it.",
    )

    name_chain = LLMChain(
        llm=OpenAI(api_key="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"),
        prompt=prompt_template,
    )

    response = name_chain({'animal_type': animal_type})
    print(response["text"])


generate_pet_name(animal_type="dog")