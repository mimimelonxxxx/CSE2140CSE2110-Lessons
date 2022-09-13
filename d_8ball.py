#d_8ball.py
"""
title: Magic 8 Ball! 
author: Michelle Jiang
date-created: 2022-09-12
"""
"""
Notes: 
create 20 different responses 
"""
import random 

### Intro ### 
print("Shake the magic 8 ball! Seek to find ~*the answer in mind*~")

# Input # 
VALUE = input("Think your question, think it twice. Then ENTER in the 8 ball. (Just press ENTER to shake the ball)")

# Processing # 
if VALUE == "":
    ANSWER = random.randint(1, 20)

# Output #
    if ANSWER == 1:
        print("⭐Certainly.⭐")
    elif ANSWER == 2:
        print("✨It is decidedly so.✨")
    elif ANSWER == 3:
        print("⭐Without a doubt.⭐")
    elif ANSWER == 4:
        print("✨Absolutely✨")
    elif ANSWER == 5:
        print("⭐Definitely⭐")
    elif ANSWER == 6:
        print("✨You can count on it✨")
    elif ANSWER == 7:
        print("⭐Yes⭐")
    elif ANSWER == 8:
        print("✨Most likely✨")
    elif ANSWER == 9:
        print("✨Outlook good.✨")
    elif ANSWER == 10:
        print("⭐Signs point to yes.⭐")
    elif ANSWER == 11:
        print("✨Cannot be determined.✨")
    elif ANSWER == 12:
        print("⭐Your mom⭐")
    elif ANSWER == 13:
        print("⭐Try again⭐")
    elif ANSWER == 14:
        print("✨Ask again later✨")
    elif ANSWER == 15:
        print("⭐Now is not a good time⭐")
    elif ANSWER == 16:
        print("✨ Sorry, but no. ✨")
    elif ANSWER == 17:
        print("~*Clear your mind*~ and ask again")
    elif ANSWER == 18:
        print("⭐The stars do not align⭐")
    elif ANSWER == 19:
        print("✨My sources say no✨")
    else:
        print("~*It is not fated*~")