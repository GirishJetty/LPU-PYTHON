Bwa_Expected_Days = int(input("Enter expected number of days: "))
Valid_Days = int(input("Enter valid recorded days: "))

DCI = (Valid_Days / Bwa_Expected_Days) * 100

print("\nData Continuity Index (DCI):", round(DCI, 2), "%")