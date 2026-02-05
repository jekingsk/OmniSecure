import psutil
from datetime import datetime
from event_bus import add_event 
LOG_FILE = "../logs/events.log"

SUSPICIOUS_KEYWORDS = [
    "keylogger",
    "miner",
    "hack",
    "rat",
    "trojan"
]

def log_event(level, message):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} | {level} | {message}\n")

def monitor_processes():
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            name = proc.info['name']
            cpu = proc.cpu_percent(interval=None)  # SAFE way

            if not name:
                continue

            lower_name = name.lower()

            # 🔴 Suspicious name detection
            for keyword in SUSPICIOUS_KEYWORDS:
                if keyword in lower_name:
                    log_event(
                        "CRITICAL",
                        f"Suspicious process detected: {name} (PID {proc.pid})"
                    )
                    add_event(f"Suspicious process detected: {name}")

            # 🟡 High CPU usage detection
            if cpu > 70:    
                log_event(
                    "WARNING",
                    f"High CPU process: {name} (PID {proc.pid}) using {cpu}% CPU"
                )
                add_event(f"Suspicious process detected: {name}")
                
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
