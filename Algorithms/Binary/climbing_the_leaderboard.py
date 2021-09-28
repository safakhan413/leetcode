import math
import os
import random
import re
import sys

from collections import Counter

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    print('hey')
    # ranked.sort(reverse=True)
    # print(ranked)
    '''Algo:
    Output: increasing ranks of new player
    Input: two lists. One of the leaderboard with scores for ranks.
    2. of new player score. 
    
    Steps: 1. combine the two arrays into one and sort.
    2. Create  a dictionary where value is the ranking.
    How to do that: start index with i. check for each value, if its the same as the last 
    then assign the same i and
     if it is not the same as the last
    3. 
    
    '''
    cout1 = dict(Counter(ranked))
    cout1 = cout1.fromkeys(cout1, 0)
    print(cout1)
    i = 0
    for k,v in cout1.items():
        i+=1
        cout1[k] = i
    print(cout1)
    res = []
    for k,v in cout1:
        for i in player:
        if i > k:
            res.append(cout1[k]+1)
        else:



    # newR = ranked + player
    # newR.sort(reverse=True)
    # print(newR)
    # cout1 = dict(Counter(newR))
    # i = 0
    # cout1 = cout1.fromkeys(cout1, 0)
    # print(cout1)
    # for k,v in cout1.items():
    #     i+=1
    #     cout1[k] = i
    # print(cout1)
    # res = []
    # for i in player:
    #     res.append(cout1[i])
    # print(res)
    # # print(cout1)
    # print(cout1)



    # Write your code here

ranked = [100, 90, 90, 80, 75, 60]
player = [50, 65, 77, 90, 102]
climbingLeaderboard(ranked, player)
