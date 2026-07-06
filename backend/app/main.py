from fastapi import FastAPI
from app.api.chatbot import chatbot_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


app.add_middleware(
    CORSMiddleware, 
allow_origins=["*"],
allow_methods=["*"],
allow_headers=["*"],
)

@app.get("/")
async def read():
    return {"message":"This is a sample API endpoint "}

@app.get("/hello")
async def hello():
    return {"Data":"This is hello endpoint"}

app.include_router(chatbot_router, prefix="/api", tags=["chatbot"])