from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from transformers import pipeline

APP_DIR = Path(__file__).resolve().parent
STATIC_DIR = APP_DIR / "static"

toxic_pipe = pipeline("text-classification", model="JungleLee/bert-toxic-comment-classification")
pos_neg_pipe = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-sentiment-latest")

class Comment(BaseModel):
    text: str

#fastapi instance
app = FastAPI()
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/", include_in_schema=False)
def index():
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/moderate")
def moderate(comment: Comment):
    result = toxic_pipe(comment.text)
    toxic_true = result[0]
    if toxic_true["label"] == "toxic":
        return {"label": "toxic",
                "reason": "Contains abusive or hateful language." }
    
    else:
        result = pos_neg_pipe(comment.text)
        pos_or_neg = result[0]
        if pos_or_neg["label"] == "positive":
             return {"label": "positive",
                     "reason": "Contains postive feedback." }

        elif pos_or_neg["label"] == "negative":
             return {"label": "negative",
                     "reason": "Contains critism or negative feedback." }
        
        elif pos_or_neg["label"] == "neutral":
             return {"label": "negative",
                     "reason": "Contains critism or negative feedback." }

        else:
             return {"label": "unknown",
                     "reason": f"Could not classify label: {pos_or_neg['label']}" }


@app.post("/feedback")
def feedback(response: Comment):
    return {}
