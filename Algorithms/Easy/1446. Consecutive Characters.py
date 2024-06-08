"""The power of the string is the maximum length of a non-empty substring that contains only one unique character.

Given a string s, return the power of s.

 

Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
 """
from itertools import groupby


# def maxLen(s):
#     max(len)

def maxPower(s):
    # print(s)
    x = groupby(s)
    max = 0
    for k, v in x:
        # print(k, list(v))
        length = len(list(v))
        # print(length,max)
        if length > max:
            max = length
    return max

    # print(list(x))
    # for i in enumerate(x):
    #     print(i, '/n', list(i[1][1]))

str1 = "abbcccddddeeeeedcba"
i = maxPower(str1)
print(i)