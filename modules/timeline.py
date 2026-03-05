import os, datetime
from pathlib import Path
import matplotlib.pyplot as plt

def build_timeline(folder):
    folder = Path(folder)
    events = []

    for file in folder.rglob('*'):
        if file.is_file():
            stat = file.stat()
            events.append(f"{datetime.datetime.fromtimestamp(stat.st_mtime)} - {file}")

    return sorted(events)

def plot_timeline(events):
    times = [datetime.datetime.fromisoformat(e.split(' - ')[0]) for e in events]
    plt.scatter(times, [1]*len(times))
    plt.gcf().autofmt_xdate()
    plt.title("Timeline Analysis")
    plt.show()
