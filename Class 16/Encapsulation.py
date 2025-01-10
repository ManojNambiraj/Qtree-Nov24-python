# Encapsulation:

    # getter
    # setter

    # Access specifier:
        # 1. Private
        # 2. Public

class Car:
    def __init__(self, mileage, no_of_wheels, cName):
        print("It's a constructor")
        self.__mileage = mileage
        self.no_of_wheels = no_of_wheels
        self.cName = cName

    def goForward(self):
        print("Car is moving front side")

    def get_mileage(self):
        return self.__mileage
    
    def set_mileage(self, new_mile):
        self.__mileage = new_mile


car1 = Car(20, 4, "Honda")

print("before: ", car1.get_mileage(), car1.no_of_wheels)

print("-------------------------------")

car1.set_mileage(55)

print("after: ", car1.get_mileage())
