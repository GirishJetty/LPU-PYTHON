Bwa_Workout_Time = float(input("Enter total fitness time in minutes: "))
Valid_Days = int(input("Enter number of valid recorded days: "))

PhAI = Bwa_Workout_Time / Valid_Days

print("\nPhysical Activity Index (PhAI):", round(PhAI, 2), "min/day")