class Car:
    def __init__(self, m, w, c, CN):
        print("It's a Constructor")
        self.mileage = m
        self.wheels = w
        self.color = c
        self.cName = CN

    def forward(self):
        print("Moving front")

    def __str__(self):
        return self.cName
    
    def __del__(self):
        print("I'm Destructor", self)

car1 = Car(21.0, 4, "Red", "City")

print(car1.mileage, car1.color)

car2 = Car(15.0, 5, "Black", "Honda")

print(car2.mileage, car2.color)