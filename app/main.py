from fastapi import FastAPI ,UploadFile , File ,Form
from pydantic import BaseModel
from .pipeline import simple_pipeline , pipeline_with_doc
import tempfile
import shutil

app=FastAPI(title="LLM Quickstart" , version="0.1.0")

class chatReq(BaseModel):
    query : str
    
class ChatRes(BaseModel):
    answer: str
    
@app.post("/chat",response_model=ChatRes)
async def chat(req:chatReq):
    ans=await simple_pipeline(req.query)
    return ChatRes(answer=ans)

@app.post("/chat-with-doc",response_model=ChatRes)
async def chat_with_doc(query:str =Form(...),file:UploadFile=File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        shutil.copyfileobj(file.file,tmp)
        file_path=tmp.name
    
    ans=await pipeline_with_doc(query,file_path)
    return ChatRes(answer=ans)