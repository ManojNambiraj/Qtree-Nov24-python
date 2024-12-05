# if(10 > 5):
#     print("It's Greater")
# else:
#     print("It's Wrong")

# print("It's Greater" if(3 > 5) else "It's Wrong")

# Looping statements or Iterations

# 1) For loop

    # Forward Looping

    # for i in range(0, 10, 2):
    #     print(i)

    # Backward Looping

    # for i in range(10, 1, -2):
    #     print("hi")

# 2) While loop

    # num = 10

    # while(num > 0):
    #     print(num)
    #     num -= 1

# Jumping Statement

# 1) continue

"""
for i in range(0, 10, 1):
    if(i == 4):
        continue
    print(i)
"""

# 2) Break

# for i in range(0, 10, 1):
#     if(i == 4):
#         break
#     print(i)

# Nested Loop

# Expected OP

"""
1
12
123
1234
12345
"""

n = int(input("Enter the n Value:"))

for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end="")
    print()