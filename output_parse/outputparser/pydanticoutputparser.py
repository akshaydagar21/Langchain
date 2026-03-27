from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser,PydanticOutputParser
from pydantic import BaseModel,Field

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)


class Person(BaseModel):
    name: str = Field(description='Name of a person')
    age: int = Field(gt=18 , description='Age of a person')


parser = PydanticOutputParser(pydantic_object=Person)


template = PromptTemplate(
    template='generate a name , age of a {place} person \n {format_instruction} ',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'place':'india'})

print(result)