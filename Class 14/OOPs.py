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

    def forward():
        print("Go Front")

    def backward():
        print("Go Back")


Honda = Car()

Honda.milage = 20.5

print("Honda: ", Honda.milage)

Skoda = Car()

Skoda.milage = 16.7   # 2023
Skoda.milage = 14     # 2024

print("Skoda: ", Skoda.milage)

