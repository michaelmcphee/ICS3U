#Michael McPhee, 04/02/21, tip calculating program

#ask user subtotal and if they want to add tip
subtotal = float(input("Enter subtotal "))
tip = input("Do you wish to enter a tip (enter yes or no) ")

#ask user how they wish to tip
if tip == "yes":
    tipmethod = input("Do you wish to tip by a specific amount or by a percentage of the total (enter amount or percentage) ")
    
else:
    tipmethod = "none"

#calculte tip amount
if tipmethod == "amount":
    tipamount = float(input("How much do you wish to tip "))

elif tipmethod == "percentage":
    tipamount = float(input("What percentage of the subtotal do you wish to tip ")) * subtotal / 100
    
elif tipmethod == "none":
    tipamount = 0

#calculate tax and total
tax = float(subtotal*0.13)
total = float(subtotal+tipamount+tax)

#print values
print("Your subtotal is ", round(subtotal,2))
print("Your tax owed is ", round(tax,2))
print("Your tip is ", round(tipamount,2))
print("Your total is ", round(total,2))