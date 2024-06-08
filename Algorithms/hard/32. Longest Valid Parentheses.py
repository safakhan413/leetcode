# Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
# substring
# .

 

# Example 1:

# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
# Example 2:

# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
# Example 3:

# Input: s = ""
# Output: 0



# def longestValidParentheses(s):
#     print(s)
from collections import deque

def isValidParantheses(s):
    print(s)

    """
    input: string containing parantheses
    output: True or false

    Algo:

    create a dictionary s.t. closing brackets are keys with opening brackets as values
    if opening brakcets i.e. brackets in dic.keys( put in stack1)
    as soon as the bracket is not in keys then its a closing bracket and put in s2

    then check s2 -1 and corresponding value in dic, if they match pop from both s1 and s2. if all elelments are gone like this
    OR you don't encounter mismatching parantheses(s2 keys value does not match) then return True otherwise false

    """

    # dic = {")": "(", "]": "[", "}":"{"}
    # s1 =deque([])
    # s2 =deque([])


    # for i in s:
    #     if i in dic.keys():
    #         s2.append(i)
    #     else:
    #         s1.append(i)
    # print(s1,s2)
    # i = 0
    # while len(s2) > 0:



    # # for i in range( len(s2)):
    #     # print(s2[i])
    #     # if dic[s2[i]] == s1.pop():

    #     #     s2.popleft()
    #     #     print(s1,s2)
    #     # elif dic[s2[i]] == s1.popleft():
    #     #     s2.popleft()
    #     #     print('second condition', s1,s2)
    #     print(dic[s2[i]], s1[-1], s1[0])
    #     if dic[s2[i]] == s1[-1]:
    #         s1.pop()
    #         s2.popleft()
    #         print('first conditio',s1,s2)
    #     elif dic[s2[i]] == s1[0]:
    #         s2.popleft()
    #         s1.popleft()
    #         print('second condition', s1,s2)


    #     else:
    #         return False
    # if len(s2) ==0 and len(s1) == 0:
    #     return True
    # else:
    #     return False

    # # print(s1,list(reversed(s2)))
    # # for i
    stack = []
    pair = {')' : '(' , ']' : '[' , '}' : '{'}
    for c in s:
        if c in pair: # check the keys
            if stack and stack[-1] == pair[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False


s ="([{}])"
s1 = "({)}" # for s1 its false
s3 = "()[]{}"

print(isValidParantheses(s1))
