# i_rock_paper_scissors.py

"""
title: Rock Paper Scissors
author: Michelle Jiang
date-created: 2022-09-22
"""

from random import randint
import sys

### SUBROUTINES ###
# Inputs # 
def checkInt(VALUE): 
    """Validate whether a string is an integer 
    :param VALUE: string 
    :return: int 
    """
    if VALUE.isnumeric(): 
        VALUE = int(VALUE) 
        return VALUE
    else: 
        print("Please enter a valid number! ")
        NEW_NUM = input("> ")
        return checkInt(NEW_NUM)

def menu():
    """
    displays user selection and user chooses their weapon 
    :return: int 
    """
    print("""Welcome to Rock Paper Scissors! Please choose your weapon wisely! 
1. Rock
2. Paper
3. Scissors
4. Bomb""")
    WEAPON = input("> ")
    WEAPON = checkInt(WEAPON)
    if WEAPON > 0 and WEAPON < 5: 
        return WEAPON
    else: 
        print("Please enter an integer between 1 and 5! ")
        return menu()

def playAgain():
    """
    asks the user if they want to play again 
    :return: boolean
    """
    CHOICE = input("Would you like to play again? (Y/n): ")
    if CHOICE == "n" or CHOICE == "N": 
        return False
    else: 
        return True

# Processing # 
def computerChoice():
    """
    The computer chooses a weapon! 
    :return: int 
    """
    WEAPON = randint(1, 4)
    return WEAPON

def determineWinner(PLAYER, COMPUTER): 
    """
    determines the winner of this round! 
    :param PLAYER: int - player's choice
    :param COMPUTER: int - computer's choice
    :return: int - winner of the round (0: tie, 1: player, 2: computer, 3+: everyone dies)
    """
    if PLAYER == COMPUTER: 
        return 0 
    elif COMPUTER == PLAYER + 1 or COMPUTER == 1 and PLAYER == 3: 
        return 2 
    elif COMPUTER == 4:
        return 3
    elif PLAYER == 4: 
        return 4
    else: 
        return 1

# Outputs # 
def displayWinner(WINNER): 
    """
    display the winner of the round 
    :param WINNER: int 
    :return: None"""
    if WINNER == 0: 
        print("It's a tie! ")
    elif WINNER == 1: 
        print("You won! ")
    elif WINNER == 2: 
        print("You lost! ")
    elif WINNER == 3: 
        print("The computer detonated a bomb. Everyone has died. ")
        sys.exit()
    elif WINNER == 4: 
        print("Why would you do that? Everyone has died! ")
        sys.exit()
    
### MAIN PROGRAM CODE ### 
if __name__ == "__main__":
    while True:
        # Inputs # 
        PLAYER = menu() 
        COMPUTER = computerChoice() 
        # Processing # 
        WINNER = determineWinner(PLAYER, COMPUTER)
        # Outputs #
        displayWinner(WINNER)
        if not playAgain():
            sys.exit()