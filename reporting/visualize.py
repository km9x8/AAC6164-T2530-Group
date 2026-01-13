import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA_FILE = Path("output/logs/system_metrics.csv")
PLOTS_DIR = Path("output/plots")

PLOTS_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA_FILE)

df["timestamp"] = pd.to_datetime(df["timestamp"])

plt.figure()
plt.plot(df["timestamp"], df["cpu_percent"])
plt.xlabel("Time")
plt.ylabel("CPU Usage (%)")
plt.title("CPU Usage Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(PLOTS_DIR / "cpu_usage.png")
plt.close()

plt.figure()
plt.plot(df["timestamp"], df["mem_percent"])
plt.xlabel("Time")
plt.ylabel("Memory Usage (%)")
plt.title("Memory Usage Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(PLOTS_DIR / "memory_usage.png")
plt.close()

plt.figure()
plt.plot(df["timestamp"], df["disk_percent"])
plt.xlabel("Time")
plt.ylabel("Disk Usage (%)")
plt.title("Disk Usage Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(PLOTS_DIR / "disk_usage.png")
plt.close()

print("Plots generated successfully.")

