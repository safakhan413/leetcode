def convert( s: str, numRows: int) -> str:
    print('hi')

    # Algorithm:
    # Output: Linearize the zig zagged string matrix
    # input: string and number of rows in which to make the string zag zag
    # Algorithm steps:
    # Two special cases identified: when n =1 return the string when n = 2 the zig zag arrangement will be opposite (desc becomes asc) in each new column
    # We first code without these two special cases:
    # 1. make one array containing non-diagonal called ND values
    # 2. make other array with diagonal D values
    # 3. until there are values in array of string(use while true) put n values in ND and then n-2 values in D
    # 4. Then make new string by appending s.t for  if i%n ==0 then append all thsoe strings. For next strings take e.g. i%n ==1 take values but insert
    # n-2-1. When it is tiem to pick the next element from thsi D array now the. In D array always reverse the string ebfore adding to D string then pick teh second one afetr
    # first index

 # d and nd list /diagonal and nondiagonal lists
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

