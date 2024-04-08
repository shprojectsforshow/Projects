import math
import sys
import random
from random import choice
from rockpaperscissors import rock_paper_scissors

capital = "Topeka"

bird = "Western Meadowlark"

flower = "Sunflower"

song = "Home on the Range"

def randomfunfact():
    funfacts=[
        "Kansas isnt Oklahoma", "Kansas City is in Missouri too", "Wizard of Oz is boring reference", "Rock Chalk Jayhawks"
    ]

    index = choice("0123")

    print(funfacts[int(index)])
    

rock_paper_scissors()