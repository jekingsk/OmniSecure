import psutil
import numpy as np
from datetime import datetime
from sklearn.ensemble import IsolationForest

LOG_FILE = "../logs/events.log"

def log_event(level, message):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} | {level} | {message}\n")

# 🔹 Initialize model
model = IsolationForest(
    n_estimators=100,
    contamination=0.03,
    random_state=42
)

def collect_features():
    return [
        psutil.cpu_percent(),
        psutil.virtual_memory().percent,
        len(psutil.pids()),
        len(psutil.net_connections())
    ]

def train_model():
    log_event("INFO", "Training anomaly detection model")

    data = []
    for _ in range(60):  # ~1 minute baseline
        data.append(collect_features())

    model.fit(np.array(data))
    log_event("INFO", "Anomaly detection model trained")

def detect_anomaly():
    features = np.array(collect_features()).reshape(1, -1)
    prediction = model.predict(features)

    if prediction[0] == -1:
        log_event(
            "CRITICAL",
            "Anomalous system behavior detected (AI)"
        )
