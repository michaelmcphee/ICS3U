#Michael McPhee, 04/04/21, simple math problem practice

import random

#generate random numbers and type of question
num1 = int(random.randint(0,50))
num2 = int(random.randint(0,50))
questiontype = int(random.randint(0,2))

#create variable that tracks tries
y=5

#create loop that asks for users answer and repeats until the user is correct or 5 tries are over
for x in range(0,5):
    if (questiontype == 1):
        realanswer = num1 - num2
        print(num1, "-", num2)
        useranswer = int(input("Enter answer: "))
    else:
        realanswer = num1 + num2
        print(num1, "+", num2)
        useranswer = int(input("Enter answer: "))
            
    if realanswer == useranswer:
        print("Correct!")
        break
    else:
        print("Incorrect, try again. ")
        y=y-1
        

if y==0:
    print("Your 5 tries are over, the answer is", realanswer)

    