def paranthesisBalanced(strP):
    print('hi')
    s = []
    newStr = strP.split()
    print(newStr)
    for i in newStr:
        print(s)
        if i == '(':
            s.append(i)

        else:
            if len(s) == 0:
                return False
            s.pop()

    if len(s) == 0:
        return True
    else:
        return False


        # s.append(i)
    print(s)


print(paranthesisBalanced('( ( ) ( ) ( ) ( ( ) ) ) )'))

'''
Algorithm:

( push
) pop

steps: paranthesis matching





'''


