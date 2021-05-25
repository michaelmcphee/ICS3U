#Michael McPhee, 05/09/21, fraction math practice program
import random

#gcd function using eucludian algorithm
def gcd(numeranswer, denomanswer):
   
    while denomanswer:
        numeranswer, denomanswer = denomanswer, numeranswer % denomanswer
    return numeranswer

#addition function
def add(numer1, numer2, denom1, denom2):
    numeranswer = ((numer1 * denom2) + (numer2 * denom1))
    denomanswer = (denom1 * denom2)
    z = gcd(numeranswer, denomanswer)
    denomanswer = denomanswer / z
    numeranswer = numeranswer / z
    return numeranswer, denomanswer

#subtraction function
def subtract(numer1, numer2, denom1, denom2):
    numeranswer = ((numer1 * denom2) - (numer2 * denom1))
    denomanswer = (denom1 * denom2)
    z = gcd(numeranswer, denomanswer)
    denomanswer = denomanswer / z
    numeranswer = numeranswer / z
    return numeranswer, denomanswer

#multiply function
def multiply(numer1, numer2, denom1, denom2):
    numeranswer = numer1 * numer2
    denomanswer = denom1 * denom2
    z = gcd(numeranswer, denomanswer)
    denomanswer = denomanswer / z
    numeranswer = numeranswer / z
    return numeranswer, denomanswer

#divide function
def divide(numer1, numer2, denom1, denom2):
    numeranswer = numer1 * denom2
    denomanswer = denom1 * numer2
    z = gcd(numeranswer, denomanswer)
    denomanswer = denomanswer / z
    numeranswer = numeranswer / z
    return numeranswer, denomanswer

#operation type function
def operationtype(numer1, numer2, denom1, denom2):
    #generate random number between 1 and 4
    x = int(random.randint(1,4))
    #each number is a diffent operation
    if x == 1:
        print (numer1 , "/", denom1, "plus ", numer2, "/", denom2)
        numeranswer, denomanswer = add(numer1, numer2, denom1, denom2)
    elif x == 2:
        print (numer1 , "/", denom1, "subtract ", numer2, "/", denom2)
        numeranswer, denomanswer = subtract(numer1, numer2, denom1, denom2)
    elif x == 3:
         print (numer1 , "/", denom1, "multiplied by ", numer2, "/", denom2)
         numeranswer, denomanswer = multiply(numer1, numer2, denom1, denom2)
    else:
         print (numer1 , "/", denom1, "divided by ", numer2, "/", denom2)
         numeranswer, denomanswer = divide(numer1, numer2, denom1, denom2)
    return numeranswer, denomanswer

#function that determines if answer is correct
def correct(numeranswer, denomanswer, useranswer, counter):
    #split user answer into numberator and denominator intergers
    answer = useranswer.split("/")
    usernumer = int(answer[0])
    userdenom = int(answer[1])
    #determine if answer is correct
    if usernumer == numeranswer and userdenom == denomanswer:
        print("Correct!")
        #add to correct answer counter
        counter = counter + 1
    else:
        #print correct answer
        print("Incorrect, the answer was ", numeranswer, "/", denomanswer)
    return counter

counter = 0

while True:
    #generate fractions
    numer1 = int(random.randint(1,10))
    denom1 = int(random.randint(1,10))

    numer2 = int(random.randint(1,10))
    denom2 = int(random.randint(1,10))
    
    #generate operation type
    numeranswer, denomanswer = operationtype(numer1, numer2, denom1, denom2)
    
    #obtain user answer
    useranswer = input("Enter answer: ")
    
    counter = correct(numeranswer, denomanswer, useranswer, counter)
    
    #ask user if they wish to continue
    y = input("Do you wish to continue (Enter yes/no): ")
    
    if y == "no":
        print("You had", counter, "correct answer(s)! Thanks for playing.")
        break