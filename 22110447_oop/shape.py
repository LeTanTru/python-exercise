import math


class Shape:
    def calculate_perimeter(self):
        pass

    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def calculate_area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

    def calculate_area(self):
        s = self.calculate_perimeter() / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))


radius = 5
length = 4
width = 6
side1 = 3
side2 = 4
side3 = 5

circle = Circle(radius)
print("Perimeter of circle:", circle.calculate_perimeter())
print("Area of circle:", circle.calculate_area())

rectangle = Rectangle(length, width)
print("Perimeter of rectangle:", rectangle.calculate_perimeter())
print("Area of rectangle:", rectangle.calculate_area())

triangle = Triangle(side1, side2, side3)
print("Perimeter of triangle:", triangle.calculate_perimeter())
print("Area of triangle:", triangle.calculate_area())
