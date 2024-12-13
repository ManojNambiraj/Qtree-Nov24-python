# set1 = {2, 3, 4, 5, 6}

# set1.add(True)

# set1.remove(2)

# set1.clear()

# print(type(set1))
# print(set1)

# set1 = {1,2,3}
# set2 = {3,4,5}

# Union, intersection, difference --> Based on Maths ven diagrams

# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set2.difference(set1))

# Traversal

# set1 = {10, 55, 22, 36}

# for i in set1:
#     print(i)

# print(44 in set1)

# Quiz

# set1 = {1,2,3}
# set2 = {3,4,5}

# print(set1.union(set2).intersection(set2))  # o/p: {3, 4, 5}

# List Comprehension

lst = [10, 20, 30, 77, 99, 55, 22, 36]

eve_num = [i for i in lst if i%2 != 0]

# for i in lst:
#     if i % 2 != 0:
#         eve_num.append(i)

print(eve_num)