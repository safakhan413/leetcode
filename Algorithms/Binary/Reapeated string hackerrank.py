import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    '''
    if i dont make a new string.
    1. count number of as in the x len string
    2. multiply that with the rpt times for count.
    3. for remainder create a string and see how many a's are there
    '''
    # Write your code here
    lenS = len(s)
    rpt_times = n//lenS
    remainder = n%lenS
    print(rpt_times, remainder)
    ## should i make a new string  at all
    count = 0
    for i in s:
        if i == 'a':
            count +=1
    count_for_rpt_times = count * rpt_times
    remainderS = s[:remainder]
    for i in remainderS:
        if i == 'a':
            count_for_rpt_times +=1
    return count_for_rpt_times

### solution num 2

    # newS = s*rpt_times + s[0:remainder]
    # print(newS)
    # # a_dict = dict()
    # count = 0
    # for i in range(n):
    #     if 'a' == newS[i]:
    #         count +=1
    # print(count)
    # return count

    # numT = Coun
    # dicti = dict()
    # # for i in range(0,n):
    # #     dicti['a'] = dicti.getit



# s =  'aba'
# n = 10
s ='a'
n = 1000000000000
print(repeatedString(s,n))