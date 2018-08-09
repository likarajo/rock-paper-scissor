from tkinter import *
from random import *

user = "none"

def play(user):
    c = (randint(1,3))
    if (c == 1):
        comp = 'rock'
        choiceComputer.config(text="Computer:\nROCK")
        imgC = PhotoImage(file='images/rock.png')
        canvas.itemconfig(imgComputer, image=imgC)
    elif (c == 2):
        comp = 'paper'
        choiceComputer.config(text="Computer:\nPAPER")
        imgC = PhotoImage(file='images/paper.png')
        canvas.itemconfig(imgComputer, image=imgC)
    else:
        comp = 'scissor'
        choiceComputer.config(text="Computer:\nSCISSOR")
        imgC = PhotoImage(file='images/scissor.png')
        canvas.itemconfig(imgComputer, image=imgC)

    if (user == 'rock'):
        if (comp == 'rock'):
            result.config(bg="yellow", text="DRAW")
        elif (comp == 'paper'):
            result.config(bg="red", text="Computer WINS")
        else:
            result.config(bg="green", text="User WINS")
    elif (user == 'paper'):
        if (comp == 'rock'):
            result.config(bg="green", text="User WINS")
        elif (comp == 'paper'):
            result.config(bg="yellow", text="DRAW")
        else:
            result.config(bg="red", text="Computer WINS")
    else:
        if (comp == 'rock'):
            result.config(bg="red", text="Computer WINS")
        elif (comp == 'paper'):
            result.config(bg="green", text="User WINS")
        else:
            result.config(bg="yellow", text="DRAW")


def selectRock():
    user = "rock"
    play(user)
    choiceUser.config(text="User:\nROCK")
    imgU1 = PhotoImage(file='images/rock.png')
    root.after(1000, canvas.itemconfig(imgUser, image=imgU1))

def selectPaper():
    user = "paper"
    play(user)
    choiceUser.config(text="User:\nPAPER")
    imgU1 = PhotoImage(file='images/paper.png')
    root.after(1000, canvas.itemconfig(imgUser, image=imgU1))

def selectScissor():
    user = "scissor"
    play(user)
    choiceUser.config(text="User:\nSCISSOR")
    imgU1 = PhotoImage(file='images/scissor.png')
    root.after(1000, canvas.itemconfig(imgUser, image=imgU1))

root = Tk()

Label(root, text="Welcome to the **** ROCK PAPER SCISSOR GAME ****", bg="blue", fg="white").pack(fill=X, pady=10)
Label(root, text="Click on your choice").pack(fill=X)

Button(root, text="ROCK", bg="brown", fg="yellow", command=selectRock).pack(fill=X, padx=200)
Button(root, text="PAPER", bg="white", fg="black", command=selectPaper).pack(fill=X, padx=200)
Button(root, text="SCISSOR", bg="grey", fg="black", command=selectScissor).pack(fill=X, padx=200)

result = Label(root, text="--Result--", bg="white", fg="black")
result.pack(fill=X, padx=50, pady=10)

canvas=Canvas(root, height=400, width=400, bg="white")
choiceUser = Label(root, text="User's\nChoice", bg="white", width=20)
choiceUser.pack(side=LEFT)
choiceComputer = Label(root, text="Computer's\nChoice", bg="white", width=20)
choiceComputer.pack(side=RIGHT)
canvas.pack()

imgU = PhotoImage(file='images/user.png')
imgUser = canvas.create_image(0, 200, anchor=W, image=imgU)
imgC = PhotoImage(file='images/computer.png')
imgComputer = canvas.create_image(200, 200, anchor=W, image=imgC)

root.mainloop()
