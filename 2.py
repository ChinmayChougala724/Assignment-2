# Simple Calculator

# taking two numbers 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Results:")

# addition
print(a, "+", b, "=", a + b)

# subtraction
print(a, "-", b, "=", a - b)

# multiplication
print(a, "*", b, "=", a * b)

# division
print(a, "/", b, "=", round(a / b, 2))

# modulus
print(a, "%", b, "=", a % b)

# exponentiation
print(a, "^", b, "=", a ** b)