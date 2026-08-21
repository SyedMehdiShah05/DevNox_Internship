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



# 3 Write a function that returns the second-largest number in a list.
def second_largest(numbers):
    # Remove duplicates
    unique_numbers = list(set(numbers))

    if len(unique_numbers) < 2:
        return None

    unique_numbers.sort()

    return unique_numbers[-2]


numbers = [10, 45, 23, 67, 89, 89, 34]

result = second_largest(numbers)

if result is None:
    print("Second largest number does not exist.")
else:
    print("Second Largest Number:", result)