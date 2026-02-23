# Number Guessing Game

import random

best_score = None   # To store minimum attempts

while True:
    secret = random.randint(1, 100)
    attempts = 7
    used_attempts = 0
    guessed = False

    print("\n===== NUMBER GUESSING GAME =====")
    print("Guess the number between 1 and 100")
    print("You have 7 attempts!")

    while attempts > 0:
        guess = int(input("Enter your guess: "))
        used_attempts += 1
        attempts -= 1

        if guess == secret:
            print("🎉 Congratulations! You guessed correctly.")
            print("Attempts used:", used_attempts)
            guessed = True

            # Update best score
            if best_score is None or used_attempts < best_score:
                best_score = used_attempts
                print("🏆 New Best Score:", best_score)

            break

        elif guess > secret:
            print("Too High!")

        else:
            print("Too Low!")

        # Bonus hint (within 5)
        if abs(guess - secret) <= 5 and guess != secret:
            print("Hint: You are very close!")

        print("Attempts remaining:", attempts)

    if not guessed:
        print("❌ Game Over! The correct number was:", secret)

    # Ask to play again
    again = input("Do you want to play again? (yes/no): ")
    if again.lower() != "yes":
        print("Thank you for playing!")
        break