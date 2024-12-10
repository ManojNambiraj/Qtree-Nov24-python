# Dictionaries

# thisDict = dict(brand= "Ford", model= "Ecosport", year= 1995, "brandName": "fordCars"= "Ford")         // Constructor
# thisDict = {"brand": "Ford", "model": "Ecosport", "year": 1995, "brandName": "Ford"}


# Methods:

# print(thisDict[brand])
# print(len(thisDict))
# print(type(thisDict))
# print(thisDict)
# print(thisDict.get("model"))
# print(thisDict.keys())
# print(thisDict.values())
# print(thisDict.items())

# Quiz

# if "1995" in thisDict:
#     print(True)

# Changing values

# thisDict = {"brand": "Ford", "model": "Ecosport", "year": 1995, "brandName": "Ford"}

# thisDict.update({"brandName": "fordCars"})
# thisDict.update({"fuel": "petrol"})
# thisDict["year"] = 2020
# thisDict["fuel"] = "Disel"

# print(thisDict)

# Remove item:

# thisDict.pop("model")
# thisDict.popitem()

# del thisDict

# print(thisDict)

# for i, j in thisDict.items():
#     print(i, j)

# Copy

thisDict = {"brand": "Ford", "model": "Ecosport", "year": 1995, "brandName": "Ford"}

# mydict = dict(thisDict)

# print(mydict)

# Nested Dictionaries

# myParent = {
#     "child1": {
#         "name":"nancy", 
#         "age": 23
#     }, 
#     "child2": {
#         "name": "raj", 
#         "age": 25
#     }
# }


# print(myParent)
# print(myParent["child2"]["age"])

