# Leap Year Checker

year = int(input("Enter a year: "))

# Checking leap year condition
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a Leap Year")
            print("Reason: Divisible by 4, divisible by 100 and also divisible by 400.")
        else:
            print(year, "is NOT a Leap Year")
            print("Reason: Divisible by 100 but NOT divisible by 400.")
    else:
        print(year, "is a Leap Year")
        print("Reason: Divisible by 4 but NOT divisible by 100.")
else:
    print(year, "is NOT a Leap Year")
    print("Reason: Not divisible by 4.")