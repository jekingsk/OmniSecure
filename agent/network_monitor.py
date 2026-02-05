import psutil
from datetime import datetime
from event_bus import add_event 
LOG_FILE = "../logs/events.log"

# Common safe ports
SAFE_PORTS = {80, 443, 53, 123}

def log_event(level, message):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} | {level} | {message}\n")

def monitor_network():
    connections = psutil.net_connections(kind="inet")

    for conn in connections:
        try:
            if conn.raddr:
                ip = conn.raddr.ip
                port = conn.raddr.port

                # Log unusual outbound ports
                if port not in SAFE_PORTS:
                    log_event(
                        "INFO",
                        f"Unusual outbound connection to {ip}:{port}",
                        add_event(f"Unusual outbound connection to {ip}:{port}")

                    )

        except Exception:
            continue
