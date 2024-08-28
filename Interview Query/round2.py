## class implementation of a stack

## pop and push method

# class Stack:
#     def __init__(myself, arr=None):
#         if arr is None:
#             myself.stack = []
#         else:
#             myself.stack = arr
    
#     def push(self, elem):
#         self.stack.append(elem)
#         print(self.stack)

#     def pop(self):

#         # self.stack.remove(-1)
#         return self.stack.pop()

# s1 = Stack([2,3])
# s1.push(1)
# print(f" popped value: {s1.pop()}")

# # print(help([]))

# ________________________________________________

import time
# s = time
# print(s)

# print(help(time))






# import logging
# def execution_decorator(func):
#     def wrapper( *args, **kwargs):
#         start = time.time()
#         result = func(*args)
#         end = time.time()
#         executionTime = end - start
#         logging.INFO(f'my execution time is {executionTime} and result is {result}')
#         return result




# @execution_decorator
# def addit(a,b):
#     return a+b

# print(addit(5,4))


# Given a list of sorted integers how do you find unique ones inside it
input= [0,0,1,2,2,2,3,4,4,4]
# output: [0,1,2,3,4]

from collections import Counter
def uniqueInts(input):
    # uniqueSet = set(input)
    # return list(uniqueSet)
     #not allowed to use set
    # uniqueCounts = dict(Counter(input))
    # print(uniqueCounts)
    # return list(uniqueCounts.keys())

    # for i, elem in enumerate(input):
    if len(input)==0 or len(input)==1:
        return input
    
    for i in range(1, len(input)):
        prev = input[i-1]
        print('prev',prev)
        if prev == input[i]:
            # input[:] = input[:i]
            # input.pop

            # input.remove(input[i])
    



print(f'Unique elements are : {uniqueInts(input)}')