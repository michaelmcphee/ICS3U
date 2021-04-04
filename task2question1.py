#Michael McPhee, 03/05/21, develops equation of linear graph from 2 points

x1 = int(input("Enter x1 "))
y1 = int(input("Enter y1 "))
x2 = int(input("Enter x2 "))
y2 = int(input("Enter y2 "))

#calculate numerator and denominator of the slope
slopenumerator = int(y2-y1)
slopedenominator = int(x2-x1)

#calculate numerator and denominator of the slope
yinterceptdenominator = int(slopedenominator*y1)
yinterceptnumerator = int((y1-slopenumerator/slopedenominator*x1)*yinterceptdenominator)


print("The equation of the line that passes through these points is y=",slopenumerator,"/",slopedenominator,"x +",yinterceptnumerator,"/",yinterceptdenominator)