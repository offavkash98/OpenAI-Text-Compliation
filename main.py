import openai
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


openai.api_key = ""

class Prompt(BaseModel):
    prompt: str

@app.post("/complete-text")
async def complete_text(request: Prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=request.prompt,
        max_tokens=10
    )
    return {"completion": response.choices[0].text.strip()}
