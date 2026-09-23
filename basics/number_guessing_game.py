import random

secret_number = random.randint(1, 10)
guess = 0
attempts = 0

print("Guess the secret number between 1 and 10!")

while guess != secret_number:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low. Try again.")
    elif guess > secret_number:
        print("Too high. Try again.")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")