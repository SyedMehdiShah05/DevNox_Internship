# practice question Day 6, Create functions 
def greet_user():
    print("heloo")

greet_user()
greet_user()

# passing information to a function
 
def greet_user(username):
    print("helo , " + username.title() + "Mosvi")

greet_user('mehdi')

#passing argument

def describe_pet(animal_type, pet_name):
    print("\nI Have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet("Cat", " harry")
describe_pet("dog", "Dogesh")

#returning a simple value

def get_formatted_name(first_name, middle_name, last_name):
    full_name = first_name + " " + middle_name + " "+  last_name
    return full_name.title()
student = get_formatted_name("syed" , "Mehdi ","Mosvi")
print(student)

# # using a function with a while loop

# def get_name(fname, lname):
#     fname =fname + " " + lname
#     return fname.title()
# while True:
#     print("\nEnter Your name")
#     f_name = input("ENter first name:")
#     l_name = input("enter last name : ")

#     formatted_name = get_name(f_name, l_name)
#     print("\n Helo ," + formatted_name + "!")
    
def divide_numbers(a, b):
    try:
        # It will "try" to do this math
        result = a / b
        print("The answer is:", result)
    except:
        # If it fails (like dividing by zero), it runs this instead of crashing
        print("Oops! Something went wrong. Did you try to divide by zero?")

divide_numbers(10, 2)  # Works fine! Answer is 5.0
divide_numbers(10, 0)  # Fails safely! Prints the "Oops!" message.