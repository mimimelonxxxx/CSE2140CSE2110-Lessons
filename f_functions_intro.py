# f_functions_intro.py

"""
title: Variables and Functions
author: Michelle Jiang 
date-created: 2022-09-16
"""

# VARIABLES # 

### Procedural Subroutines ### 
print("Procedural Subroutines with Local and Global Variables")
print("Example 1:")
VAR = "hello world - global variable" # global variable 
print(VAR)

print("Example 2:")
def hello2():
    VAR = "hello world 2 - local variable" # local variable
    print(VAR)

hello2()
print(VAR) # prints the global variable

print("Example 3:")
def hello3(): 
    global VAR # brings the global variable into the subroutine 
    VAR = "hello world 3 - global updated in a subroutine"
    print(VAR)

hello3()
print(VAR)

### Functions ###
print("Example 4:")
def hello4(VAR):
    print(VAR) # don't need to type return unless you need to return a value 

hello4("hello world 4 - argument inputted into a function parameter")
print(VAR)

print("Example 5:")

def hello5(VAR): 
    print(VAR)
    return VAR 

hello5("hello world 5") # hello world 5 is returned to the main program code 
print(VAR)

VAR = hello5("hello world 5 - update global with function return")
print(VAR)

print("Example 6:")
def mathEquation(NUMBER): # parameter
    # note: variables store data, functions transform data
    RESULT = 4 * NUMBER + 5 # local, local
    return RESULT # local

VALUE = 8 # global variable
ANSWER = mathEquation(VALUE) # ANSWER: global, VALUE: argument
print(ANSWER) # global
# output 37 

