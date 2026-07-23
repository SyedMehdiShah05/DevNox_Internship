# Task 1: Swapping two numbers without using a third variable
#Method 1: Using arithmetic operations
print("Method 1: Using arithmetic operations")
a = 78
b = 109

a = a + b
b = a - b
a = a - b

print("a=", a)
print("b=", b)

# Method 2: Using tuple unpacking
print("\nMethod 2: Using tuple unpacking")

a = 223
b = 109

a, b = b, a
print("a=", a)
print("b=", b)

#method 3: Using XOR bitwise operation
print("\nMethod 3: Using XOR bitwise operation")

a = 223
b = 109

a = a ^ b
b = a ^ b
a = a ^ b

print("a=", a)
print("b=", b)