"""
Fun text game made by me, Braeden
Nov 3 2021
"""
# TODO:
# rules/about

from Stage1 import *
from Stage2 import *
# IMPORT STATEMENTS
from textGameFunctions import *

# Variable Declarations
# Initial health set to 5
currentHP = 5
name = "joe"  # testing purposes
# Main
# Run Stage1() which returns your Health Points, set to currentHP, and your name, set to name
currentHP, name = Stage1(currentHP)
print(Color.YELLOW + "Stage 1 Completed" + Color.END)
input("Press enter to continue...")
currentHP, name = Stage2(currentHP, name)
print(Color.YELLOW + "Stage 2 Completed" + Color.END)
input("Press enter to continue...")
