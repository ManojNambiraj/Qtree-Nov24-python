# OOPS

"""

     Class/Object
    1. Encapsulation
    2. Inheritance
    3. Polymorphism
    4. Abstraction

"""

# Class -->  Template

class Mobile:
    color = ""
    cost = 0
    battery = 0

    def make_call(self):
        print("Hi... Calling someOne", self)

apple = Mobile()  # instance

apple.make_call()

# apple.color = "Silver"

# print("Apple: ", apple.color)



Moto = Mobile()

Moto.make_call()

# Moto.color = "Black"

# print("Moto: ", Moto.color)