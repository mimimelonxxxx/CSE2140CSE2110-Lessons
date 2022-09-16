# CSE 2110 Procedural Programming 1 Notes 

## Procedures and Functions
Subroutines contain two different categories: procedures and functions. Procedures are a series of steps, like folliwng the steps of a recipe or a lab investigation. In contrast, functions take some data as inputs, called _arguments_ and __transforms__ the arguments into new data. That new data can be returned at the end of the function. The **main difference** between procedures and functions is that functions have their own **inputs and outputs**. 

### Example 1 - Math Functions 

Functions in programming are similar to functions in mathematics. There are processes where data is inputted into the function and a new result exits the function. Therefore, and individual function can be considered a sub-program to the program. It will have it's own inputs, outputs, processing, and variables. 

```
f(x) = 4x + 5
```

| INPUTS | PROCESSING | OUTPUTS |
|---|---|---|
| (arguments) | | (returns) |
| 0 | 4(0) + 5 | 5 |
| 1 | 4(1) + 5 | 9 | 
| 2 | 4(2) + 5 | 13 |
| 3 | 4(3) + 5 | 17 | 

```python 
# python version of the above 
def myFunction(x): 
    y = 4 * x + 5 
    return y

print(myFunction(4))
# displays 21 
```

## Structure of a Function 
```python 
def functionName(PARAMETER1, PARAMETER2,...)
"""
    docstring - explains what the function does 
    :param PARAMETER1: data type expected
    :param PARAMETER2: data type expected 
    :return: data type expected to return to the main program
"""
# CODE to transform data 

return VALUE 
```

Creating a function uses the same statement as creating a procedural subroutine: ```def```. However, functions also include parameters within the parenthesis following the function name. 

**Arguments** are the external data (number, string, variable, data structure, etc) values that are inputted into the parameter of the function. These arguments come from the rest of the main program code and stored as a **local variable** with the parameter name. Once the function completes its processing with the input values, it can *return a value* or a series of values back to the main program. The main program will then need to store the returned value in a **global variable** if it is needed further along in the program. Return values can also include a statement that occurs on a single line. For example `return int(VALUE)`. 

*A function must have either an input or an output, it **does not**, in fact, require both.*

```python 
NUMBER1 = 5 # GLOBAL VARIABLE 
def squareNumber(NUM): 
    # NUM and SQUARE_NUM are local variables
    SQUARE_NUM = NUM ** 2 # NUM ^ 2
    return SQUARE_NUM

NUMBER2 = squareNumber(NUMBER1) # GLOBAL VARIABLE 
```

### Variables in a Function 

In programming, there are two different categories of variables: global and local. Global variables are accessed throughout the main protion of non-subroutine code (Main program code). Local variables are accessed within a particular subroutine. Local variables do not exist outside teh subroutine they are used in. 

Subroutines cannot use global variables unless they are called into the subroutine. 

```python 
# using global variables in a function 
NUMBER1 = 7 

def squareNumber(): 
    global NUMBER1 # calls global variabel into the function 
    SQUARE_NUM = NUMBER1 ** 2 
    return SQUARE_NUM
    NUMBER2 = SQUARE_NUM 
```

Note that while calling a global variable is possible, it should be rarely done in a program because it affects modularity of how much we an reuse a function. 

## Advantages of Functional Programming

Functional programming has many advantages over structural (or top-down) programming. 

1. **Repeatability**: once a function is written, it can be used in many different sections of the program without retyping the same lines multiple times. Functions extend into separate program files; whereas procedural subroutines often only work in the file they are written in. 

2. **Modularity**: certain functions can be used and switched out for other functions without breaking the rest of the program. 

3. **Debugging and Testing**: certain functions can be excluded from the main program until it is properly working. 