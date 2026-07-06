# Guess the Number V2
# Created by Rozhin
# My second Python game

import random

print("===== Guess the Number =====")

secret_number = random.randint(1, 10)

count = 0

while True:
    a = int(input("Enter a number (1-10): "))
    count += 1

    if secret_number > a:
        print("Higher!")

    elif secret_number < a:
        print("Lower!")

    else:
        print("Congratulations!")
        print("You guessed it in", count, "tries.")
        break

    if count == 5:
        print("Game Over!")
        print("The secret number was", secret_number)
        break

print("Thanks for playing!")
