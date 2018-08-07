import logic

print("Welcome to the ******* ROCK PAPER SCISSOR GAME *********")

while(1):
    u = input("Select \'R\' for Rock, \'P\' for Paper, and \'S\' for Scissor:")
    if (u=='r' or u=='R'):
        user = 'rock'
        logic.play(user);
    elif (u=='p' or u=='P'):
        user = 'paper'
        logic.play(user);
    elif (u=='s' or u=='S'):
        user = 'scissor'
        logic.play(user);
    else:
        print("Wrong input")
