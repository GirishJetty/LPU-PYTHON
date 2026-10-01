total_tracked_time = float(input("Enter total tracked time in minutes: "))
valid_days = int(input("Enter number of valid recorded days: "))

TUI = total_tracked_time / valid_days

print("\nTime Utilization Index (TUI):", round(TUI, 2), "min/day")