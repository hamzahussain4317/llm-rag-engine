from .core.llm_client import ask_llm

async def simple_pipeline(user_query:str)->str:
    return await ask_llm(user_query)
