# Task 3 Print the Fibonacci series using a loop
n =int(input("Enter the number of terms for Fibonacci series: "))

a = 0
b = 1

for i in range(n):
    print(a, end=' ')
    a, b = b, a + b




# Task 3 Print the Fibonacci series using using recursion.

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

terms = int(input("\nEnter number of terms: "))

for i in range(terms):
    print(fibonacci(i), end=" ")