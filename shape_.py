from math import pi


class Shape:
    def get_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = pi * self.radius**2
        return area


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        area = self.length * self.width
        return area


circle = Circle(5)
print(circle.get_area())

rectangle = Rectangle(7, 4)
print(rectangle.get_area())
