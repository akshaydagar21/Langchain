from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,Literal
from pydantic import BaseModel,Field

load_dotenv()

model = ChatOpenAI()

class Review(BaseModel):

    key: list[str] = Field(description="Summary of topic")
    pros: Optional[list[str]] = Field(description="pros of topic")
    sentiment : Literal["pos","neg"] = Field(description="final opinion")
    cons: Optional[list[str]] = Field(description="cons of topic")

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("write down your summary")

print(result.pros)
