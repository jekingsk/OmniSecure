import psutil
import time
from datetime import datetime
from process_monitor import monitor_processes
import threading
from file_monitor import start_file_monitor
from network_monitor import monitor_network
from anomaly_detector import train_model, detect_anomaly
from ai_analyzer import analyze_threat
LOG_FILE = "../logs/events.log"

from collections import deque

event_window = deque(maxlen=8)

def add_event(event):
    event_window.append(event)

def build_event_summary():
    summary = "Recent security-relevant events:\n"
    for e in event_window:
        summary += f"- {e}\n"
    return summary

def log_event(level, message):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} | {level} | {message}\n")

def monitor_system():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent

    if cpu > 80:
        log_event("WARNING", f"High CPU usage detected: {cpu}%")

    if memory > 85:
        log_event("WARNING", f"High memory usage detected: {memory}%")

    #print(f"CPU: {cpu}% | Memory: {memory}%")

def main():
    log_event("INFO", "Security Monitoring Agent started")

    # Prime CPU counters
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent(interval=None)
        except Exception:
            pass

    # Start file monitor thread
    file_thread = threading.Thread(
        target=start_file_monitor,
        daemon=True
    )
    file_thread.start()

    # Train AI model once at startup
    train_model()

    while True:
        monitor_system()
        monitor_processes()
        monitor_network()
        detect_anomaly()
        time.sleep(5)





if __name__ == "__main__":
    main()
THREAT_THRESHOLD = 60  # example score

if threat_score >= THREAT_THRESHOLD:
    summary = build_event_summary()
    analyze_threat(summary)
    reset_score()