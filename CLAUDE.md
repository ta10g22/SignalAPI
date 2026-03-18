# SignalAPI

## About the Developer
- 3rd year Electronics Engineering student, switching to ML/full-stack
- Target: big tech (FAANG+), MSc Computer Science (UCL conversion)
- Background: strong ML theory, 80+ LeetCode, C++, embedded systems, hardware design
- Doing LeetCode daily alongside these projects
- Plans to host and demo SignalAPI on YouTube for subscribers

## Project Overview
Text moderation REST API — classifies comments as **positive / negative / toxic** with confidence scores and a short reason. "Production-grade text moderation service", not just a toy classifier.

Planned roadmap (post-MVP):
- Human-in-the-loop feedback loop (false positive appeals, store labels for retraining)
- Thresholding + calibration (precision/recall tradeoffs per class)
- Latency/throughput targets, batching
- Failure analysis (sarcasm, obfuscation, emojis, multilingual)
- Monitoring (drift, performance, PII redaction on logs)
- Model versioning + canary deploys + rollback

## Tech Stack
- Python 3.12
- FastAPI + Pydantic v2
- Uvicorn (ASGI server)
- HuggingFace Transformers (local model inference — NOT OpenAI API)
- Hosting: TBD (cheap cloud, e.g. Railway or Render)
- Frontend: FastAPI /docs for now; may add Next.js + Tailwind later

## Why HuggingFace (not OpenAI)
HuggingFace runs the model locally and teaches real ML engineering (tokenization, inference pipeline, model loading). OpenAI is just an API call — any dev can do that. For an ML engineering CV, HuggingFace is more impressive and educational.

## Current State
- `app/main.py` — FastAPI skeleton complete with 3 routes returning hardcoded placeholder values
- Server runs locally via uvicorn, Swagger UI confirmed working at `/docs`
- No real model integrated yet — next step is wiring up a HuggingFace model

## Project Structure
```
SignalAPI/
├── app/
│   └── main.py
├── tests/
├── .venv/
├── requirements.txt
└── README.md
```

## API Endpoints
- `GET /health` — health check
- `POST /moderate` — classify a comment (accepts `{"text": "..."}`)
- `POST /feedback` — submit corrections (accepts `{"text": "..."}`)

## Development
- Virtual environment: `.venv/`
- Run server: `uvicorn app.main:app --reload`
- Install deps: `pip install -r requirements.txt`

## 2026 Project Roadmap
1. **SignalAPI** — toxic comment detection API (current)
2. **CineRank** — recommendation system with personalised ranked items
3. **TravelSolver** — AI-powered group travel planning app
(Extra: cat detector for MLOps learning, ShelfScanner book discovery app)

## Working Style
**The user writes all the code themselves and must understand every line.**
Claude's role:
- Explain concepts and patterns (define new terms when first introduced)
- Ask guiding questions, not give answers
- Review code and give feedback
- Help debug and troubleshoot
- Discuss architecture and tradeoffs
- Treat the user as a beginner on software (not ML theory) — explain unfamiliar terms

**Do NOT write code for the user. Do NOT paste implementations.**

## Conventions
- Pydantic models for request/response validation
- Keep routes in `app/main.py` until the project grows enough to warrant splitting
- User understands Python and C++ — no need to explain basic syntax
