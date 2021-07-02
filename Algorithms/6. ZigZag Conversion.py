def convert( s: str, numRows: int) -> str:
    print('hi')

    # Algorithm:
    # Output: Linearize the zig zagged string matrix
    # input: string and number of rows in which to make the string zag zag
    # Algorithm steps:

 # d and nd list /diagonal and nondiagonal lists
    #remove all prints if pasting in leetcode
    if numRows == 1:
        return s
    step = 1
    pos = 1
    lines = {}
    for c in s:
        if pos not in lines:
            print(pos, 'im pos', 'and im step',step)
            lines[pos] = c
            print(lines, 'when pos  not in lines')
        else:
            print(pos, 'im pos', 'and im step',step)
            lines[pos] += c
            print(lines, 'when pos in lines'),
        pos += step
        if pos == 1 or pos == numRows:
            step *= -1
    sol = ""
    for i in range(1, numRows + 1):
        try:
            sol += lines[i]
            print('im sol', sol)
        except:
            return sol
    return sol






s1 = "PAYPALISHIRING" #14
numRows1 = 3
# Output: "PAHNAPLSIIGYIR" #7 columns

s2 = "PAYPALISHIRING" #14
numRows2 = 4
print(convert(s2,numRows2))
# Output: "PINALSIGYAHRPI" #7 columns

