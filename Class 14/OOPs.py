"""
    OOPs ----> Object Oriented Programmings

    --> Class
    --> Object
    --> Inheritance
    --> Ploymorphism

"""

class Car:
    cName = ""
    model = ""
    milage = 0.0
    year = 0

    def forward(self):
        print("Go Front")

    def backward(self):
        print("Go Back")


Honda = Car()  #instantiation (object)

Honda.milage = 20.5

print("Honda: ", Honda.milage)

Skoda = Car()

Skoda.milage = 16.7   # 2023
Skoda.milage = 14     # 2024

print("Skoda: ", Skoda.milage)

Skoda.forward()

