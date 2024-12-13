# Python Function:

# def demo(value):
#     return value * 100

# num = int(input("Enter the number:"))

# result = demo(num)

# print("Result is: ", result)

# Quiz: Area of rect (l*w)

# l = int(input("Enter the Rect Length:"))
# w = int(input("Enter the Rect Width:"))

def areaOfRect(length, a, width=1):   # Parameters
    return length * width + a

result = areaOfRect(length=5, a=8)        # Arguments

print("Area of Rect:", result)

"""
    keyword parameter
    default parameter
    position parameter
"""