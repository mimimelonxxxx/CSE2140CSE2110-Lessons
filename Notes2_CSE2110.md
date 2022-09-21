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

4. **Collaboration**: because local variables do not affect the rest of the main program, multiple developers can be creating different functions and do not need to match variable names or data structures. 

## Returning Multiple Values from a Function 

A function can have multiple return values. In order to restore multiple return values, separate variables or a more complex data structure must be used. 

```python 
def myFunction(): 
    return VALUE1, VALUE2 

VARIABLE1, VARIABLE2 = myFunction() 
VARIABLE3 = myFunction() # stores as a tuple data structure 
```
## Docstrings 

Docstrings are the internal documentation of a function. They are used by functions to describe the data that is being inputted and outputted from a function. (Docstrings improve the readability of the program and is a part of *internal documentation*).

```python 
def ageCaclulator(CURRENTYEAR, BIRTHYEAR):
    """
    Calculates the age the user turns into in a given year
    :param CURRENTYEAR: int
    :param BITHYEAR: int
    :return: int
    """
    # docstrings count as pass 
```

## Recursive Functions (IB)

Recursive functions are functions that return to the same function. This return value will only happen in certain instances and there is **always** a return value that is not the function. These functions loop on themselves because they return back to the function. 

```python
def checkInt(NUM): 
    if NUM.isnumeric() == True: 
        return int(NUM)
    else: 
        print("Please enter a valid number!")
        NEWNUM = input("Number: ")
        return checkInt(NEWNUM) # recursive statement 
```

You can theoretically call other functions within the function, but using this technique has many drawbacks, such as reducing readability, introducing complexity, and not following IPO format. 

## Default Parameters 

A function can have default arguments in the event that no arguments are passed into the funciton. Default parameters are often optional and usually placed at the end of the functions parameters in descending order of importance. 

```python
def myFun(PARAM1=True):
    return PARAM1 
print(myFun()) # prints True
print(myFun(False)) # prints False
print(myFun(True)) # prints True
```

Note that the function cannot skip default parameters. If there is a parameter lower in the list of parameters, all default parameters must havea rguments to reach the desired paramter. `def myFun(PARAM1, PARAM2=0, PARAM3=0)` :arrow_right: PARAM3 cannot be called without calling PARAM1 AND PARAM2. 

## Using Multiple Files

Subroutines can be stored in separate files to orgamize functions and improve collaboration. Eg: if you make a program to manage sales at a coffee shop, functions can be organized into payments, transactions and reports. Each of these categories can be in a separate file imported into the main file. In this scenario, edvelopers can then work on separate features of the program without distrupting other developers. 

In order to link mulitple files together, python uses `inport` statement. Files must be in the same folder (or a subfolder) of the main program file. 

The file name of the secondary files must follow variable naming conventions including being alphanumeric but not starting with a number, and only using hypens and underscores as special characters. 

### The \_\_name__ magic variable

When Python runs a file, it associates the "\_\_main__" value to the \_\_name__ magic variable for the file that runs. All other fies imported to the running program uses their file name as the \_\_name__ magic variable. **Magic variables** are predetermined variables in the backend of the programming language that helps the program run. Oftentimes programmers do not need to modify these values in the program. Magic variables are indicated by two underscores before and after the text. They are sometimes called "double underscore variables" or "dunder variables." (NEVER use the name dunder variables.) Since python automatically updates the \_\_name__ magic variable, a check can be included to ensure that code runs only if the given file is run, and not an imported file. This cheeck allows subroutines and functions to be tested in their respective files withiout being inpored into the main program. 

```python
def someFunction(PARAM1):
    VALUE = {some code}
    return VALUE

if __name__ == "__main__":
    # This section will only run if the file is run, not imported
    print(someFunction(VAR1))
```
