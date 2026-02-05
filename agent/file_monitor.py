from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime
import time
from event_bus import add_event 
LOG_FILE = "../logs/events.log"
WATCH_DIR = "../watch_dir"

def log_event(level, message):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} | {level} | {message}\n")

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        if not event.is_directory:
            log_event("INFO", f"File created: {event.src_path}")
            add_event(f"File deleted: {event.src_path}")


    def on_modified(self, event):
        if not event.is_directory:
            log_event("WARNING", f"File modified: {event.src_path}")

    def on_deleted(self, event):
        if not event.is_directory:
            log_event("CRITICAL", f"File deleted: {event.src_path}")

def start_file_monitor():
    observer = Observer()
    observer.schedule(FileEventHandler(), WATCH_DIR, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
