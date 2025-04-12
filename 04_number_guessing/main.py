import random

secret = random.randint(1, 20)
attempts_left = 5

while attempts_left > 0:
    try:
        guess = int(input("Guess a number between 1 and 20: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess == secret:
        print("Correct! You win!")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")

    attempts_left -= 1

    if attempts_left:
        print(f'{attempts_left} tries left')
    else:
        print(f"You lose! The number was {secret}")
