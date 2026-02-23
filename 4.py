# Age Calculator

current_year = 2026
birth_year = int(input("Enter your birth year: "))

age = current_year - birth_year

print("Current age:", age)
print("Age in months:", age * 12)
print("Age in days:", age * 365)
print("Age in hours:", age * 365 * 24)
print("Age in minutes:", age * 365 * 24 * 60)
print("Years until 100:", 100 - age)