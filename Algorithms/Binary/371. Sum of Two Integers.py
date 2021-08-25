## Completing all curated questions
# https://www.teamblind.com/post/New-Year-Gift---Curated-List-of-Top-75-LeetCode-Questions-to-Save-Your-Time-OaM1orEU

def getSum( a,b):
    '''Algo:
    Output: sum of two ints without using + or -
    Input: two ints a and b
    Step1:
    Use bitwise manipulation
    '''
    print(a|b)
    print(a^b)
    # add_aNb = a|b
    # aNb = a&b
    # sum = add_aNb | aNb
    # print(add_aNb, aNb, sum)
    # | operator gives a+b - (a and b)
    # so to add you have to add back (a and b)

    # print(a or b)

a = 1
b = 2
getSum(a,b)