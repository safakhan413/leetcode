# Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

# Example 1:

# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
# Example 2:

# Input: nums = [1,2,3], k = 0
# Output: 0
 
def numSubarrayProductLessThanK(nums, k):
    # import math
    # print(nums,k)
    # if k == 0 or k < min(nums):
    #     return 0
    # prod = 1
    # res = []
    # # while prod < k:
    #     # initarr = []
    # count = 0
    
    # for i in range(len(nums)):
    #     initarr = []

    #     for j in range(i+1, len(nums)+1):
    #         print(i,j, nums[i:j])
    #         if math.prod(nums[i:j]) <k:
    #             count +=1
    #             # res.append(nums[i:j])
    #             # print('res', res)
    #         # print()
    # return count
    if k <= 1:
        return 0
    prod = 1
    count = 0
    left = 0
    for right in range(len(nums)):
        prod *= nums[right]
        while prod >= k and left <= right:
            prod /= nums[left]
            left += 1
        count += right - left + 1
    return count
    # import math
    # res = math.comb([])
    # pass

nums,k = [10,5,2,6], 100
print(numSubarrayProductLessThanK(nums, k))