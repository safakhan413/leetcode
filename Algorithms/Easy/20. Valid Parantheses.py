# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

def isValid(s):
# brute force because the innermost should at least be nested properly fpor it to work
    # while True:
    #     if '()' in sequence :
    #         sequence = sequence.replace ( '()' , '' )
    #     elif '{}' in sequence :
    #         sequence = sequence.replace ( '{}' , '' )
    #     elif '[]' in sequence :
    #         sequence = sequence.replace ( '[]' , '' )
    #     else :
    #         return not sequence

    
#  we will use stack though 
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

    # lets make three stacks initially
    #below brute force approach didn't work because doesnt hold for "([)]" should be correctly nested too

    # s1 for (), s2 for [], s3 for {}
    # s1,s2, s3 =[], [], []
    # for p in s:
    #     if p == '(' or p == ')':
    #         s1.append(p)
    #     elif p == '[' or p == ']':
    #         s2.append(p)
    #     else:
    #         s3.append(p)

    # pt1,pt2,pt3 = 0,0,0        
    # while len(s1) > 0:
    #     a = s1.pop()
    #     if a == ')':
    #         pt1 = pt1 + 1
    #     else :
    #         pt1 -=1

    # while len(s2) > 0:
    #     a = s2.pop()
    #     print(a)
    #     if a == ']':
    #         pt2 = pt2 + 1
    #         print('###########', pt2)
    #     else :
    #         pt2 -=1
    #         print('@@@@@@@@@@@', pt2)


    # while len(s3) > 0:
    #     a = s3.pop()
    #     if a == '}':
    #         pt3 = pt3 + 1
    #     else :
    #         pt3 -=1

    # print(s1, pt1, '\n', s2, pt2, '\n', s3 , pt3, '\n')
    # if pt1 == 0 and pt2 == 0 and pt3 == 0:
    #     return True
    # else:
    #     return False

s = "()[]{}"
isIt = isValid(s)
print(isIt)