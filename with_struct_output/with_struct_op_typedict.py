from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated

load_dotenv()

model = ChatOpenAI()

class Review(TypedDict):
    key: Annotated[str,"Summary of the topic"]
    pro: Annotated[str,"pros of this topic"]
    con: Annotated[str,"cons of the topic"]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("write down your summary")

print(result)
