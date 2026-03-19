# SignalAPI

SignalAPI is a simple text moderation service that classifies comments as **Positive**, **Negative**, or **Toxic**.  
It also returns a short explanation for the decision, so you can understand why a comment was flagged.

## What it does
- **Positive**: supportive / approving comments
- **Negative**: criticism or disagreement (allowed)
- **Toxic**: abusive, hateful, racist, or harmful language (should be removed)

## How it works (high level)
SignalAPI uses a 2 pretrained NLP model from `https://huggingface.co/` to score an input comment and returns:
- the predicted category (`positive | negative | toxic`)
- a short reason/explanation

## API (planned)
- `POST /moderate` — classify a comment and return the result
  (coming soon!)
- `POST /feedback` — submit corrections (optional, for improving the model later)

## Frontend Demo
- Open `https://signalapi.co/` to use the built-in frontend.
- Type a comment in the textbox and click **Analyze Comment**.
- The frontend sends `POST /moderate` with:
  ```json
  { "text": "your comment here" }
  ```
- The API response is rendered on the page (label + reason).

## Example response
```json
{
  "label": "toxic",
  "reason": "Contains abusive or hateful language."
}
