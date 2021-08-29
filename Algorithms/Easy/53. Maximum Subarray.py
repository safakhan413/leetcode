from itertools import chain, combinations, permutations


def maxSubArray(nums):
    '''Algo
    Output: find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
    Input: array of integers
    Steps: 1. 2 for loops to give all sublists

    '''
    dp = []
    dp.append(nums[0])
    current_largest_sum = dp[0]
    for i in range(1,len(nums)):
        # dp.append()
        # print(dp,dp[i-1], nums[i],max(dp[i - 1] + nums[i], nums[i]))
        dp.append(max(dp[i - 1] + nums[i], nums[i]))
        # print('after appending', dp)
        if dp[i] > current_largest_sum:

            current_largest_sum = dp[i]
            # print('current_largest_sum', current_largest_sum)

    return current_largest_sum

    # maxsum = float('-inf')
    # if len(nums) == 1:
    #     return nums[0]
    # for i in range(len(nums)+1):
    #     for j in range(i+1, len(nums)+1):
    #         # print(i,j)
    #         sumItoj = sum(nums[i:j])
    #         # print(sumItoj)
    #         if sumItoj > maxsum:
    #             maxsum = sumItoj
    #         else:
    #             continue
    # # print(maxsum)
    # return maxsum

# nums = [-1]
# nums = [5,4,-1,7,8]
# nums = [-2,-1]
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))