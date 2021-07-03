def reverse(x):
    # s = []
    # signNeg = 0
    # for i in str(x):
    #     if i == '-':
    #         signNeg = 1
    #         continue
    #     s.append(i)
    # newInt = ''
    # for i in range(len(s)):
    #     newInt = newInt + s.pop()
    # if signNeg == 1:
    #     newInt = int('-' + newInt)
    # else:
    #     newInt = int(newInt)
    # if newInt < -2 ** 31 or newInt > 2 ** 31 - 1:
    #     print('im at least here')
    #     return 0
    # return newInt
    if x > 0:  # handle positive numbers
        a = int(str(x)[::-1])
    if x <= 0:  # handle negative numbers
        a = -1 * int(str(x * -1)[::-1])
        # handle 32 bit overflow
    mina = -2 ** 31
    maxa = 2 ** 31 - 1
    if a not in range(mina, maxa):
        return 0
    else:
        return a
        # ```

x= -123
# reverse(x)
print(reverse(x))