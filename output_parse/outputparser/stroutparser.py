from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI()

#1prompt = detailed report
template1 = PromptTemplate(
    template= 'Write a detailded report on {topic}',
    input_variables = ['topic']
)

#2 prompt = summary report
template2 = PromptTemplate(
    template= 'Write a summary on the following {text}',
    input_variables = ['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)