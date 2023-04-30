# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

def isValid(s):
    # lets make three stacks initially
    # s1 for (), s2 for [], s3 for {}
    s1,s2, s3 =[], [], []
    for p in s:
        if p == '(' or p == ')':
            s1.append(p)
        elif p == '[' or p == ']':
            s2.append(p)
        else:
            s3.append(p)

    print(s1, '\n', s2, '\n', s3 ,'\n')

s = "()[]{}"
isIt = isValid(s)