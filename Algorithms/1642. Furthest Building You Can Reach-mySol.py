'''
Output: index of building to which you can reach
Input: 1. Array of heights. Index 0-i representing builing num
2. numbricks
3. num ladders

Algorithm:
- define an array fo differences with len n-1
- loop through array s.t. you store diff in array.
- multiply each with -1 to reverse the signs
- find all max elements and their indices.
- see if building[maxIndex - 1] first max can be reached with bricks.
- Then use ladder for the first max otherwise use bricks and when they finish a ladder

'''

import operator
import numpy

class Solution:
    def diffheight_and_maxtillIndex(self,heights, bricks, ladders):
        diffHeights = []
        print('Inputs are:', heights)
        sum = 0
        j = 0
        maxIdx = 0
        for i in range(0, len(heights) - 1):
            diffHeights.append(-1 * (heights[i] - heights[i + 1]))
            # if diffHeights[i] > 0 and sum <= (bricks+ladders):
            sum = diffHeights[i] + sum
            # if sum > bricks and j == 0:
            if sum > bricks and ladders > 0 :
                # j = 1
                ladders = ladders - 1
                maxIdx = i ## we want the pos in diffHeights array which has len n-1
        return diffHeights,maxIdx


    def furthestBuilding(self, heights, bricks, ladders) :
                # sum = diffHeights[i] + sum
            # if diffHeights[i] > 0:
        diffHeights, maxIndex = self.diffheight_and_maxtillIndex(heights, bricks, ladders)
        npdiff = numpy.array(diffHeights[0:maxIndex])
        indices = npdiff.argsort()[-1*(maxIndex):][::-1]
        print('im numpy', npdiff)
        print('im numpy max indices', indices)
        print('im diff heights', diffHeights)
        print('im mighty maxIndex', maxIndex)

        bldIndex = 0
        for i in range(0,len(diffHeights)):
            if i in indices[0:ladders] and ladders > 0:
                print('condition1', diffHeights[i])
                ladders = ladders - 1
                bldIndex = bldIndex +1
            elif diffHeights[i] > 0 and bricks > 0 and bricks > :
                bricks = bricks - diffHeights[i]
                print('condi2', diffHeights[i], bricks)
                bldIndex = bldIndex + 1
            elif diffHeights[i] < 0:
                print('cond3', diffHeights[i])
                bldIndex = bldIndex + 1
        print('im bldidx', bldIndex )
        return  bldIndex

s = Solution()
# heights = [4,2,7,6,9,14,12]
# bricks = 5
# ladders = 1
heights = [4,12,2,7,3,18,20,3,19]
bricks = 10
ladders = 2
bldIndex = s.furthestBuilding(heights,bricks,ladders)
# print('heyyy Im building index', bldIndex)