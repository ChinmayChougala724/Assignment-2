# ATM Simulation

balance = 10000   # Initial balance

while True:
    print("\n===== ATM SIMULATOR =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    # Check Balance
    if choice == 1:
        print("Current Balance: ₹", balance)

    # Deposit Money
    elif choice == 2:
        amount = float(input("Enter amount to deposit: ₹"))
        if amount > 0:
            balance = balance + amount
            print("Deposit successful!")
            print("New balance: ₹", balance)
        else:
            print("Invalid amount!")

    # Withdraw Money
    elif choice == 3:
        amount = float(input("Enter amount to withdraw: ₹"))

        if amount > balance:
            print("Insufficient balance!")
        elif balance - amount < 500:
            print("Minimum balance of ₹500 must be maintained!")
        else:
            balance = balance - amount
            print("Withdrawal successful!")
            print("New balance: ₹", balance)

    # Exit
    elif choice == 4:
        print("Thank you for using ATM.")
        break

    else:
        print("Invalid choice! Please select 1-4.")