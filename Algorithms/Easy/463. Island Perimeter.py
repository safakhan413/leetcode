def checkNumAdjacent1s(grid, i,j, length, width):
    # then check for i-1,j, i, j-1, i, j+1, i+1,j
    numAdj1s = 0
    if 0<= i-1 < width and grid[i-1,j] == 1:
        numAdj1s = numAdj1s + 1
    if 0<= j-1 < length and grid[i,j-1] == 1:
        numAdj1s = numAdj1s + 1
    if 0< i+1 < width and grid[i+1,j] == 1:
        numAdj1s = numAdj1s + 1
    if 0< j+1 < length and grid[i,j+1] == 1:
        numAdj1s = numAdj1s + 1
         # i is for width # j is for length
    return numAdj1s

def giveAppPerimeter(adjs):
    
    if adjs == 4:
        return 0
    elif adjs == 3:
        return 1
    elif adjs == 2:
        return 2
    elif adjs == 1:
        return 3
    else:
        return 4  
    

def islandPerimeter(grid):
    print(grid)
    length = len(grid[0])
    width = len(grid)
    print(width, length)

    import numpy as np

    y = np.array(grid)
    print(y, y.shape)
    perimeter = 0
    for i in range(width):
        for j in range(length):
            if y[i][j] == 1:
                print(i,j)
                adjs = checkNumAdjacent1s(y, i,j, length, width)
                perimeter = perimeter + giveAppPerimeter(adjs)
                print(adjs, perimeter)
                # checkVa
                # then check for i-1,j, i, j-1, i, j+1, i+1,j
                
                # condition to check for 4 adjacent 1s
                # cond1 = 



                # perimeter = perimeter + 4
                # if (y[i-1][j] and y[i-1][j] ==1):
    return perimeter



    # for i, j in y:
    #     print(i,j)

# grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

x = islandPerimeter(grid)