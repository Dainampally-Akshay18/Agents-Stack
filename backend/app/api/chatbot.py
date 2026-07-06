import os

from dotenv import load_dotenv
from fastapi import APIRouter
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from pydantic import BaseModel

chatbot_router=APIRouter()
load_dotenv()

llm=ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.get_env("GROQ_API_KEY"),
)

class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    response: str
    

@chatbot_router.post("/chatbot",response_model=ChatResponse)
async def chat(request:ChatRequest):
    respone = llm.invoke([HumanMessage(content=request.question)])
    return ChatResponse(response=respone.content)