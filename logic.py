import random

def play(user):
    c = (random.randint(1,3))
    if (c == 1):
        comp = 'rock'
    elif (c == 2):
        comp = 'paper'
    else:
        comp = 'scissor'

    if (user == 'rock'):
        print('USER: ROCK ')
        if (comp == 'rock'):
            print('COMPUTER: ROCK ')
            print("DRAW")
        elif (comp == 'paper'):
            print('COMPUTER: PAPER ')
            print("COMPUTER WINS")
        else:
            print('COMPUTER: SCISSOR ')
            print("USER WINS")
    elif (user == 'paper'):
        if (comp == 'rock'):
            print('COMPUTER: ROCK ')
            print("USER WINS")
        elif (comp == 'paper'):
            print('COMPUTER: PAPER ')
            print("DRAW")
        else:
            print('COMPUTER: SCISSOR ')
            print("COMPUTER WINS")
    else:
        if (comp == 'rock'):
            print('COMPUTER: ROCK ')
            print("COMPUTER WINS")
        elif (comp == 'paper'):
            print('COMPUTER: PAPER ')
            print("USER WINS")
        else:
            print('COMPUTER: PAPER ')
            print("DRAW")
