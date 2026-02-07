# SignalAPI

SignalAPI is a simple text moderation service that classifies comments as **Positive**, **Negative**, or **Toxic**.  
It also returns a short explanation for the decision, so you can understand why a comment was flagged.

## What it does
- **Positive**: supportive / approving comments
- **Negative**: criticism or disagreement (allowed)
- **Toxic**: abusive, hateful, racist, or harmful language (should be removed)

## How it works (high level)
SignalAPI uses a pretrained NLP model to score an input comment and returns:
- the predicted category (`positive | negative | toxic`)
- confidence scores
- a short reason/explanation

## API (planned)
- `POST /moderate` — classify a comment and return the result
- `POST /feedback` — submit corrections (optional, for improving the model later)

## Example response
```json
{
  "label": "toxic",
  "scores": {
    "positive": 0.02,
    "negative": 0.10,
    "toxic": 0.88
  },
  "reason": "Contains abusive or hateful language."
}
