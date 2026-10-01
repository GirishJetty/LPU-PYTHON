Bwa_Study_Time = float(input("Enter total study time in minutes: "))
Valid_Class_Time = float(input("Enter total class time in minutes: "))
Total_Days = int(input("Enter number of valid recorded days: "))

AAI = (Bwa_Study_Time + Valid_Class_Time) / Total_Days

print("\nAcademic Activity Index (AAI):", round(AAI, 2), "min/day")