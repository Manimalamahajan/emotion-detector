# Watson Emotion Detector 🧠

A simple emotion detection app using IBM Watson NLU API, Flask, and Docker.

## Features
- Detects emotions from text
- CLI and web interface
- Error handling & tests
- Deployable with Docker

## Setup
```bash
git clone https://github.com/your-username/emotion-detector.git
cd emotion-detector
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

Set your Watson credentials in a `.env` file (see `.env.example`).

## Run Flask App
```bash
python -m app.web
```

## Run CLI
```bash
emotion-detect "I am feeling very happy and joyful today!"
```

## Run Tests
```bash
pytest
```

## Docker Deployment
```bash
docker-compose up --build
```
