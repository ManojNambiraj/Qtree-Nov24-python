# Operators:
    # 1) Arithmetic op

        # (+, -, *, /, %, **, //)

            # a = 5
            # b = 2

            # result = a + b
            # result = a - b
            # result = a * b
            # result = a / b
            # result = a ** b
            # result = a // b

            # print(result)

    # 2) Assignment op

        # (=, +=, -=, *=, /=, //=, %=, **=, &=, |=, ^=, >>=, <<=)

            # a = 5

            # a += 2    # a = a + 2
            # a -= 2    # a = a - 2
            # a *= 2    # a = a * 2
            # a /= 2    # a = a / 2
            # a //= 2    # a = a // 2
            # a %= 2    # a = a % 2
            # a **= 2    # a = a ** 2

            # print(a)

    # 3) Comparision op  --> (Boolean --> true or false)

        # (==, !=, >, >=, <, <=)

            # a = 5

            # result = (a == 5)
            # result = (a != 5)
            # result = (a > 5)
            # result = (a >= 5)
            # result = (a <= 5)

            # print(result)

    # 4) Logical op

        # (and, or, not)

            # and

            #  (True)  and (True)  ---> True
            #  (True)  and (False) ---> False
            #  (False) and (True)  ---> False
            #  (False) and (False) ---> False

            # a = 8

            # result = (a == 5) and (a > 10)

            # print(result)

            # or

            #  (True)  and (True)  ---> True
            #  (True)  and (False) ---> True
            #  (False) and (True)  ---> True
            #  (False) and (False) ---> False

            # not

            #   (True)  ---> False

            # a = 5

            # result = (a != 5) or (a < 3)

            # print(not(result))

    # 5) Identity op

        # (is, is not)

            # x = ["apple", "banana"]
            # y = ["apple", "banana"]
            # z = x

            # print(x is not y)
            # print(x is not z)

    # 6) Membership op

        # (in, not in)

            # x = "hello"

            # print("l" not in x)

    # 7) Bitwise op

        # (&, |, ^, ~, <<, >>)

         # &

            #  (1) & (1)  ---> 1
            #  (1) & (0)  ---> 0
            #  (0) & (1)  ---> 0
            #  (0) & (0)  ---> 0

                # x = 5
                # y = 7

                # result = x & y

                # print(result)

                # Implementation

                # (5) ---> 0101
                # (7) ---> 0111
                    # ----------------
                #          0101    ->    5

         # |

            #  (1) | (1)  ---> 1
            #  (1) | (0)  ---> 1
            #  (0) | (1)  ---> 1
            #  (0) | (0)  ---> 0

                # x = 5
                # y = 2

                # result = x | y

                # print(result)

                # Implementation

                # (5) ---> 0101
                # (2) ---> 0010
                # ----------------
                #          0111   ---> 7

         # ^

            #  (1) ^ (1)  ---> 0
            #  (1) ^ (0)  ---> 1
            #  (0) ^ (1)  ---> 1
            #  (0) ^ (0)  ---> 0

                # x = 5
                # y = 7

                # result = x ^ y

                # print(result)

                # Implementation

                # (5) ---> 0101
                # (7) ---> 0111
                    # ----------------
                #          0010    ->   2 

         # ~

            #  (1) ~   --> 0

                # x = 4

                # result = ~4

                # print(result)

        # <<

            # x = 3

            # result = x << 2

            # print(result)

            # Implementation

            # (3)  ----->   00000011

            # (1)  ----->   00000110
            # (2)  ----->   00001100   --> 12

        # >>

            # x = 40

            # result = x >> 2

            # print(result)

            # Implementation

            # (40)  ----->   00101000

            # (1)  ----->    00010100
            # (2)  ----->    00001010   ---> 10