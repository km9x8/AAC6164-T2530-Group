# Osama – System Metrics Monitoring Evidence

## Objective
Verify that the system metrics monitoring module correctly records CPU, memory,
and disk usage into a CSV log file.

## Execution
Command used to verify logging:
tail -n 5 output/logs/system_metrics.csv

## Sample Output
2026-01-31 17:24:14,2.6,30.7,1246830592,4058759168,58.2,13868937216,25130254336,215,9752.37,113.23
2026-01-31 17:24:18,2.6,30.7,1246830592,4058759168,58.2,13868937216,25130254336,215,9756.38,117.24
2026-01-31 17:24:22,5.5,30.7,1246822400,4058759168,58.2,13868937216,25130254336,215,9760.38,121.24
2026-01-31 17:24:26,0.0,30.7,1246822400,4058759168,58.2,13868937216,25130254336,215,9764.39,125.25
2026-01-31 17:24:30,1.6,30.7,1246822400,4058759168,58.2,13868937216,25130254336,215,9768.39,129.25

## Notes
- CSV file updates periodically with timestamps.
- Confirms system metrics logger is running correctly.
