import os
import requests
from datetime import datetime

AI_KEY = os.getenv("OMNISECURE_AI_KEY")
AI_ENDPOINT = "https://api.scaledown.ai/v1/chat/completions"
MODEL_NAME = "gpt-4.1-mini"  # change if Scaledown gives a specific model

LOG_FILE = "../logs/events.log"

def log_event(level, message):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} | {level} | {message}\n")

def analyze_threat(event_summary: str):
    """
    Sends summarized security events to AI for threat analysis
    """

    if not AI_KEY:
        log_event("ERROR", "AI API key not found in environment")
        return None

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are an advanced cybersecurity threat analysis engine. "
                    "Analyze system behavior and determine threat level. "
                    "Respond with:\n"
                    "- Threat Level (Low/Medium/High/Critical)\n"
                    "- Short reasoning\n"
                    "- Recommended action"
                )
            },
            {
                "role": "user",
                "content": event_summary
            }
        ],
        "temperature": 0.2
    }

    headers = {
        "Authorization": f"Bearer {AI_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(
            AI_ENDPOINT,
            json=payload,
            headers=headers,
            timeout=10
        )

        if response.status_code == 200:
            verdict = response.json()["choices"][0]["message"]["content"]
            log_event("CRITICAL", f"AI Threat Analysis:\n{verdict}")
            return verdict
        else:
            log_event(
                "ERROR",
                f"AI API error {response.status_code}: {response.text}"
            )
            return None

    except Exception as e:
        log_event("ERROR", f"AI request failed: {str(e)}")
        return None
