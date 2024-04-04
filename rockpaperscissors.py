import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playagain = True

while playagain:
    playerchoice = input(
        "\nEnter ... \n1  for Rock, \n2 for Paper, or \n3 for Scissors"
    )
    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit("you must enter 1,2, or 3.")

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("\nyou chose " + playerchoice + ".")
    print("Python chose " + computerchoice + ".\n")

    if player == 1 and computer == 3:
        print("you win")
    elif player == 2 and computer == 1:
        print("you win")
    elif player == 3 and computer == 2:
        print("you win")
    elif player == computer:
        print("tie game")
    else:
        print("python wins")

    playagain = input("\nPlay again? \nY for Yes or \nQ to Quit \n\n")

    if  playagain.lower() == "y":
        continue
    else:
        print("Thanks")
        playagain  = False
        #or use break