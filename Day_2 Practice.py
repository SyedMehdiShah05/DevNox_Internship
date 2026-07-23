# Day 2 practice problems
# Problem 1: 
age = 20
if age ==20:
    print("You are 20 years old.")

# practice problem 2: make a simple function to check if a number is even or odd whaen user give number

def check_even_odd(num):
    if num % 2 == 0:
        return f"{num} is an even number."
    else:
        return f"{num} is an odd number."

# test the function
user_input = int(input("Enter a number to check if it is even or odd: "))
result = check_even_odd(user_input)
print(result)

# practice problem 3: nested if else statement to check if a number is positive, negative or zero when user give number
input = int(input("Enter a number to check if it is positive, negative or zero: "))
if input > 0:
    print(input, "is a positive number.")
else:
    if input < 0:
        print(input, "is a negative number.")
    else:
        print(input, "is zero.")   

