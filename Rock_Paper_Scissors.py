import random

def play():
    user = input("What is your Choice? if rock write 'r', if paper write 'p', if scissor write 's'\n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return "The game is tie"
    
    if is_win(user,computer):
        return "You are win"
    
    return "You are loser"

def is_win(player,opponent):
    if(player=='r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='p' and opponent=='r'):
        return True

print(play())