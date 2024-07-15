"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]


Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]

"""



# def checkLiveNeighbours(board, row, col):

    #"""possible row +1done,col,  row-1done
        # col +1, col -1
        # diagonal : (row + 1, col -1)done,( row -1, col -1 )done, (rpow -1, col +1)done, (row +1, col +1)done

    
    # """
def checkLiveNeighbours(board, row, col):
    """
    Check the number of live neighbours around a given cell
    """
    numNeigh = 0
    ttRow = len(board)
    ttcols = len(board[0])

    # Checking all 8 neighbors
    directions = [
        (1, 0),   # down
        (-1, 0),  # up
        (0, 1),   # right
        (0, -1),  # left
        (1, 1),   # down-right
        (1, -1),  # down-left
        (-1, 1),  # up-right
        (-1, -1)  # up-left
    ]

    for d in directions:
        newRow, newCol = row + d[0], col + d[1]
        if 0 <= newRow < ttRow and 0 <= newCol < ttcols:
            if board[newRow][newCol] == 1:
                numNeigh += 1

    return numNeigh

def gameOfLife(board):
    """
    Out: Do not return anything, modify board in-place instead.
    Input: board
    Info: m * n board
    Steps:





    """
    import numpy as np
    x = np.array(board)
    print(x)
    rows = x.shape[0]
    columns = x.shape[1]
    print(x.shape[0])
    # result = [[0]*columns for _ in range(rows)]
    deadList = []
    aliveList = []
    for row in range(rows):
        for col in range(columns):
            x = checkLiveNeighbours(board, row, col)
            if board[row][col] ==1:
                #dead cells tuples list 
                if x < 2:
                    deadList.append((row,col))
                    # board[row][col] =2 #mark cell to be dead
                elif 2 <= x <=3:
                    # result[row][col] =3
                    aliveList.append((row,col))
                elif x>3:
                    deadList.append((row,col))

            if board[row][col] ==0:
                if x==3:
                    aliveList.append((row,col))
    
    for d in deadList:
            board[d[0]][d[1]] = 0

    for d in aliveList:
        board[d[0]][d[1]] = 1

            # print('neighbour of ', row, col, x)
            # print(x[row][col], 'each')
    

    print('final \n',board)






# board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
gameOfLife(board)
