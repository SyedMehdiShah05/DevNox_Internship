# Write a program to check if a number is prime AND if a string is a palindrome.
 # Problem 1: Check if a number is prime when user give number 
num = int(input("Enter a number to check if it is prime: "))
if num <= 1:
    print(num, "is not a prime number.")
else:
    if all(num % i != 0 for i in range(2, int(num**0.5) + 1)): 
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")

# problem 2: Check if a string is a palindrome when user give string
def_palindrome = input("Enter a string to check if it is a palindrome: ")
cleaned = ''.join(c.lower() for c in def_palindrome if c.isalnum())
if cleaned == cleaned[::-1]:
    print(def_palindrome, " is a palindrome.")
else:
    print(def_palindrome, " is not a palindrome.")

# method 2 to check if a string is a palindrome

text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
