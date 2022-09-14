# e_coinflip.py

"""
title: Coin Flip
author: Michelle Jiang
date-created: 2022-09-14
"""

from random import randrange

def intro(): # used to define stuff! 
    print("""
Welcome to Coin Flip! Get points by choosing the right answer. Lose points if you choose incorrectly. 
    """)

def heads(): 
    print("""
          __-----__
     ..;;;--'~~~`--;;;..
   /;-~IN GOD WE TRUST~-.\\
  //      ,;;;;;;;;      \\
.//      ;;;;;    \       \\
||       ;;;;(   /.|       ||
||       ;;;;;;;   _\      ||
||       ';;  ;;;;=        ||
||LIBERTY | ''\;;;;;;      ||
 \\     ,| '\  '|><| 1995 //
  \\   |     |      \  A //
   `;.,|.    |      '\.-'/
     ~~;;;,._|___.,-;;;~'
         ''=--'
    """)

def tails(): 
    print('''
               ,,==="""""""===,,
           ,==""' |\ |   /\   `""==,
        ,="'|\    | \|  /__\   /\  `"=,
      /"    |,"\  |  | /'  `\ /  )     "\\
    /"  ,"  |                 `\/    /|  "\\
   /'  |   ,                       /",|   `\\
  /'   ",/"                           |    `\\
 /'      I=I=I               ,d8ba,___      `\\
/'     I=8=8=8=I_I_          88888P"""       `\\
|   xXXXXXXXXXXXXXXXxIxx    ,888"             |
| ~XXXXXXXXXXXXXXX~-~-~-~-~ d888~-~-~-~-~-~-~ |
| ~-~-~-~-~-~-~-~-,aad888ba,8888,-~-~-~-~-~-~ |
| ~-~-~-~-~-~-,ad888888888888888b-~-~-~-~-~-~ |
\ ~-~-~-~-~,ad8888888888888888888-~-~-~-~-~-~ /
`\ -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~- /'
 `\ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~,-,~~~~~ /'
  `\    /"\         1 9 9 4        \ /\    /'
   `\  "\,/'                   |\   `\ `  /'
     "\      /""\   |    |     |,'\     /"
       `"=,_ \__/   |__  |__   |    ,="'  
          `""=,__             __,=""'     
               ``""=========""''
    ''')

### MAIN PROGRAM CODE ### 

SCORE = 0
intro()

while True:

    # Inputs # 
    CHOICE = int(input("Choose both heads(1), both tails(2), or heads and tails(3): "))

    # Processing # 
    COIN1 = randrange(2) # randomly chooses an integer between 0 and 1
    COIN2 = randrange(2) 

    if COIN1 == 1 and COIN2 == 1: 
        RESULT = 1 # HH
    elif COIN1 == 0 and COIN2 == 0: 
        RESULT = 2 # TT
    else: 
        RESULT = 3 # HT TH

    # RESULT = COIN1 + COIN2 # 0 both tails, 1 heads and tails, 2 both heads

    # Output #
    if COIN1 == 1: 
        heads()
    else: 
        tails()

    if COIN2 == 1: 
        heads()
    else: 
        tails()

    if CHOICE == RESULT: 
        print("You guessed correctly!")
        SCORE += 10
        print("Your score is: ", SCORE)
    elif SCORE == 0: 
        print("You can't go much lower than that!")
        print(f"Your score is: {SCORE}") # print(f " ") allows you to use variables within the string
    else: 
        print("You'll get it next time!")
        SCORE -= 5
        print("Your score is:", SCORE)