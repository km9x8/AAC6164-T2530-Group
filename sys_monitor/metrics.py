import time
import csv
import psutil
from pathlib import Path

LOG_FILE = Path("output/logs/system_metrics.csv")

def collect_metrics():
    cpu_percent = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    processes_count = len(psutil.pids())

    return {
        "cpu_percent": cpu_percent,
        "mem_percent": mem.percent,
        "mem_used": mem.used,
        "mem_total": mem.total,
        "disk_percent": disk.percent,
        "disk_used": disk.used,
        "disk_total": disk.total,
        "processes": processes_count
    }
if __name__ == "__main__":
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

    if not LOG_FILE.exists():
        with open(LOG_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "timestamp",
                "cpu_percent",
                "mem_percent",
                "mem_used",
                "mem_total",
                "disk_percent",
                "disk_used",
                "disk_total",
                "processes"
            ])

    while True:
        metrics = collect_metrics()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        with open(LOG_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                timestamp,
                metrics["cpu_percent"],
                metrics["mem_percent"],
                metrics["mem_used"],
                metrics["mem_total"],
                metrics["disk_percent"],
                metrics["disk_used"],
                metrics["disk_total"],
                metrics["processes"]
            ])

        time.sleep(3)
