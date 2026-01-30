print("Monitoring started...")
import os
import time
import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
MONITORED_DIR = BASE_DIR / "monitored_dir"
LOG_FILE = BASE_DIR / "output" / "logs" / "dir_changes.csv"

def snapshot_directory(directory: Path):
    snapshot = {}
    directory.mkdir(parents=True, exist_ok=True)

    for item in directory.iterdir():
        try:
            stats = item.lstat()
            snapshot[item.name] = {
                "size": stats.st_size,
                "mtime": stats.st_mtime,
                "mode": stats.st_mode,
                "uid": stats.st_uid,
                "gid": stats.st_gid
            }
        except FileNotFoundError:
            continue

    return snapshot

def detect_changes(old_state: dict, new_state: dict):
    created = []
    deleted = []
    modified = []

    old_files = set(old_state.keys())
    new_files = set(new_state.keys())

    for name in new_files - old_files:
        created.append(name)

    for name in old_files - new_files:
        deleted.append(name)

    for name in old_files & new_files:
        old_info = old_state[name]
        new_info = new_state[name]

        if (old_info["size"] != new_info["size"] or
            old_info["mtime"] != new_info["mtime"] or
            old_info["mode"] != new_info["mode"]):
            modified.append(name)

    return created, deleted, modified

if __name__ == "__main__":
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

    if not LOG_FILE.exists():
        with open(LOG_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "event", "filename", "size", "mtime", "mode", "uid", "gid"])

    prev_state = snapshot_directory(MONITORED_DIR)

    while True:
        time.sleep(3)
        curr_state = snapshot_directory(MONITORED_DIR)

        created, deleted, modified = detect_changes(prev_state, curr_state)

        ts = time.strftime("%Y-%m-%d %H:%M:%S")

        with open(LOG_FILE, "a", newline="") as f:
            writer = csv.writer(f)

            for name in created:
                info = curr_state[name]
                writer.writerow([ts, "CREATED", name, info["size"], info["mtime"], info["mode"], info["uid"], info["gid"]])

            for name in deleted:
                writer.writerow([ts, "DELETED", name, "", "", "", "", ""])

            for name in modified:
                info = curr_state[name]
                writer.writerow([ts, "MODIFIED", name, info["size"], info["mtime"], info["mode"], info["uid"], info["gid"]])

        prev_state = curr_state
