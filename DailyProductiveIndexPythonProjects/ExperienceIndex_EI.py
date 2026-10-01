RealCalculatedFeelings = float(input("Enter average feeling score (out of 5): "))
RealCalculatedsatisfaction = float(input("Enter average satisfaction score (out of 5): "))
CalculatedEnergy = float(input("Enter average energy score (out of 5): "))

EI = (RealCalculatedFeelings + RealCalculatedsatisfaction + CalculatedEnergy) / 3

print("\nExperience Index (EI):", round(EI, 2), "/ 5")