#Michael McPhee, 04/04/21, two diamonds

#let user pick size of diamond
x = int(input("Enter diamond size: "))

#create top triangles
for i in range(x):
    
    #create first top triangle
    for j in range(x-i-1):
        print(end = " ")
    for k in range(2*i+1):
        print(end = "*")
        
    #create second top triangle
    for j in range(2*(x-i)-1):
        print(end = " ")
    for k in range(2*i+1):
        print(end = "*")
    
    #start new line
    print(" ")
    
#create bottom triangles
for i in range(x):
    
    #create first bottom triangle
    for j in range(i):
        print(end = " ")
    for k in range(2*(x-i)-1):
        print(end = "*")
    
    #create second bottom triangle
    for j in range(2*i+1):
        print(end = " ")
    for k in range(2*(x-i)-1):
        print(end = "*")
    
    #start new line
    print(" ")
