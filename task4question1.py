#Michael McPhee, 04/04/21, customizable bar graph

#ask for values
bar1 = int(input("Enter value 1: "))
bar2 = int(input("Enter value 2: "))
bar3 = int(input("Enter value 3: "))
bar4 = int(input("Enter value 4: "))
bar5 = int(input("Enter value 5: "))

#create variable that tracks wether or not user went over limit of 30
y=1

#if statement changing variable if user went over 30
if bar1 > 30 or bar2 > 30 or bar3 > 30 or bar4 > 30 or bar5 > 30:
    y=0
    print("Please try again with values less than 30. ")

#for loops printing bars only if variable didn't change
for x in range(0,bar1):
    if (y == 1):
        print("@", end = "")
    
print("")
    
for x in range(0,bar2): 
    if (y == 1):
        print("@", end = "")

print("")

for x in range(0,bar3): 
    if (y == 1):
        print("@", end = "")

print("")

for x in range(0,bar4):
    if (y==1):
        print("@", end = "")

print("")

for x in range(0,bar5): 
    if y == 1:
        print("@", end = "")
