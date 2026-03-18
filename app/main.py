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
    toxic_true = print(toxic_pipe(comment.text))
    if toxic_true[0] == "toxic":
        return {"label": "toxic",
                "reason": "Contains abusive or hateful language." }
    
    else:
        pos_or_neg = print(pos_neg_pipe(comment.text)) 
        if pos_or_neg[0] == "positive":
             return {"label": "positive",
                     "reason": "Contains postive feedback." }
        

        elif pos_or_neg[0] == "negative":
             return {"label": "negative",
                     "reason": "Contains critism or negative feedback." }
        
        elif pos_or_neg[0] == "neutral":
             return {"label": "negative",
                     "reason": "Contains critism or negative feedback." }

@app.post("/feedback") 
def feedback(response: Comment):

    return {}  
