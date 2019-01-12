import tkinter as tk
from PIL import ImageTk, Image
from random import *
import webbrowser

user = "none"
comp = "none"

def rand():
    c = (randint(1,3))
    if (c == 1):
        comp = "rock"
        imgComp = ImageTk.PhotoImage(Image.open("images/rock.png"))
        panelComp.configure(image=imgComp)
        panelComp.image = imgComp
        choiceComp.config(text="Computer:\nROCK")
        return comp
    elif (c == 2):
        comp = "paper"
        imgComp = ImageTk.PhotoImage(Image.open("images/paper.png"))
        panelComp.configure(image=imgComp)
        panelComp.image = imgComp
        choiceComp.config(text="Computer:\nPAPER")
        return comp
    else:
        comp = "scissor"
        imgComp = ImageTk.PhotoImage(Image.open("images/scissor.png"))
        panelComp.configure(image=imgComp)
        panelComp.image = imgComp
        choiceComp.config(text="Computer:\nSCISSOR")
        return comp

def play(user,comp):
    if (user == 'rock'):
        if (comp == 'rock'):
            result.config(text="DRAW")
            choiceUser.config(bg="yellow")
            choiceComp.config(bg="yellow")
        elif (comp == 'paper'):
            result.config(text="Computer Wins :|")
            choiceUser.config(bg="red")
            choiceComp.config(bg="green")
        else:
            result.config(text="User Wins !!!")
            choiceUser.config(bg="green")
            choiceComp.config(bg="red")
    elif (user == 'paper'):
        if (comp == 'rock'):
            result.config(text="User Wins !!!)")
            choiceUser.config(bg="green")
            choiceComp.config(bg="red")
        elif (comp == 'paper'):
            result.config(text="DRAW")
            choiceUser.config(bg="yellow")
            choiceComp.config(bg="yellow")
        else:
            result.config(text="Computer Wins :|")
            choiceUser.config(bg="red")
            choiceComp.config(bg="green")
    else:
        if (comp == 'rock'):
            result.config(text="Computer Wins :|")
            choiceUser.config(bg="red")
            choiceComp.config(bg="green")
        elif (comp == 'paper'):
            result.config(text="User Wins !!!")
            choiceUser.config(bg="green")
            choiceComp.config(bg="red")
        else:
            result.config(text="DRAW")
            choiceUser.config(bg="yellow")
            choiceComp.config(bg="yellow")

def selectRock():
    user = "rock"
    imgUser = ImageTk.PhotoImage(Image.open("images/rock.png"))
    panelUser.configure(image=imgUser)
    panelUser.image = imgUser
    choiceUser.config(text="User:\nROCK")
    comp = rand()
    play(user,comp)

def selectPaper():
    user = "paper"
    imgUser = ImageTk.PhotoImage(Image.open("images/paper.png"))
    panelUser.configure(image=imgUser)
    panelUser.image = imgUser
    choiceUser.config(text="User:\nPAPER")
    comp = rand()
    play(user,comp)

def selectScissor():
    user = "scissor"
    imgUser = ImageTk.PhotoImage(Image.open("images/scissor.png"))
    panelUser.configure(image=imgUser)
    panelUser.image = imgUser
    choiceUser.config(text="User:\nSCISSOR")
    comp = rand()
    play(user,comp)

def openLink(event):
    webbrowser.open_new("https://github.com/likarajo")

root = tk.Tk()
root.title("Rock-Paper-Scissor GAME")

tk.Label(root, text="Welcome to the **** ROCK PAPER SCISSOR GAME ****", bg="blue", fg="white").pack(fill=tk.X)

link = tk.Label(root, text="likarajo", font= "Verdana 10 underline", fg="blue", cursor="hand2")
link.pack(fill=tk.X)
link.bind("<Button-1>", openLink)

tk.Label(root, text="Click on your choice").pack(fill=tk.X)

tk.Button(root, text="ROCK", bg="white", fg="black", command=selectRock).pack(fill=tk.X, padx=200)
tk.Button(root, text="PAPER", bg="white", fg="black", command=selectPaper).pack(fill=tk.X, padx=200)
tk.Button(root, text="SCISSOR", bg="white", fg="black", command=selectScissor).pack(fill=tk.X, padx=200)

result = tk.Label(root, text="--Result--", bg="purple", fg="yellow")
result.pack(fill=tk.X, padx=50, pady=10)

choiceUser = tk.Label(root, text="User's\nChoice", bg="white", width=20)
choiceUser.pack(side=tk.LEFT)

imgUser = ImageTk.PhotoImage(Image.open("images/user.png"))
panelUser = tk.Label(root, image = imgUser)
panelUser.image = imgUser
panelUser.pack(side=tk.LEFT)

imgComp = ImageTk.PhotoImage(Image.open("images/computer.png"))
panelComp = tk.Label(root, image = imgComp)
panelComp.image = imgComp
panelComp.pack(side=tk.LEFT)

choiceComp = tk.Label(root, text="Computer's\nChoice", bg="white", width=20)
choiceComp.pack(side=tk.LEFT)

root.mainloop()
