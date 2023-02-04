import math

def bhaskara_formula(a,b,c):
    delta = b**2 - 4 *a*c
    if delta < 0:
        print("Sorry, but it doesn't have real solutions")
        return None
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    return x1, x2

a = float(input("Enter the A: "))
b = float(input("Enter the B: "))
c = float(input("Enter the C: "))
results = bhaskara_formula(a, b, c)

if results:
    x1, x2 = results
    print("Solution 1:", x1)
    print("Solution 2:", x2)


