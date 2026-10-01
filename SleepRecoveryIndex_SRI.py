Bwa_Sleep_time = float(input("Enter total sleep time in minutes: "))
Valid_Days = int(input("Enter number of valid recorded days: "))

SRI = Bwa_Sleep_time / Valid_Days

print("\nSleep & Recovery Index (SRI):", round(SRI, 2), "min/day")