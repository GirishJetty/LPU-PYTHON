Bwa_Development_Time = float(input("Enter Coding Time In Minutes : "))
Coding_Days = int(input("Enter number of valid recorded days: "))

TPI = Bwa_Development_Time / Coding_Days

print("\nTech Productivity Index (TPI):", round(TPI, 2), "min/day")