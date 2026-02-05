from collections import deque

event_window = deque(maxlen=8)

def add_event(event: str):
    event_window.append(event)

def get_event_summary():
    summary = "Recent security-relevant events:\n"
    for e in event_window:
        summary += f"- {e}\n"
    return summary

def clear_events():
    event_window.clear()
