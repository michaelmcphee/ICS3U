#Michael McPhee, 04/02/21, displays 3 numbers from the user from smallest to largest
num1 = int(input("Enter a first number "))
num2 = int(input("Enter a second number "))
num3 = int(input("Enter a third number "))

#use if else statements to oragnize and display numbers
if num1 < num2 and num2 < num3:
    print("The numbers from smallest to largest are ", num1, num2, num3)
    
elif num1 < num3 and num3 < num2:
    print("The numbers from smallest to largest are ", num1, num3, num2)
    
elif num2 < num3 and num3 < num1:
    print("The numbers from smallest to largest are ", num2, num3, num1)
    
elif num2 < num1 and num1 < num3:
    print("The numbers from smallest to largest are ", num2, num1, num3)
    
elif num3 < num1 and num1 < num2:
    print("The numbers from smallest to largest are ", num3, num1, num2)
    
else:
    print("The numbers from smallest to largest are ", num3, num2, num1)