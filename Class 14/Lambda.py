# Normal function

    # def fun(a, b):
    #     return a * b

    # ans = fun(10, 5)

    # print(ans)

# lambda arguments : expression

    # res = lambda a, b : a * b

    # print(res(77, 5))

def demo(n):
    return lambda a : a * n

answer = demo(5)

print(answer(50))