# Ticket Pricing System

# Taking inputs
age = int(input("Enter age: "))
day = input("Enter day of week: ")
tickets = int(input("Enter number of tickets: "))

# Age-based pricing
if age < 3:
    price = 0
    category = "Free"
elif age <= 12:
    price = 150
    category = "Child"
elif age <= 59:
    price = 300
    category = "Adult"
else:
    price = 200
    category = "Senior"

# Calculating base price
base_price = price * tickets

# Day-based discount
if day.lower() in ["friday", "saturday", "sunday"]:
    discount = base_price * 0.20
else:
    discount = 0

price_after_discount = base_price - discount

# Displaying output
print("\n=== TICKET BILL ===")
print("Category:", category)
print("Base price: ₹", base_price)
print("Discount: ₹", discount)
print("Price after discount: ₹", price_after_discount)
print("Total amount to pay: ₹", price_after_discount)