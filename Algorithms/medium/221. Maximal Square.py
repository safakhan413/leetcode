# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

# Example 1:


# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4
# Example 2:


# Input: matrix = [["0","1"],["1","0"]]
# Output: 1
# Example 3:

# Input: matrix = [["0"]]
# Output: 0

from typing import List
import numpy as np

class Solution:
    def areaifSquare(self, y, i, j, sideLen):
        for x in range(i, i + sideLen):
            for z in range(j, j + sideLen):
                if y[x, z] == 0:
                    return 0
        return sideLen ** 2

    def findLargestSquareArea(self, y, rows, columns):
        maxArea = 0
        for i in range(rows):
            for j in range(columns):
                for sideLen in range(1, min(rows - i, columns - j) + 1):
                    area = self.areaifSquare(y, i, j, sideLen)
                    maxArea = max(maxArea, area)
        return maxArea

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        y = np.array(matrix, dtype=int)
        rows, columns = y.shape
        return self.findLargestSquareArea(y, rows, columns)

# def areaifSquare(y,i,j, diagonalSize):
#     square = False
#     for sideLen in range(diagonalSize-1):
#         if y[i+sideLen, j] =="1" and y[i, j+sideLen] =="1":
#             print("sides are square")
#             square = True
#             area = diagonalSize**2
#             return i, j, area
#         else:
#             print("sides are not square")
#             square = False
#             return i, j, 0


# def findLargestSquareArea(y, i, j, rows, columns):
#     areaSquare = 1
#     diagonal = 1

#     if 0< i+1 < rows and 0< j+1<columns and y[i+1, j+1] == "0": #i represnts width, j represents length
#         print('firstIfareasquare i, j, areasquare', i,j, areaSquare)
#         return areaSquare
    
#     # while 0< i+1 < width and 0< j+1<length

#     # if 0< i+1 < width and 0< j+1<length and y[i+1, j+1] == 1: # the diagonal is 1, increase lensquare and have the new i as i+1, j as j+1
#         #
#         # diagonal = diagonal+1

#     for incr in range(0, min(rows-i, columns-j)): # reasoning is that square cant be bigger than the length of the smaller of width and length
#         if 0< i+incr < rows and 0< j+incr<columns and y[i+incr, j+incr] == "1":
#             diagonal = diagonal+1
#             print(i,j, i+incr, j+incr, diagonal, 'im increi, incrj, diagonalLengthTocheck')
#             x, y, returnArea= areaifSquare(y,i,j,diagonal)
#             areaSquare = max(areaSquare, returnArea )
#             print('2nd method second loop, area', areaSquare)
#             return areaSquare

#     print('im area square')



#     # find the top left corner of square, return that with lengthof square
#     # check diagonal and with max diagonal try to see if the other indices around are also part of the square
#     # if even one 1 found, area = 1
#     # then check max(oldarea, newArea)
#     # return maxarea

#     # find longest continuous diagonals and then 



# import numpy as np
# def maximalSquare( matrix):
#     y = np.array(matrix)
#     print(y)
#     columns = len(matrix[0])
#     rows = len(matrix)
#     area = 0
#     for i in range(0,rows):
#         for j in range(0,columns):
#             print(y[i,j]=="1",y[i,j], 'im i js of y')
#             if y[i,j] == "1":
#                 print(i,j, 'in first method')
#                 area = findLargestSquareArea(y,i,j, rows, columns )
#                 # area = max(area, areaOfSquareAround(y, i, j, length, width))
#     return area


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
area = maximalSquare(matrix)
print(f'Im the final area \n {area} ')