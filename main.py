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

#Function that manages what happens during the card game when a player draws a Jack.
def jack(playerNumber, numberOfPlayers):
  playerNumber = playerNumber + 1
  t = 1
  while t > 0:
    if playerNumber > numberOfPlayers:
      playerNumber = 1
      continue
    elif playerNumber == 1:
      hand = playerHand1
    elif playerNumber == 2:
      hand = playerHand2
    elif playerNumber == 3:
      hand = playerHand3
    else:
      hand = playerHand4
    
    if len(hand) == 0:
      break
    discardPile.append(hand[0])
    hand.pop(0)

    if discardPile[len(discardPile)-1] == 11:
      print("Player "+str(playerNumber)+" played a "+faceCards[11])
      #time.sleep(0.5) <-Messes with GUI text area inserts!
      jack(playerNumber, numberOfPlayers)
      break

    elif discardPile[len(discardPile)-1] == 12:
      print("Player "+str(playerNumber)+" played a "+faceCards[12])
      #time.sleep(0.5)
      queen(playerNumber, numberOfPlayers)
      break


    elif discardPile[len(discardPile)-1] == 13:
      print("Player "+str(playerNumber)+" played a "+faceCards[13])
      #time.sleep(0.5)
      king(playerNumber, numberOfPlayers)
      break

    elif discardPile[len(discardPile)-1] == 14:
      print("Player "+str(playerNumber)+" played an "+faceCards[14])
      #time.sleep(0.5)
      ace(playerNumber, numberOfPlayers)
      break

    else:
      print("Player "+str(playerNumber)+" played a(n) "+str(discardPile[len(discardPile)-1]))
      #time.sleep(0.5)
      t = t - 1
      if t == 0:
        playerNumber = playerNumber - 1
        pick_up_discard_pile(playerNumber, numberOfPlayers)

#Function that manages what happens during the card game when a player draws a Queen.
def queen(playerNumber, numberOfPlayers):
  playerNumber = playerNumber + 1
  t = 2
  while t > 0:
    if playerNumber > numberOfPlayers:
      playerNumber = 1
      continue
    elif playerNumber == 1:
      hand = playerHand1
    elif playerNumber == 2:
      hand = playerHand2
    elif playerNumber == 3:
      hand = playerHand3
    else:
      hand = playerHand4

    if len(hand) == 0:
      break
    discardPile.append(hand[0])
    hand.pop(0)

    if discardPile[len(discardPile)-1] == 11:
      print("Player "+str(playerNumber)+" played a "+faceCards[11])
      #time.sleep(0.5)
      jack(playerNumber, numberOfPlayers)
      break

    elif discardPile[len(discardPile)-1] == 12:
      print("Player "+str(playerNumber)+" played a "+faceCards[12])
      #time.sleep(0.5)
      queen(playerNumber, numberOfPlayers)
      break


    elif discardPile[len(discardPile)-1] == 13:
      print("Player "+str(playerNumber)+" played a "+faceCards[13])
      #time.sleep(0.5)
      king(playerNumber, numberOfPlayers)
      break

    elif discardPile[len(discardPile)-1] == 14:
      print("Player "+str(playerNumber)+" played an "+faceCards[14])
      #time.sleep(0.5)
      ace(playerNumber, numberOfPlayers)
      break

    else:
      print("Player "+str(playerNumber)+" played a(n) "+str(discardPile[len(discardPile)-1]))
      #time.sleep(0.5)
      t = t - 1
      if t == 0:
        playerNumber = playerNumber - 1
        pick_up_discard_pile(playerNumber, numberOfPlayers)
     

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
