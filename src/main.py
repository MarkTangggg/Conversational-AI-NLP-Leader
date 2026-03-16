from fastapi import FastAPI
from pydantic import BaseModel
from src.core.orchestrator import AIOrchestrator

app = FastAPI(title="Conversational AI API")
orchestrator = AIOrchestrator()

class QueryRequest(BaseModel):
    prompt: str

@app.post("/v1/chat")
async def chat(request: QueryRequest):
    response = orchestrator.process_query(request.prompt)
    return {"status": "success", "response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
