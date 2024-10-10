# 54. Spiral Matrix
# Medium
# Topics
# Companies
# Hint
# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

def traverse_boundaries(submat, level, m,n):
    # any level other than level 0 you need to move the indexes i.e. if level1 
    pass

def spiralOrder(matrix):
    import numpy as np
    a = np.array(matrix)
    m = len(a[0,:])
    n = len(a[:,0])
    rown0= a[0,:]
    col0= a[:,0]
    print(a, a.size, m,n)

    class node:
        def __init__(self, val,visited=0):
            self.val = val
            self.visited = visited
    # in every iteration the number of rows and columns will be omitted from the omitted and inside matrix will be passed

    # for  
    #
    ## check if there are 4 boundaries of the rectangle 
    # observation: Anytime m and n reach 1 then just get the m +n returned
    # Otheriwse keep decrementing m and n and passing indexes

    result += 

    """
    Algo:
    1) get first row, 
    2) get last column skip the first element of last column
    
    3)Get last row
    4) get first column till you skip the first element of column
    5) move inwards by 1 and repeat for smaller matrix 

    base case: [123][456] -> [123654] 
    """

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
spiralOrder(matrix)