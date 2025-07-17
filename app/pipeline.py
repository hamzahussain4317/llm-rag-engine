from .core.llm_client import ask_llm
from .core.document_utils import extract_text_from_pdf

async def simple_pipeline(user_query:str)->str:
    return await ask_llm(user_query)

async def pipeline_with_doc(user_query:str,file_path:str)->str:
    doc_text =extract_text_from_pdf(file_path)
    
    prompt=f"""Here is a document:\n{doc_text}\n\nNow answer this question based on the above document:\n{user_query}"""
    return await ask_llm(prompt)