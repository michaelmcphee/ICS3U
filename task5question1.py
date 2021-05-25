#Michael McPhee, 04/08/21, finds standard deviation and determines if a number exceptional

import random
import math

#define variables
standard_deviation = 0
x = []
y = []
sum1 = 0
sum2 = 0

#generate 150 random integers between 0 and 100
for i in range(150):
    x.append(random.randint(0,100))

#find average of integers
for q in range(150):
    sum1 = sum1 + x[q]
    
u = sum1/150

#find standard deviation
for p in range(150):
    y.append((x[p]-u)**2)

for t in range(150):
    sum2 = sum2 + y[t]

standard_deviation = math.sqrt(sum2/150)

#ask user for number
num = int(input("Enter a number: "))

#determine and display if number is exceptional
if (u + standard_deviation) < num or (u - standard_deviation) > num:
     print("Your number is exceptional.")

else:
    print("Your number is not exceptional. ")