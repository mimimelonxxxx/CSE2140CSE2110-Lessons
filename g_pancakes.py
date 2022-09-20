# g_pancakes.py 

"""
title: Making Pancakes
author: Michelle Jiang
date-created: 2022-09-19
"""

### SUBROUTINES ### 

# Inputs # 
# Functional inputs have no parameters but a return value
from ast import Return
from inspect import getmembers


def getFlour(): 
    """
    Ask user for amount of flour (cups) 
    :return: float 
    """
    FLOUR = input("How many cups of flour do you have? ")
    FLOUR = float(FLOUR)
    return FLOUR

def getEggs(): 
    """
    Ask user for amount of eggs 
    :return: integer
    """
    EGGS = input("How many eggs do you have? ")
    EGGS = int(EGGS)
    return EGGS
def getMilk(): 
    """
    Ask user for amount of milk (cups) 
    :return: float 
    """
    MILK = input("How much many cups of milk do you have? ")
    MILK = float(MILK)
    return MILK

# Processing # 
# Has parameters and return values 
def makePancakes(FLOUR, MILK, EGGS): 
    """
    Check that there are enough ingredients and then return the number of servings 
    :param FLOUR: float
    :param MILK: float
    :param EGGS: int
    :return: int - Number of servings
    """

    if FLOUR >= 1.5 and MILK >= 1.0 and EGGS >= 2: 
        FLOUR_SERVINGS = FLOUR // 1.5 
        MILK_SERVINGS = MILK // 1 # int(MILK) 
        EGGS_SERVINGS = EGGS // 2

        SERVINGS = FLOUR_SERVINGS # Assuming FLOUR_SERVINGS is limiting
        if MILK_SERVINGS < SERVINGS: 
            SERVINGS = MILK_SERVINGS
        if EGGS_SERVINGS < SERVINGS: 
            SERVINGS = EGGS_SERVINGS
        SERVINGS = int(SERVINGS)
        return SERVINGS
    return 0 

# Outputs # 
# Have parameters and no return values 
def displayPancakes(DOZEN):
    """
    display number of pancakes to user, and then display by the dozen
    :param DOZEN: int
    :return: NONE
    """
    if DOZEN == 0: 
        print("You do not have enough ingredients to make yummy pancakes!")
    else: 
        PANCAKES = 12 * DOZEN
        print(f"You can make {PANCAKES} pancakes! This is {DOZEN} dozen pancakes! ")

### MAIN PROGRAM CODE ### 

if __name__ == "__main__": 
    # Inputs # 
    FLOUR_G = getFlour()
    EGGS_G = getEggs()
    MILK_G = getMilk()

    # Processing # 
    SERVINGS_G = makePancakes(FLOUR_G, MILK_G, EGGS_G)

    # Outputs # 
    displayPancakes(SERVINGS_G)