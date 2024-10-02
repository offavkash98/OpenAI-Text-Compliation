from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class Prompt(BaseModel):
    prompt: str

@app.post("/complete-text")
async def complete_text(request: Prompt):
    return {"completion": f"You provided the prompt: '{request.prompt}'"}
