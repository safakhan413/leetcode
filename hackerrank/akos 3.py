def eval(val1,val2,i):
    value = 0
    if i == '*':
        value = val1 * val2
    elif i == '+':
        value = val1 + val2
    elif i == '-':
        value = val1 - val2
    else:
        value = val1/val2
    # print(val1 )
    return value


def evaluatePostfix(string):
    ''' Algorithm
    Convert postfix into infix version
    How?

    create a stack
    push when you see numebrs
    when you come across symbol the first time you pop two values from stack
    evaluate with that symbol. put in temp
    if there is a value in stack still then evaluate with temp, otherwise()nothing left in stack move on


    :param string as postfix notation expression:
    :return: evaluated value
    '''
    numbers = '123456789'
    symbols = '*+-/'

    postfix = string.split()
    print(postfix)
    stack = []
    for i in postfix:
        if i in numbers:
            stack.append(i)
        else:
            val1 = int(stack.pop())
            val2 = int(stack.pop())
            evaluation = eval(val1,val2,i)
            stack.append(evaluation)
            print(stack)
    return stack.pop()







    #constraints numbers 1 digit

# 1 + 2 * 3 + 4 --> 1 2 3 * + 4 +
# (1 + 2) * (3 * 4) --> 12+34+*


evaluatePostfix('1 2 3 * + 4 +')