"""
    class/Objects

    1. Encapsulation
    2. Inheritance
    3. Polymorphism
    4. Abstraction

"""
# 1. Encapsulation

class Car:
    def __init__(self, wheels, color):
        self.__no_of_wheels = wheels
        self.car_color = color

    def set_wheels(self, num):
        self.__no_of_wheels = num

    def get_wheels(self):
        return self.__no_of_wheels

honda = Car(4, "red")

honda.set_wheels(6)

print(honda.get_wheels())




