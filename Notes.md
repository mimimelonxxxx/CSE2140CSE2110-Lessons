# CSE2140 Second Language Programming 1 and CSE2110 Procedural Programming 1

## CSE2140 Notes 

### Version Control Systems 

Version control systems are a category of software tools that helps **record changes** to files by keeping track of modifications done to the file. 

Version control systems provides a framework for *external documentation*, where each commit documents what changes were made from previous versions of code. In addition, it provides documentation, such as README files within the project folder. 

Version control contributes to *change management* as data is not lost when personnel leave the project and new recruits that are hired will have documentation about what has already happened. 

When a project is ready for publishing, the version control system can also package the current project and release it. Release schedules vary depending on the project and organization structures. For example, Microsoft does their updates on Tuesday, and Google does their updates on Wednesday. They can either be time based (eg: Microsoft and Google) or feature-based (eg: videos being released for the core game and downloadable content (DLC) being released afterwards). 

There are many version control systems, such as Git, Subversion, Mercurial, and Microsoft Team Foundation Version Control. We are using Git for the computing science program at Lillian Osborne. Git is the most commonly used system, although there are some that are similar. 

#### Git and Git Repositories 

Git is a version control system (VCS) that tracks changes to source code. Git repositories are the online storage platform for projects versioned using Git. One important thing to note is that Git and Git Repos are not on any exams, however you will submit projects through Git. The curriculum doesn't have anything on Git and Git Repositories or VCS because our curriculum was published in 2009. Even so, learning Git and Git Repos are incredibly useful for working and industry standards. 

Cloning a repository takes a copy of the Git repository and places it onto the local computer. The clone also has all versioning and branches of the repository. With a clone on your computer, you do not need an internet connection to work on the code. To create a new version of the source code on Git, the new changes must be **committed** to Git to save a local of the changes. To synchronize the local changes to the online repository, the local committed version must be **pushed** to the online repository. 

* Note that a user can have multiple local commits of a project before pushing all the changes to the Git repository. 

To synchronize changes from the online repository to a local project, the online changes must be **pulled** to the local computer. 

* Note that it is best practice to pull changes to a local repository before adding additional changes. If a pull is not done first there may be conflicts when trying to synchronize changes afterwards. This practice is required for collaborating within a Git repo. 

There are additional features such as collaboration, restoring previous versions, and branching that are covered in CS30.  

## Change Management (IB)

Change management is the process, tools, and techniques to manage the people side of changes to achieve required business outcomes. 

Changing a system can be difficult for a variety of reasons.

* New personnel will need time to become accustomed to the workflow and styles of the project
* Staff usually need to learn new processes and skills
* New personnel must adjust to the culture of the new environments (People need to feel welcome so that they can stay for a long time)
* Staff set in their ways may find adjusting difficult (revolt!)
* Efficiency of the entire team will decrease as they lack experience with certain software and workloads
* There may be downtime between system changeovers
  * Transferring data between systems is complex
  * Data may be lost during the transfer
* Transitioning to new systems requires purchasing new (expensive!) equipment and time for users to adjust
* New systems may omit useful features from the old system 

## Computing Science 10 Review 

### Variables 

Variables are a tool to store data and call data at a later part of the program. When naming variables, there are different formats such as camelCase, snake_case, kebab-case, PascalCase (Capitalized), lowercase, UPPERCASE. (For IB, UPPERCASE is used for **all** variable names.) camelCase is used for function and method names, lowercase is used for local variables, UPPERCASE is used for global variables. 

When naming variables
1. The name of the variables can only have alphanumeric characters, underscores(_), or hyphens(-) 
2. Variable names must be unique (case sensitive)
3. It should be descriptive about the data it stores (so you can remember it)
4. Can't start with a number
5. Variable names should not (with exceptions) overwrite built in commands 

### Permitted Data Types

Data is stored in various types so that the programs can interact with them based on their data type.

