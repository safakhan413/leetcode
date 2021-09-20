def trap(height):
    '''Algo:
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
    Output: Number of units of water trapped
    Input: List of the brick walls position
    Steps:
    Observations:
    find all subsequences s.t. left is some height and right is some height at least equal or greater than the left and
    then figure out how much water can be trapped in that subsequence.

    '''
    max_left = [0] * len(height)
    for x in range(1,len(height)):
        max_left[x] = max(height[x-1], max_left[x-1])
        # print(max_left)
    max_right = [0] * len(height)
    for x in range(len(height)-2, -1, -1):
        max_right[x] = max(height[x+1], max_right[x+1])
    res = 0
    for x in range(len(height)):
        water_level = min(max_left[x], max_right[x])
        if water_level >= height[x]:
            res += water_level - height[x]
    return res
            # print(water_level)


height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))