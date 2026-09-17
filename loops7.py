secret_number = 7
attempts = 0

while True:
    guess = int(input("Guess the number: "))
    attempts += 1

    if guess < secret_number:
        print("Too low!")

    elif guess > secret_number:
        print("Too high!")

    else:
        print("Correct! You guessed it.")
        print("Attempts:", attempts)
        break