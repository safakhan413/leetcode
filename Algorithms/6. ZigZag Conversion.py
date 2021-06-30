def convert(self, s: str, numRows: int) -> str:
    print('hi')

    # Algorithm:
    # Output: Linearize the zig zagged string matrix
    # input: string and number of rows in which to make the string zag zag
    # Algorithm steps:
    # Two special cases identified: when n =1 return the string when n = 2 the zig zag arrangement will be opposite (desc becomes asc) in each new column
    # We first code without these two special cases:
    # 1. make one array containing non-diagonal values
    # 2. make other array with diagonal values





s1 = "PAYPALISHIRING" #14
numRows1 = 3
# Output: "PAHNAPLSIIGYIR" #7 columns

s2 = "PAYPALISHIRING" #14
numRows2 = 4
# Output: "PINALSIGYAHRPI" #7 columns

