# a = int(input("Enter the first number: "))
# b = int(input("Enter the Second number: "))
# c = int(input("Enter the Third number: "))

# if a >= b and a >= c:
#     largest = a
# elif b >= a and b >= c:
#     largest = b
# else:
#     largest = c

# print(f"The largest number is: {largest}")

# a = 50
# b = 70

# print("a is:", a , " " , "b is: ", b)

# # a, b = b, a

# temp = a
# a = b
# b = temp

# print("a is:", a , " " , "b is: ", b)

# n = int(input("Enter your temp: "))

# if n >= 30:
#     print("It's hot")
# elif n >= 15 and n <= 30:
#     print("It's Moderate")
# else:
#     print("It's Cool")

"""
6. Anagrams
Write a function that checks if two strings are anagrams of each other.


Ex1:

Input: "listen", "silent"
Output: True

Ex2:

Input: "Hello", "world"
Output: False

"""

# from collections import Counter

# def isAnagram(str1, str2):
#     str1 = str1.replace(" ", "").lower()
#     str2 = str2.replace(" ", "").lower()

#     return Counter(str1) == Counter(str2)

# str1 = input("Enter the Str1: ")
# str2 = input("Enter the Str2: ")

# if isAnagram(str1, str2):
#     print("It's Anagram")
# else:
#     print("Not Anagram")

"""
8. Subarray with Maximum Sum
Write a Python function to find the contiguous subarray with the maximum sum from a list of integers.

Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6 (subarray [4, -1, 2, 1])
"""
def max_sub_array(nums):
    max_sum = float('-inf')
    current_sum = 0

    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

nums = list(map(int, input("Enter the integer values separated by space: ").split()))

result = max_sub_array(nums)

print(result)