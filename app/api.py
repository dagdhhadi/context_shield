from fastapi import FastAPI
from pydantic import BaseModel
from context_shield.rewrite import clean_rewrite

app = FastAPI()

class TextIn(BaseModel):
    text: str

class TextOut(BaseModel):
    rewrite: str

@app.post("/rewrite", response_model=TextOut)
def rewrite_text(payload: TextIn):
    safe = clean_rewrite(payload.text)
    return {"rewrite": safe}
