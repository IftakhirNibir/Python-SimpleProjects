# Guessing game, in this game computer will guessing your number. 
import random

def computer_guess(x):
    low = 1
    high = int(x)
    feedback = ""
    while feedback!='c':
        if low!=high:
            guess = random.randint(low,high)
        else:
            guess = low #it may high because now low == high
        feedback = input(f"Press 'H', if the {guess} is too high or Press 'L' if the number is too low otherwise Press 'C': ").lower()
        if feedback=='h':
            high = guess-1
        elif feedback=='l':
            low = guess+1
    print(f"Nice,you guess my current guessing number = {guess}")

computer_guess(100)

        
