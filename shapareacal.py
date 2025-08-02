import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Run with user input
while True:
    print("\n1. Circle\n2. Rectangle\n3. Triangle\n4. Exit")
    choice = input("Choose a shape: ")

    if choice == '1':
        r = float(input("Enter radius: "))
        shape = Circle(r)
    elif choice == '2':
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        shape = Rectangle(l, w)
    elif choice == '3':
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        shape = Triangle(b, h)
    elif choice == '4':
        break
    else:
        print("Invalid choice.")
        continue

    print(f"Area = {shape.area():.2f}")
