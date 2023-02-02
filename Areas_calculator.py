def triangle(base, height):
    return base * height / 2

def rectangle(length, breadth):
    return length * breadth

def circle(radius):
    return 3.14159265359 * radius ** 2

def square(lenght):
    return lenght*lenght

def parallelogram(base,height):
    return base*height

def trapezium(big_base,small_base,height):
    return (big_base+small_base)*height/2

figure = input("Enter the name of the figure (triangle, rectangle, circle, square, parallelogram or trapezium):\n ").lower()

if figure == "triangle":
    base = float(input("enter base: "))
    height = float(input("enter the height: "))
    print("The area of the triangle is ", triangle(base, height))

elif figure == "rectangle":
    breadth = float(input("enter base: "))
    length = float(input("enter the height: "))
    print("The area of the rectangle is", rectangle(length, breadth))

elif figure == "circle":
    radius = float(input("enter the radius: "))
    print("The area of the circle is", circle(radius))

elif figure == "square":
    lenght = float(input("enter the lenght: "))
    print("The area of the square is", square(lenght))

elif figure == "parallelogram":
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    print("The area of the circle is", parallelogram(base,height))

elif figure == "trapezium":
    big_base = float(input("Enter the big base: "))
    small_base = float(input("Enter the small base: "))
    height = float(input("Enter the height: "))
    print("The area of the circle is", trapezium(big_base,small_base,height))
else:
    print("Sorry, I didn't understand.")
