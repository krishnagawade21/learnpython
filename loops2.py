import random

secret_number = random.randint(1, 50)
attempts = 5

print("===== NUMBER GUESSING GAME =====")
print("Guess a number between 1 and 50")
print("You have 5 attempts!")

for i in range(1, attempts + 1):

    guess = int(input(f"\nAttempt {i}: Enter your guess: "))

    if guess == secret_number:
        print("🎉 Correct! You won the game!")
        break

    elif guess < secret_number:
        print("Too low! Try a bigger number.")

    else:
        print("Too high! Try a smaller number.")

else:
    print("\n❌ Game Over!")
    print("The correct number was:", secret_number)