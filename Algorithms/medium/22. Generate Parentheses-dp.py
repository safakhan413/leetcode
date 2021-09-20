from itertools import combinations, product, permutations
#
# def valid(s):
#     open, close = 0,0
#     for c in s:
#         if c == '(':
#             open += 1
#         elif c == ')':
#             close +=1
#             ## on the ifrst misplaces closing parantheses this combination will become invalid
#             if close > open:
#                 return False
#     return True
#
#
# def generateParenthesis(n):
#     # Given n pairs of parentheses, write a function to generate all combinations of well - formed parentheses.
#     '''Algo:
#     1. First generate all possible parantheses
#     2.1 one way to do it is get all possible combinations of these paranthesis
#     2.2 check if it is a valid parantheses closing problem through stack
#     3. use dp in the next sol
#     '''
#     ########################## solution 1 #####################
#
#     perms = set(''.join(p) for p in permutations('(' * n + ')' * n))
#     return [s for s in perms if valid(s)]
#
#     ########################## solution 2 ########################
def generateParenthesis(n):
    ans = []

    def backtrack(S=[], left=0, right=0):
        if len(S) == 2 * n:
            ans.append("".join(S))
            return
        if left < n:
            S.append("(")
            print('before pop S', S)

            backtrack(S, left + 1, right)
            S.pop()
            print('after pop S', S)
        if right < left:
            S.append(")")
            print('x1 before pop S', S)

            backtrack(S, left, right + 1)
            S.pop()
            print('x1 after pop S', S)

    backtrack()
    return ans


n = 3
print(generateParenthesis(n))