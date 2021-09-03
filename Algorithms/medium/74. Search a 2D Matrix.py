import numpy as np
def binary_search_recursive(array, element, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if element == array[mid]:
        return mid

    if element < array[mid]:
        return binary_search_recursive(array, element, start, mid-1)
    else:
        return binary_search_recursive(array, element, mid+1, end)

def searchMatrix( matrix, target):
    '''
    Algo:
    Stesp1: iterate through matrix lists
    2. check the last element on the list(fidn how to index)
    fidn how oto index last elemnet:
    - length of list -1

    '''
    ### sol3,1 better than 60% submissions
    lastElemeIdx = len(matrix[0]) - 1
    for listNum, v in enumerate(matrix):
            lastElem = v[lastElemeIdx]
            if target <= lastElem:
                search = binary_search_recursive(v,target,0,lastElemeIdx)
                # print(search)
                if search >= 0:
                    return True
                else:
                    return False
                #### following was solution of solution1
                # print(search)
                # if target in v:
                #     return True
                # else:
                #     return False #( as defined by the constraints of the matrix. it is sorted so target cant be in this array )
            else:
                continue
############## slow solution
    # numpy_mat = np.array(matrix)
    # solutions = np.argwhere(numpy_mat == target)
    #
    # if len(solutions) > 0:
    #     return True
    # else:
    #     return False
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
# matrix = [[1]]
# target = 1
output = searchMatrix(matrix, target)
print(output)