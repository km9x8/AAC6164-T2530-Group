#!/usr/bin/env bash
set -e

BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
MON_DIR="$BASE_DIR/monitored_dir"
LOG="$BASE_DIR/output/logs/dir_changes.csv"

touch "$MON_DIR/A.txt" "$MON_DIR/B.txt" "$MON_DIR/C.txt"
echo "hello" > "$MON_DIR/D.txt"
rm -f "$MON_DIR/A.txt"
echo "update" >> "$MON_DIR/D.txt"

echo "Events triggered."
echo "Last 10 log lines:"
tail -n 10 "$LOG" || true
