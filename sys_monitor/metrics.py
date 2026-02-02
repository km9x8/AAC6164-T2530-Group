import time
import csv
import psutil
from pathlib import Path
from datetime import datetime

# ==============================
# Paths (absolute, safe)
# ==============================
BASE_DIR = Path(__file__).resolve().parents[1]
LOG_DIR = BASE_DIR / "output" / "logs"
LOG_FILE = LOG_DIR / "system_metrics.csv"

LOG_DIR.mkdir(parents=True, exist_ok=True)

# ==============================
# Active uptime (script runtime)
# ==============================
START_TIME = time.time()

# ==============================
# CSV header
# ==============================
CSV_HEADER = [
    "timestamp",
    "cpu_percent",
    "mem_percent",
    "mem_used",
    "mem_total",
    "disk_percent",
    "disk_used",
    "disk_total",
    "processes",
    "system_uptime",
    "active_uptime",
]

def write_header_if_needed():
    if not LOG_FILE.exists():
        with open(LOG_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(CSV_HEADER)

def collect_metrics():
    cpu_percent = psutil.cpu_percent(interval=1)

    mem = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    processes_count = len(psutil.pids())

    system_uptime = time.time() - psutil.boot_time()
    active_uptime = time.time() - START_TIME

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return [
        timestamp,
        cpu_percent,
        mem.percent,
        mem.used,
        mem.total,
        disk.percent,
        disk.used,
        disk.total,
        processes_count,
        round(system_uptime, 2),
        round(active_uptime, 2),
    ]

def append_metrics(row):
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(row)

def main():
    print("System metrics monitoring started...")
    print("Logging to:", LOG_FILE)

    write_header_if_needed()

    while True:
        row = collect_metrics()
        append_metrics(row)
        time.sleep(3)   # sampling interval

if __name__ == "__main__":
    main()
   
# System Performance & Resource Monitoring
# Author: Osama
