#  279. Perfect Squares
# Given an integer n, return the least number of perfect square numbers that sum to n.

# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

# Example 1:

# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# Example 2:

# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

def numSquares(n):
    # pass
    import math
    # we need to get least number so we will take perfect squares after sqrt
    start = math.floor(math.sqrt(n))
    valids = []
    for i in range(start,n):
        if math.sqrt(i) == int(math.sqrt(i)):
            valids.append(i)
    ## once you get valids list
    res = []
    for i in valids:
        quotient, remainder = divmod(n,i)
        if remainder ==0:
            res.extend([i]*quotient)
            return quotient
        else:
            n -=i
        print(quotient, remainder, res)
# mm.
    print(math.sqrt(n), valids)
n=13
print(numSquares(n))