from heapq import *


class Solution:
    def furthestBuilding(self, heights, bricks, ladders):
        heap = []

        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]

            if diff > 0: ## if 2nd bld is higher than 1st bld
                heappush(heap, diff)
            if len(heap) > ladders: ## if all possible diff> 0 are greater than ladders
                bricks -= heappop(heap) ## pop smallest elems to consum bricks
            if bricks < 0: ##terminate
                return i

        return len(heights) - 1

s = Solution()
# heights = [4,2,7,6,9,14,12]
# bricks = 5
# ladders = 1
heights = [4,12,2,7,3,18,20,3,19]
bricks = 10
ladders = 2
bldIndex = s.furthestBuilding(heights,bricks,ladders)