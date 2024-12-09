# List 

# students_height = [169, 175, 152, 151, 166, 165, 169, 175, 151, "oneFiveSeven", True, [1, 2 ,3]]

# # indexing:        #0   #1   #2   #3.................

#Find type

# print(type(students_height))

#Find Length

# print(len(students_height))

# #Joining List

# lst1 = [1,2,3]
# lst2 = [4,5,6]

# lst3 = lst1 + lst2

# print(lst3)

# List Replication

# lst1 = [1,2,3]

# lst3 = lst1 * 5

# print(lst3)

# List constructor

# lst1 = ("apple", "banana", "orange")

# lst2 = list(lst1)

# print(type(lst2))

# Quiz

# lst1 = ["apple", "banana", "orange"]

# if "kiwi" in lst1:
#     print("Answer is right")
# else:
#     print("something went wrong")

# Change the Item in list

# lst1 = ["apple", "banana", "orange", "kiwi", "dragon", "grapes"]

# lst1[1:4] = ["blackcurrent", "cherry"]

# print(lst1)

# List Methods - Add items

# lst1 = ["apple", "banana", "orange", "kiwi", "dragon", "grapes"]

# # lst1.append("cherry")
# # lst1.extend(["cherry", "greenApple"])
# lst1.insert(2, "cherry")

# print(lst1)

# List Methods - Remove items

# lst1 = ["apple", "banana", "orange", "kiwi", "dragon", "grapes"]

# print(lst1)

# # lst1.remove("orange")
# # lst1.pop() # lst1.pop(3)
# # del lst1[1]
# # lst1.clear()
# # lst1.sort()
# lst1.sort(reverse=True)

# print(lst1)

# Nested List

# lst = [[1,2,3],[4,5,6],[7,8,9]]

# print(lst[2][2])

lst1 = ["apple", "banana", "orange", "kiwi", "dragon", "grapes"]

for i in lst1:
    print(i)