# Sum and Average Calculator

count = int(input("How many numbers? "))

total = 0

# Taking first number separately to set max and min
num = float(input("Enter number 1: "))
total = total + num
maximum = num
minimum = num

# Taking remaining numbers
for i in range(2, count + 1):
    num = float(input("Enter number " + str(i) + ": "))
    total = total + num

    if num > maximum:
        maximum = num

    if num < minimum:
        minimum = num

average = total / count

print("\nSum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)