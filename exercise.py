import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

d = (b**2) - (4*a*c)

if d > 0:
 root1= (-b+math.sqrt(d))/(2*a)
 root2= (-b-math.sqrt(d))/(2*a)
 print(f"The roots are {root1} and {root1}")
elif(d == 0):
    root1 = (-b+math.sqrt(d))/(2*a)
    root2 = (-b-math.sqrt(d))/(2*a)
    print(f"The root is {root1}")
elif d < 0:
    print("The equation has no real roots")
