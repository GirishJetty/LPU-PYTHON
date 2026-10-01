TPI = float(input("Enter TPI: "))
AAI = float(input("Enter AAI: "))
PhAI = float(input("Enter PhAI: "))
SRI = float(input("Enter SRI: "))
TUI = float(input("Enter TUI: "))
EI = float(input("Enter EI: "))
DCI = float(input("Enter DCI: "))
PAI = (
    0.15 * TPI + 0.20 * AAI + 0.15 * PhAI + 0.20 * SRI + 0.15 * TUI + 0.10 * EI + 0.05 * DCI
)
print("\nPersonal Activity Index (PAI):", round(PAI, 2))