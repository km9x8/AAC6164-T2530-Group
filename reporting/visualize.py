import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
LOG_FILE = BASE_DIR / "output" / "logs" / "system_metrics.csv"
PLOTS_DIR = BASE_DIR / "output" / "plots"

PLOTS_DIR.mkdir(parents=True, exist_ok=True)

# ======================
# Load data
# ======================
df = pd.read_csv(LOG_FILE)

# Convert timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"])

# ======================
# Basic processing
# ======================
cpu_avg = df["cpu_percent"].mean()
cpu_max = df["cpu_percent"].max()

print(f"Average CPU Usage: {cpu_avg:.2f}%")
print(f"Max CPU Usage: {cpu_max:.2f}%")

# ======================
# CPU Usage Plot
# ======================
plt.figure()
plt.plot(df["timestamp"], df["cpu_percent"])
plt.xlabel("Time")
plt.ylabel("CPU Usage (%)")
plt.title("CPU Usage Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(PLOTS_DIR / "cpu_usage.png")
plt.close()

# ======================
# Memory Usage Plot
# ======================
plt.figure()
plt.plot(df["timestamp"], df["mem_percent"])
plt.xlabel("Time")
plt.ylabel("Memory Usage (%)")
plt.title("Memory Usage Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(PLOTS_DIR / "memory_usage.png")
plt.close()

# ======================
# Disk Usage Plot
# ======================
plt.figure()
plt.plot(df["timestamp"], df["disk_percent"])
plt.xlabel("Time")
plt.ylabel("Disk Usage (%)")
plt.title("Disk Usage Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(PLOTS_DIR / "disk_usage.png")
plt.close()

print("Plots saved to:", PLOTS_DIR)

