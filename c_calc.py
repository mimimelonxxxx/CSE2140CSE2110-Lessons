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
repeatProcess = 1 
result = 0 
while repeatProcess == 1: 
    numberOne = int(input("Please enter the first number: "))
    operation = input("Please enter the operation you would like to use (+, -, *, /): ")
    numberTwo = int(input("Please enter the second number: "))

# Processing # 
    if operation == "+": 
        result = numberOne + numberTwo
    elif operation == "*": 
        result = numberOne * numberTwo
    elif operation == "/": 
        result = numberOne / numberTwo
    elif operation == "-": 
        result = numberOne - numberTwo

# Output # 
    print("The answer to", numberOne, operation, numberTwo, "is:", result, ". ")

# Input # 
    newCalculation = input("Would you like to make another calculation? (Y/N): ")

#Processing # 
    if newCalculation == "Y": 
        repeatProcess = 1
    elif newCalculation == "N": 
        repeatProcess = 0