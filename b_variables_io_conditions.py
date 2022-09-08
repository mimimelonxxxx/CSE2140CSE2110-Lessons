#b_variables_io_conditions.py

"""
title: CS10 Concept Review and Language Translation
author: Michelle Jiang
date-created: 2022-09-08
"""

### VARIABLES ###

STRING = '7' #double quotations are also permissible
INTEGER = 7
FLOAT = 7.0

print(STRING)
print(INTEGER)
print(FLOAT)
print(type(STRING))
print(type(INTEGER))
print(type(FLOAT))

## Typecasting ## 

# The process of converting from one data type to another. 

NUMBER = "14" #string 
INT_NUMBER = int(NUMBER)
FLOAT_NUMBER = float(NUMBER)
STR_NUMBER = str(NUMBER)

print(type(INT_NUMBER), type(FLOAT_NUMBER), type(STR_NUMBER))

### INPUTS ###

#Inputs allows user to enter text data into the program. 

USER_IN = input("Enter a number: ")
# print(int(USER_IN))
#print(type(USER_IN))
USER_IN = int(USER_IN)
## NOTE: All characters from input() are strings. 

### CONDITIONAL STATEMENTS ### 

if USER_IN > 10:
    print("Woah, that is a high number! ")
else: 
    print("I can count those on my fingers! ")
