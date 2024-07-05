#Beggar Thy Neighbor written by Adam Miller on 7/5/24.
#This program simulates the card game "Beggar Thy Neighbor" where the computer plays against virtual players.

#Random import for shuffling the deck
import random

#Time import for slowing the card game down
import time

#GUI imports
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

#Create window for Graphical User Interface (GUI). 
#Add radio buttons to select the number of players. 
#Create "Start" and "Exit" buttons to manage the program. 
#The card game should begin when a player number has been selected, and the "Start" button is pressed. 
#Finally, a text area should display what is going on during the card game, and a label should be in place with the title of the card game. 
#Output is split between the console and GUI because attempting to push all output into GUI takes too much memory and crashes the program.

window = Tk()
window.title("Beggar Thy Neighbor")
window.geometry("570x350")

def enableStartButton():
  startButton=Button(window, text="Start ", bg="green", fg="white", command=startButtonClicked, state="active")
  startButton.grid(column=2, row=2)

def endProgram():
  print("\nThank you for playing!")
  time.sleep(3)
  exit()


infoLbl =Label(window, text="Welcome to Beggar Thy Neighbor!", font=("Times New Roman", 15))
infoLbl.grid(column = 1, row = 0)

gameTextArea=scrolledtext.ScrolledText(window, width=50, height=10)
gameTextArea.grid(column = 1, row = 1)

endButton=Button(window, text="Exit ", bg="red", fg="white", command=endProgram, state="active")
endButton.grid(column=2, row=3)

gameTextArea.insert(INSERT, "How many players are there?")

playerButtonGroup = StringVar()

players2=ttk.Radiobutton(window, text="Two Players", variable=playerButtonGroup, value=2, command=enableStartButton)
players3=ttk.Radiobutton(window, text="Three Players", variable=playerButtonGroup, value=3, command=enableStartButton)
players4=ttk.Radiobutton(window, text="Four Players", variable=playerButtonGroup, value=4, command=enableStartButton)

players2.grid(column=1, row=2)
players3.grid(column=1, row=3)
players4.grid(column=1, row=4)


window.mainloop()
