#c_calc.py 
"""
title: Simple Calculator 
author: Michelle Jiang 
date-created: 2022-09-09
"""

"""
Notes: 
Follow IPO format with Inputs, Processing, Outputs as headers 
Using nested conditional statements 
Use while to repeat process
"""

# Input # 
from sre_constants import REPEAT


REPEATPROCESS = 1 
RESULT = 0 
while REPEATPROCESS == 1: 
    NUMBERONE = int(input("Please enter the first number: "))
    OPERATION = input("Please enter the operation you would like to use (+, -, *, /): ")
    NUMBERTWO = int(input("Please enter the second number: "))

# Processing # 
    if OPERATION == "+": 
        RESULT = NUMBERONE + NUMBERTWO
    elif OPERATION == "*": 
        RESULT = NUMBERONE * NUMBERTWO
    elif OPERATION == "/": 
        RESULT = NUMBERONE / NUMBERTWO
    elif OPERATION == "-": 
        RESULT = NUMBERONE - NUMBERTWO

# Output # 
    print("The answer to", NUMBERONE, OPERATION, NUMBERTWO, "is:", RESULT, ". ")

# Input # 
    NEWCALCULATION = input("Would you like to make another calculation? (Y/N): ")

#Processing # 
    if NEWCALCULATION == "Y": 
        REPEATPROCESS = 1
    elif NEWCALCULATION == "N": 
        REPEATPROCESS = 0