def reverse(x):
    s = []
    signNeg = 0
    for i in str(x):
        if i == '-':
            signNeg = 1
            continue
        s.append(i)
    newInt = ''
    for i in range(len(s)):
        newInt = newInt + s.pop()
    if signNeg == 1:
        newInt = int('-' + newInt)
    else:
        newInt = int(newInt)
    if newInt < -2 ** 31 or newInt > 2 ** 31 - 1:
        print('im at least here')
        return 0
    return newInt


x= -123
# reverse(x)
print(reverse(x))