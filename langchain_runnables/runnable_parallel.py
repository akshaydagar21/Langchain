from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel

load_dotenv()

prompt1 = PromptTemplate(
    template='Write a tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Write a linkedIn post of {topic}',
    input_variables=['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet':RunnableSequence(prompt1,model,parser),
    'linkdein':RunnableSequence(prompt2,model,parser)
}
)

print(parallel_chain.invoke({'topic':'ai'}))