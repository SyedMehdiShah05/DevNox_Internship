class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_des_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()


my_new_car = Car("audi", "a4", 2020)

print(my_new_car.get_des_name())






# class Dog():
#     def init(self, name, age):
#         self.name = name
#         self.age = age

#     def sit(self):
#         print(self.name.title() + "is now sitting .")

#     def roll_over(self):
#         print(self.name.title() + "rolled over ! ")

# my_dog = Dog("helo", 23)
# Dog.sit()
# Dog.roll_over()

