from itertools import product


def transpose(matrix):
    '''Algo:
    outut: i want transpose. I want in each iteration first elem of each list is pciked and put in elemnts of matrix tra
    
    '''
    # matrix_tra = [[0]*len(matrix[0])]*len(matrix)
    # for i in range(len(matrix)):
    #     smallList = []
    #     for j in range(len(matrix[0])):
    #         print(i,j)
    #         smallList.append(matrix[j][i])
    #         print(smallList)
    #     matrix_tra[i] = smallList
    n, m = len(matrix), len(matrix[0])
    transposed = [[None] * n for _ in range(m)]
        # matrix_tra[i] = smallList
    for i, j in product(range(n), range(m)):
        print(i,j)
        transposed[j][i] = matrix[i][j]
    return transposed
            # matrix_tra[j][i] = matrix[i][j]
    # print(matrix_tra)
    # for i,v in enumerate(matrix):
    #
    #     (matrix_tra[i]).append(v[i])
    # print(matrix_tra)
    #     for j,elem in enumerate(i):
    #     for j in range(len(matrix)):
    #         # i,j
    #         matrix_tra[i][j] = matrix[j][i]
    # return matrix_tra

matrix = [[1,2,3],[4,5,6]]
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
out = transpose(matrix)
print(out)