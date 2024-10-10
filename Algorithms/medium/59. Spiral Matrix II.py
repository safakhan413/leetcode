# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

# Example 1:


# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
# Example 2:

# Input: n = 1
# Output: [[1]]
 

# Constraints:

# 1 <= n <= 20

def generateMatrix(n):
    import numpy as np
    # np.array
    # pass
    lst = [[None] * n for _ in range(n)]
    print(lst)

    left, right=0,n
    top, bottom = 0, n


    # while left < right and top <bottom:

        # Go through first row and assign values
    counter = 0
    for i in range(left, right):
        lst[left][i] = counter
        print(top,i)
        counter +=1
    top +=1

    for i in range(top, bottom):
        lst[i][right-1]= counter
        print('r', right-1,i)
        counter +=1
    # top +=1
    print(np.array(lst))


    print(lst)



    # arr = [None][None]*n
    # print(arr)
n= 3
# output = [[1,2,3],[8,9,4],[7,6,5]]
generateMatrix(n)