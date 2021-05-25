#Michael McPhee, 04/04/21, number sorter that divides largest by smallest

#ask user how many numbers are being entered
amount = int(input("Enter the amount of numbers: "))

#ask user for their first number to defince all of the variables outside of the loop
number = int(input("Enter a number: "))

#set the first number to be the largest and smallest numbers
largestnumber = number
smallestnumber = number

#create a loop that repeats one less than the amount of numbers being entered since one has already been entered
for i in range(amount-1):
    
    #ask for the next numbers and replace the largest and smallest numbers if applicable
    number = int(input("Enter a number: "))
    if number>largestnumber:
        largestnumber=number
    elif number<smallestnumber:
        smallestnumber=number

#print out the division between largest and smallest numbers
print("The division between the largest and smallest number is", largestnumber/smallestnumber)