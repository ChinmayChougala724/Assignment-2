# Factorial Calculator

num = int(input("Enter a number: "))

# Handling negative numbers
if num < 0:
    print("Factorial is not defined for negative numbers.")

# Handling 0
elif num == 0:
    print("0! = 1")

else:
    factorial = 1
    expression = ""

    # Calculating factorial using loop
    for i in range(num, 0, -1):
        factorial = factorial * i
        expression = expression + str(i)

        if i != 1:
            expression = expression + " × "

    print(str(num) + "! =", expression, "=", factorial)