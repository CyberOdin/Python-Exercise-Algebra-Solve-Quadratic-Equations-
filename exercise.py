""" Solving Quadratic Equations"""
"""
The two roots of a quadratic equation ax^2 + bx + c = 0 can be obtained using the following formula:
b^2 - 4ac is called the discriminant of the quadratic equation. If it is positive, the equation has two real roots.
If it is zero, the equation has one root. If it is negative, the equation has no real roots.
Write a program that prompts the user to enter values for a, b, and c and displays the result based on the discriminant.

If the discriminant is positive, display two roots.

If the discriminant is 0, display one root.

Otherwise, display “The equation has no real roots”.
"""


import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

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
