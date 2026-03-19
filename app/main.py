from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

toxic_pipe = pipeline("text-classification", model="JungleLee/bert-toxic-comment-classification")
pos_neg_pipe = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-sentiment-latest")

 
class Comment(BaseModel):  #pydantic model
    text:str

#fastapi instance
app = FastAPI()

#routes
@app.get("/health")
def health():
    return {"status":"ok"}

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

@app.post("/feedback") 
def feedback(response: Comment):

    return {}  
