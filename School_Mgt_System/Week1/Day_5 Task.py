#Task 5	Create 3 classes demonstrating inheritance (e.g., Shape → Circle/Rectangle) with an area() method.

#  Shape
#  │
#  ├── Circle
#  │
#  └── Rectangle

class Shape:
    def area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


circle = Circle(5)
rectangle = Rectangle(10, 6)

print("Circle Area =", circle.area())
print("Rectangle Area =", rectangle.area())


# Task 5: Handle division-by-zero and invalid input safely with try/except.

try:
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))

    result = numerator / denominator

    print("Result =", result)

except ValueError:
    print("Error: Please enter valid numeric values.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")