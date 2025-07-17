import httpx
import asyncio

OLLAMA_HOST = "http://localhost:11434"
MODEL_TAG   = "falcon3:1b"   

async def ask_llm(question: str) -> str:
    payload = {
        "model": MODEL_TAG,
        "messages": [
            {"role": "user", "content": question}
        ],
        "stream":False
    }

    async with httpx.AsyncClient() as client:
        r = await client.post(f"{OLLAMA_HOST}/api/chat", json=payload, timeout=120)

    # Basic error handling
    if r.status_code != 200:
        raise RuntimeError(f"Ollama error {r.status_code}: {r.text}")

    data = r.json()
    # Ollama returns:  {"message": {"role":"assistant","content":"…"}, ...}
    return data["message"]["content"].strip()
