# h_calc_2.py

"""
title: Calculator (with added functions!)
author: Michelle Jiang
date-created: 2022-09-20
"""

import math

### SUBROUTINES ###

# Inputs # 
def getNumber1():
    """
    ask user for first number 
    :return: float
    """
    INPUT1 = input("Welcome to your super awesome free calculator! Please input your first number! ")
    INPUT1 = float(INPUT1)
    return INPUT1

def getOperation():
    """ 
    asks user for operation
    :return: string 
    """
    OPERATION = input("What operation would you like to perform? (+, -, *, /, sqrt): ")
    return OPERATION

def getNumber2(): 
    """
    asks user for second number 
    :return: float 
    """
    INPUT2 = input("Kindly input your second number! ")
    INPUT2 = float(INPUT2)
    return INPUT2 

# Processing # 
def addition(NUM1, NUM2):
    """
    add two floating decimal numbers 
    :param NUM1: float
    :param NUM2: float 
    :return: float 
    """
    SUM = NUM1 + NUM2 
    SUM = float(SUM)
    return SUM

def subtraction(NUM1, NUM2):
    """
    subtract two floating decimal numbers 
    :param NUM1: float
    :param NUM2: float 
    :return: float 
    """
    DIFFERENCE = NUM1 - NUM2
    DIFFERENCE = float(DIFFERENCE)
    return DIFFERENCE 

    
def multiplication(NUM1, NUM2):
    """
    multiply two floating decimal numbers 
    :param NUM1: float
    :param NUM2: float 
    :return: float 
    """
    PRODUCT = NUM1 * NUM2 
    PRODUCT = float(PRODUCT)
    return PRODUCT 

def division(NUM1, NUM2):
    """
    add two floating decimal numbers 
    :param NUM1: float
    :param NUM2: float 
    :return: float 
    """
    QUOTIENT = NUM1 / NUM2 
    QUOTIENT = float(QUOTIENT)
    return QUOTIENT

def sqrt(NUM1):
    """
    select a command from the math library and use it here (aka square root)
    :param NUM1: 
    :return:
    """
    SQRT = math.sqrt(NUM1)
    SQRT = float(SQRT)
    return SQRT

def calculateAnswer(NUM1, NUM2, OPERATION):
    """
    takes the inputted numbers and operation and returns the result
    :param NUM1: float
    :param NUM2: float
    :param OPERATION: string
    :return: float
    """
    if OPERATION == "+":
        RESULT = addition(NUM1, NUM2) 
    elif OPERATION == "-":
        RESULT = subtraction(NUM1, NUM2)
    elif OPERATION == "*":
        RESULT = multiplication(NUM1, NUM2)
    elif OPERATION == "/":
        RESULT = division(NUM1, NUM2)
    elif OPERATION == "sqrt":
        RESULT = sqrt(NUM1)
    return RESULT

# Outputs # 
def displayAnswer(RESULT):
    """
    displays the result
    :param RESULT: float
    :return: string
    """
    print(f"Your answer is {RESULT}! This has been your super awesome free calculator! ")

### MAIN PROGRAM CODE ### 
if __name__ == "__main__":
    # Inputs # 
    NUM1 = getNumber1()
    OPERATION = getOperation()
    if not OPERATION == "sqrt":
        NUM2 = getNumber2()

    # Processing # 
        RESULT = calculateAnswer(NUM1, NUM2, OPERATION)
    else: 
        RESULT = calculateAnswer(NUM1, 0, OPERATION)
        
    # Outputs # 
    displayAnswer(RESULT)