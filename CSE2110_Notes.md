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
    y = 4*x + 5 
    return y

print(myFunction(4))
# displays 21 
```