# List

# nums = [10, 20, 30, 40, "hello", [1,2,3,5]]

# nums[2] = 2000

# print(nums)

# Tuple

# tup = ("hello", 10, 20, "300", True)

# print(type(tup))
# print(type(tup))
# print(tup[-4:])


# Traversel

# for i in tup:
#     print(i)

# Change value

# temp = list(tup)    # tup[-1] = False

# temp[-1] = False

# tup = tuple(temp)

# print(tup)

# # Change the value using tuple joinin (or overwriting)
# tup1 = (100,)

# print(type(tup1))

# tup += tup1

# print(tup)

# Remove the items:

# tup = ("hello", 10, 20, "300", True)

# del tup

# print(tup)

# Unpacking:

fruits = ("apple", "banana", "orange" , "kiwi", "dragon", "grapes", "banana", "banana")

(red, yellow, orange) = fruits

print(orange)

# myTuple = fruits * 2

# print(len(fruits))

# print(fruits.index("banana"))