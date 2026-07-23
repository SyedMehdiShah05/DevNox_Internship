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