1. *Integers* - stores non-decimal numbers 
2. *Boolean* - stores a True or False (in some languages, a 1 or 0)
3. *Float(ing Point Number)* - stores a decimal number (called "a double" in Java and other C-based languages)
4. *Char* - stores a single ascii character
5. *String* - stores a string of characters (words)

### Mathematical Operators 

All programming languages include basic arithmetic. Common calculations include addition (+), subtraction (-), multiplication (*), division (/), floor/integer division (//), and modulus (%). 

#### Comparing Numbers 

* ">" = Greater than
* "<" = Less than
* ">=" = Greater than or equal to 
* "<=" = Less than or equal to 
* "==" = Equals to (a single = assigns a value to a variable)
* "!=" = Not equals 

### Conditional Statements

Conditional Statements separate parts of the program code that if a specific condition is met, only a portion of the code runs. The condition must result in a True or False (boolean) statement that determines whether the True section or the False section of the conditional statement runs. 

*Nested Conditional Statements* have conditional statements within other conditional statements. When the first condition is evaluated, it determines whether a second condition is also evaluated. 

```python
VALUE = int(input("Number: "))

if VALUE > 0: 
  #nested condition
  if VALUE < 10:
    print(VALUE)
  ```
## Contraction

Contractions are a common English technique where two words are combined together to make a single word with both meanings (i.e. do not :arrow_right: don't). In Python, there are two common contractions: decisions and accumulation (counting). 

**NOTE**: IB does not and prefers not to use contractions at all. 

### Decisions

```python
AVERAGE = float(input("Enter your average: "))

"""
if AVERAGE > 79.9: 
  GRADE = "A"
  else:
    if AVERAGE > 64.5:
     GRADE = "B"
    else:
      if...
"""

if AVERAGE > 79.9:
  GRADE = "A"
elif AVERAGE > 64.5:
  GRADE = "B"
elif AVERAGE > 49.9:
  GRADE = "C"
else
  GRADE = "D"
```

### Accumulation
```python
NUMBER = 0 

NUMBER = NUMBER + 1

#the above method is the same as,

NUMBER += 1

#Note: In C-based languages, it is NUMBER++

# Other operations
NUMBER -= 1 
NUMBER *= 2 
NUMBER /= 2
NUMBER //= 2 
NUMBER %= 2 

# Rarely do you use anything other than += or -=
```

## Inputs 

In programming languages, users are able to input information into the program manually. To create an input in python, the statement is ```input("Text that will be visible)```. Inputting text will always save the text as a string. If the entry is numeric, the text can then be *typecasted* into an integer or a float to perform calculations. 

NOTE: Inputs are the primary instructions the end user sees, therefore they need to be clear, concise, and provide instructions on what the user should enter. 

## Libraries 

Programming languages divide the commands capable within the programming language into separate files so that only a core set of commands make up the default language. This process allows programs to run with only the set of commands it requires to function, without the bloat of other commands not relevant to the current program. (For example, most programs do not need network management commands.) Programming languages have a **standard library** that is maintained as part of the language. 

There are also third-party libraries that can be installed an imported into the program as well. However, these libraries must be installed separately and rely on the maintenance of non-language programmers. Because these libraries are developed by third-parties, they may break with new updates or the developers may no longer offer updates to the library. Furthermore, including many third-party libraries can increase the complexity of installing and running the program. 

To add libraries to a program, there are three methods:

```python
# add an entire library
import random
print(random.randrange(2)) #this will output 0 or 1

# add a list of commands from a library
from random import randrange, randint 
print(randrange(2)) #waow you skipped a whole step! 

# import every function from a library (not recommended)
from random import * 
print(randrange(2))
# if there is another library with a function of the same name, it will confuse python

# import a library and rename the library
import random as r 
print(r.randrange(2))
# renaming libraries is generally not recommended as it makes clarity difficult
```

When importing an entire library, it is possible to list multiple libraries in a single import; however it increases the complexity of debugging and reduces readability. 

```python
import random, math, time
#very not recommended because this specific line would be changed a lot 
```

It is important to only import libraries that are neccessary for the program. You can access the Python standard libraries through [this](https://docs.python.org/3/library/) link. 