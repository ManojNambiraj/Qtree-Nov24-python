# Python Inheritance

# # # Single Inheritance

# class Vehicle:                                #  Parent class
#     no_of_wheels = 0

#     def moveForward(self):
#         print("moving front side")


# class Car(Vehicle):                           #  Child class
#     no_airbags = 2

#     def fm(self):
#         print("Playing music")

# car = Car()

# car.moveForward()
# car.fm()


# # Multi level Inheritance

# class Vehicle:                                #  Parent class  --> Level 1
#     no_of_wheels = 0

#     def moveForward(self):
#         print("moving front side")


# class Car(Vehicle):                           #  Child class   --> Level 2
#     no_airbags = 2

#     def fm(self):
#         print("Playing music")

# class Innova(Car):                            # Grant child    --> Level 3
#     no_of_sheets = 7

#     def colorOfCar(self):
#         print("My car color is red")


# inn = Innova()

# inn.fm()
# inn.moveForward()
# inn.colorOfCar()

# # # Hierarchical inheritance

# class Vehicle:                                #  Parent class
#     no_of_wheels = 0

#     def moveForward(self):
#         print("moving front side")


# class Car(Vehicle):                           #  Child 1 class
#     no_airbags = 2
#     no_of_wheels = 4

#     def fm(self):
#         print("Playing music")

# class Bike(Vehicle):                          #  Child 2 class
#     no_of_wheels = 2

#     def fuel(self):
#         print("It's a EV")

# car = Car()

# car.moveForward()

# bike = Bike()

# bike.moveForward()

# # # Multiple Inheritance

class Father:
    def hairColor(self):
        print("Father hair color is brown")

class Mother:
    def music(self):
        print("Mother having a music Skills")

class Son(Father, Mother):
    def sports(self):
        print("Playing Football")

child = Son()

child.hairColor()
child.music()