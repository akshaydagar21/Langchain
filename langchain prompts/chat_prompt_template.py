from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('System','You are a helpful {domain} expert'),
    ('human','Explain the {topic} in simple terms')
])

prompts = chat_template.invoke({'domain':'cricket','topic':'spin'})

print(prompts)