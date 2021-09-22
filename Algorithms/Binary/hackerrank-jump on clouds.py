import math
import os
import random
import re
import sys
import unittest

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    '''Algo:
    Output: shortest path to reach the end
    Input: a binary array. 0 is good, 1 is bad.
    Constraints: Steps can only be 1 or 2.
    Steps:
    1. for each array index check the next two array indices.
    check minsteps: whichever is min num of steps return that
    1.1. If next is 1 then add the index+2
    1.2 if next to next is 1 then add+1 only and check again

    '''
    i = 0
    step = 0
    while i < len(c)-1:##last can never be 0. second last can be 0 and we will check that
        if i + 2 >= len(c) or c[i+2] == 1:
            print(i,'im in second if')
            i +=1
            step+=1
            continue
        else:
            print(i, 'im in 4th if')
            i +=2
            step+=1
            continue
    print(step)

        # for j in range(1,3):
        #     if c[i+]

        # print('a')
        # i +=1

c =[0,0,0,1,0,0]
##output is 3
jumpingOnClouds(c)

