#it gives the output basically what was input , no change {2} -> 2


from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel,Runnablepassthrough

load_dotenv()

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Write the meaning of {text}',
    input_variables=['text']
)

model = ChatOpenAI()

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet':Runnablepassthrough(prompt1,model,parser),
    'linkdein':RunnableSequence(prompt2,model,parser)
}
)

print(parallel_chain.invoke({'topic':'ai'}))