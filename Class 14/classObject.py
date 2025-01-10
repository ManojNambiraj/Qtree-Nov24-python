class Car:

    def __init__(self, mileage, model, carName):
        print("It's a constructor")
        self.mileage = mileage
        self.model = model
        self.carName = carName

    def forward(self):
        print("Go Front")

    def backward(self):
        print("Go Back")

car1 = Car(20.5, 2012, "city")

print(car1.mileage, car1.model, car1.carName)

car2 = Car(18.0, 2018, "Verna")

print(car2.mileage, car2.model, car2.carName)