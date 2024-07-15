
import string
# >>> string.ascii_lowercase
# 'abcdefghijklmnopqrstuvwxyz'

# >>> list(map(chr, range(97, 123)))
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', '

def myAtoi(s):
    """
    Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.
    
    """
    s = s.lstrip()  # ignore leading whitespaces
        
    if not s:
        return 0
    
    sign = 1
    start_index = 0
    if s[0] == '-':
        sign = -1
        start_index = 1
    elif s[0] == '+':
        start_index = 1
    
    num = 0
    for i in range(start_index, len(s)):
        if s[i].isdigit():
            num = num * 10 + int(s[i])
        else:
            break
    
    num *= sign
    
    # Handle 32-bit signed integer range
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    if num < INT_MIN:
        return INT_MIN
    if num > INT_MAX:
        return INT_MAX
    
    return num
    # s = s.lstrip() #ignore leading whitespaces
    # # check if it starts with -, if it does then filter is digit on s and multiple with -1 to get the dig
    # #get digpart + sign  before first nondigit
    # # print(int(s))
    # # print(chr(97))
    # # alphabets = 'abcdefghijklmnopqrstuvwxyz'
    # alphabets = string.ascii_lowercase
    # print(alphabets)
    # if s.startswith("-") and all([x.isdigit() for x in s[1:]]):
    #     return int(s)
    # elif(all([x.isdigit() for x in s])):
    #     return int(s)
    # # print(any([s.startswith(c) for c in 'abcdefghijklmnopqrstuvwxyz']))
    # elif any([s.startswith(c) for c in alphabets] ):
    #     print('incorrect s')
    #     return 0
    # else:
    #     # pos_s = s.find()
    #     num = 0
    #     pos = len(s
    #     for i,chars in enumerate(s):
    #         if chars in alphabets:
    #             pos = i
    #             break
    #             print('im position of first non dig', pos)
    #         # num = num * 10 + int(char)
            

    #     truncated = s[:pos]    
    #     if truncated:
    #                 num = int(truncated)
    #     else:
    #         num = 0
            
    #     # Handle 32-bit signed integer range
    #     INT_MIN, INT_MAX = -2**31, 2**31 - 1
    #     if num < INT_MIN:
    #         return INT_MIN
    #     if num > INT_MAX:
    #         return INT_MAX

    #     return num




        # truncated  = "".join(filter(str.isdigit,s[:pos]))
        # return int(truncated)
        # print('im truncated', truncated)
    
            
    
    ### else go through string, join all the digits truncate after the first non0 

        # return()

    # x = "".join(filter(str.isdigit,s))
    # print(x)






# s = "42"
# s = " -042"
s = "1337c0d3"
# s = "0-1"
# s = "words and 987"

res = myAtoi(s)
print('res', res)