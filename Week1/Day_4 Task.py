# Build a small function library: temperature converter + simple area calculator (circle, rectangle).

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
 
print("25°C =", celsius_to_fahrenheit(25), "°F")
print("77°F =", fahrenheit_to_celsius(77), "°C")

# Area calculator functions
def circle_area(radius):
    return 3.14159 * radius * radius


def rectangle_area(length, width):
    return length * width


print("Circle Area =", circle_area(5))
print("Rectangle Area =", rectangle_area(10, 4))

# Task4: Create a Student class with name/marks attributes and a method to compute grade.
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def compute_grade(self):

        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "F"

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)
        print("Grade:", self.compute_grade())


student1 = Student("Ali", 86)

student1.display()