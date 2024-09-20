# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 

# Example 1:


# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
import numpy as np

def isValidSudoku(board):
    # Print the board as a NumPy array for easier visualization
    import numpy as np

        # Print the board as a NumPy array for easier visualization
    print(np.array(board))

    def get_subgrid_list_comprehension(board, row_start, col_start):
        # Extract a 3x3 subgrid starting from (row_start, col_start) using a list comprehension
        return [board[i][j] for i in range(row_start, row_start + 3) for j in range(col_start, col_start + 3) if board[i][j].isdigit()]

    # Get the length of rows and columns (should be 9 for a standard Sudoku)
    rowColLen = len(board[0])
    print("Board Size:", rowColLen)

    # Loop over each row, column, and 3x3 block
    for i in range(rowColLen):
        # Get the current row and filter out non-digit elements ('.' for empty spaces)
        row = [board[i][j] for j in range(rowColLen) if board[i][j].isdigit()]
        
        # Get the current column and filter out non-digit elements ('.' for empty spaces)
        column = [board[j][i] for j in range(rowColLen) if board[j][i].isdigit()]

        # Debug prints
        print(f"Row {i}: {row} - Set: {set(row)}")
        print(f"Column {i}: {column} - Set: {set(column)}")
        
        # Check if there are duplicate digits in the row or column
        if len(row) > len(set(row)) or len(column) > len(set(column)):
            return False

    # Now check each 3x3 subgrid
    for row_start in range(0, rowColLen, 3):
        for col_start in range(0, rowColLen, 3):
            # Get the 3x3 subgrid starting from (row_start, col_start)
            threebythree = get_subgrid_list_comprehension(board, row_start, col_start)
            print(f"3x3 block starting at ({row_start}, {col_start}): {threebythree} - Set: {set(threebythree)}")
            
            # Check if there are duplicate digits in the 3x3 subgrid
            if len(threebythree) > len(set(threebythree)):
                return False

    # If no issues, return True (the board is valid)
    return True        

            # Each row must contain the digits 1-9 without repetition.
            # Each column must contain the digits 1-9 without repetition.
            # first check these two conditions




# board = [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]



board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(f'final solution:  {isValidSudoku(board)}')