from fastapi import FastAPI
from pydantic import BaseModel
from .pipeline import simple_pipeline

app=FastAPI(title="LLM Quickstart" , version="0.1.0")

class chatReq(BaseModel):
    query : str
    
class ChatRes(BaseModel):
    answer: str
    
@app.post("/chat",response_model=ChatRes)
async def chat(req:chatReq):
    ans=await simple_pipeline(req.query)
    return ChatRes(answer=ans)