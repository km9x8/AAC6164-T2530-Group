# Section A – Directory Monitoring (Ahmed)

## Purpose
Track file system events (create/modify/delete) inside `monitored_dir` and log changes into CSV.

## How to run
1) Start monitor:
   cd dir_monitor
   python3 monitor.py

2) In another terminal, trigger events:
   cd monitored_dir
   touch A.txt B.txt
   echo "hello" > D.txt
   rm A.txt
   echo "update" >> D.txt

3) View log:
   tail -n 20 ../output/logs/dir_changes.csv

## Output
- CSV file: output/logs/dir_changes.csv
- Columns include timestamp, event_type, file_name/path (depends on implementation)
