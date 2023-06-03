# Guessing game. Here you can guess a number from computer

import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess!=random_number:
        guess = int(input(f"Enter a number between 1 to {x}: "))
        if guess<random_number:
            print("Sorry,guess again, your guessing number is too low")
        elif guess>random_number:
            print("Sorry,guess again, your guessing number is too high")
    print(f"Nice,you guess the number correctly! because the random number is {random_number}")

guess(10)