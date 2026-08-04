#practice 1 : loops

for i in range(1, 11):
    print(i, end=' ')


# practice 2 : print my name 10 time using loop
for i in range(10):
    print("My name is : Mehdi Mosvi")


# practice 3 : user ask to enter name and how many time he/she want to print it using loop
name = input("Enter your name: ")
times = int(input("How many times do you want to print your name? "))
for i in  range(times):
    print(name)




# # Task 3 Print the Fibonacci series using a loop, then again using recursion.

# n =int(input("Enter the number of terms for Fibonacci series: "))

# a = 0
# b = 1

# for i in range(n):
#     print(a, end=' ')
#     a, b = b, a + b

# #method 2 fibonacci series using loop 


# # method 2: using recursion
# def fibonacci_recursive(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
#     else:
#         fib_series = fibonacci_recursive(n - 1)
#         fib_series.append(fib_series[-1] + fib_series[-2])
#         return fib_series
#     n = int(input("Enter the number of terms for Fibonacci series (using recursion): "))
# fib_series = fibonacci_recursive(n)
# print("Fibonacci series :", fib_series)