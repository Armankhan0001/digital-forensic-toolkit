import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from .stego import lsb_score

class ForensicsWatcher(FileSystemEventHandler):

    def on_created(self, event):
        if not event.is_directory:
            score = lsb_score(event.src_path)
            print(f"[+] File created: {event.src_path}  (LSB Score: {score:.2f}%)")

    def on_modified(self, event):
        if not event.is_directory:
            score = lsb_score(event.src_path)
            print(f"[+] File modified: {event.src_path} (LSB Score: {score:.2f}%)")

    def on_deleted(self, event):
        if not event.is_directory:
            print(f"[-] File deleted: {event.src_path}")

def watch_directory(folder_path):
    """Monitors a directory in real-time and logs suspicious file modifications."""
    
    folder = Path(folder_path)

    if not folder.exists():
        print(f"[ERROR] Folder does not exist: {folder_path}")
        return

    print(f"[+] Real-Time Monitoring Started on: {folder_path}")
    print("[*] Press CTRL+C to stop watching.\n")

    event_handler = ForensicsWatcher()
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=False)

    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[+] Monitoring stopped.")
        observer.stop()

    observer.join()
