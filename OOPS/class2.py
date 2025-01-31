class Car:
    def __init__(self, noOfwhe, noOfAir, color, name):
        print("It's a constructor")

        self.noOfWheels = noOfwhe
        self.noOfAirbag = noOfAir
        self.color = color
        self.carName = name

    def __str__(self):
        return self.carName

    def forward(self):
        print("Car is moving front: ", self)
    
    def backward(self):
        print("Car is moving back side")

    def __del__(self):
        print("Destructor called")

honda = Car(4, 6, "Black", "Honda")

honda.forward()

Kwid = Car(4, 6, "Black", "Kwid")

Kwid.forward()
