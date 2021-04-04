#Michael McPhee, 03/05/21, solves for area perimeter and interior angles of triangle on a certain shape

import math

A = float(input("Enter A value "))
B = float(input("Enter B value "))
C = float(input("Enter C value "))

#calculate area
area = float((A*B)+(B*C/2)+(math.pi*((A/2)**2)/4))

#calculate perimeter
triangleperimeter = float(2*((C**2+(1/2*B)**2)**(1/2)))
rectangleperimeter = float(A+B)
circleperimeter = float(A+(math.pi*A/4))

perimeter = float(triangleperimeter+rectangleperimeter+circleperimeter)

#calculate interior angles
angle1 = float(math.degrees(math.atan(C/(1/2*B))))
angle2 = float(180-2*angle1)

#round answers
area = round(area, 2)
perimeter = round(perimeter, 2)
angle1 = round(angle1, 2)
angle2 = round(angle2, 2)

print("The area is ", area)
print("The perimeter is ", perimeter)
print("The interior angles are ", angle1, angle1, "and ", angle2 )