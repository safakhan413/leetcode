def searchMatrix( matrix, target):
    '''
    Algo:
    Stesp1: iterate through matrix lists
    2. check the last element on the list(fidn how to index)
    fidn how oto index last elemnet:
    - length of list -1

    '''
    ### sol1
    # lastElemeIdx = len(matrix[0]) - 1
    # for listNum, v in enumerate(matrix):
    #     for j in matrix[listNum]:
    #         lastElem = v[lastElemeIdx]
    #         if target <= lastElem:
    #             if target in v:
    #                 return True
    #             else:
    #                 return False #( as defined by the constraints of the matrix. it is sorted so target cant be in this array )
    #         else:
    #             continue


# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 3
matrix = [[1]]
target = 1
output = searchMatrix(matrix, target)
print(output)