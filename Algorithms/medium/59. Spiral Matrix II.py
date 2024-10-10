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

    counter = 1

    while left < right and top <bottom:

        # Go through first row and fill it in spiral fashion
        for i in range(left, right):
            lst[left][i] = counter
            print(top,i)
            counter +=1
        top +=1

        # Go through the last column and fill it in spiral fashion
        for i in range(top, bottom):
            lst[i][right-1]= counter
            print('r', right-1,i)
            counter +=1
        right -=1
        # Go through the last row and fill it in spiral fashion
        for i in range(right-1, left-1,-1 ):
            lst[bottom-1][i]= counter
            print('b', bottom-1,i)
            counter +=1
        bottom -=1

        # Go through the first col and fill it in spiral fashion
        for i in range(bottom-1, top-1,-1 ):
            lst[i][left]= counter
            print('l', left,i)
            counter +=1
        left +=1

    # top +=1
    print(np.array(lst))


    print(lst)
    return list(lst)


    # arr = [None][None]*n
    # print(arr)
n= 3
# output = [[1,2,3],[8,9,4],[7,6,5]]
print('final',generateMatrix(n))