#Michael McPhee, 04/02/21, program that simulates the game bear ninja cowboy

import random

#user enters their choice
userchoice = input("Choose bear ninja or cowboy ")

#generate a random number and assign a chooice to each number
number = int(random.randint(1,3))

if number == 1:
    computerchoice = "bear"

elif number == 2:
    computerchoice = "ninja"

else:
    computerchoice = "cowboy"

#use if else statements to select winner
if userchoice == "bear" and computerchoice == "ninja":
    print("User picks", userchoice, ", computer picks", computerchoice, ". Bear mauls ninja. User wins!!! ")
    
elif userchoice == "ninja" and computerchoice == "bear":
    print("User picks", userchoice,  ", computer picks", computerchoice, ". Bear mauls ninja. Computer wins!!! ")
    
elif userchoice == "ninja" and computerchoice == "cowboy":
    print("User picks", userchoice,  ", computer picks", computerchoice, ". Ninja slashes cowboy. User wins!!! ")
    
elif userchoice == "cowboy" and computerchoice == "ninja":
    print("User picks", userchoice,  ", computer picks", computerchoice, ". Ninja slashes cowboy. Computer wins!!! ")
    
elif userchoice == "bear" and computerchoice == "cowboy":
    print("User picks", userchoice,  ", computer picks", computerchoice, ". Cowboy shoots bear. Computer wins!!! ")
    
elif userchoice == "cowboy" and computerchoice == "bear":
    print("User picks", userchoice,  ", computer picks", computerchoice, ". Cowboy shoots bear. User wins!!! ")

#else statement for all ties
else:
    print("User picks", userchoice,  ", computer picks", computerchoice, ". Tie game.")