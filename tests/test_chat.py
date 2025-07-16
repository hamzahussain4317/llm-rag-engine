import asyncio ,os
from app.pipeline import simple_pipeline

def test_llm_call():
    if not os.getenv("OPENAI_API_KEY"):
        assert True
        return
    resp=asyncio.run(simple_pipeline("1+1?"))
    assert "2" in resp