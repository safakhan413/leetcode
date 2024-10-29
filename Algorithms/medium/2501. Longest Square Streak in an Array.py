# You are given an integer array nums. A subsequence of nums is called a square streak if:

# The length of the subsequence is at least 2, and
# after sorting the subsequence, each element (except the first element) is the square of the previous number.
# Return the length of the longest square streak in nums, or return -1 if there is no square streak.

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

# Example 1:

# Input: nums = [4,3,6,16,8,2]
# Output: 3
# Explanation: Choose the subsequence [4,16,2]. After sorting it, it becomes [2,4,16].
# - 4 = 2 * 2.
# - 16 = 4 * 4.
# Therefore, [4,16,2] is a square streak.
# It can be shown that every subsequence of length 4 is not a square streak.
# Example 2:

# Input: nums = [2,3,5,6,7]
# Output: -1
# Explanation: There is no square streak in nums so return -1.
def longestSquareStreak(nums1):
    nums = sorted(nums1)
    nums_set = set(nums)  # For fast lookups
    max_len = 0

    for num in nums:
        if num not in nums_set:
            continue  # Skip if already part of a counted sequence

        length = 1  # Start count from 1 (the number itself)
        current = num
        while current ** 2 in nums_set:
            current = current ** 2
            length += 1
            nums_set.remove(current)  # Remove each square as it's counted

        max_len = max(max_len, length)

    return max_len if max_len > 1 else -1




#     import copy

#     ### for i and afetr sorting see 
#     nums = copy.deepcopy(nums1)
#     nums.sort()
#     ## we need to get longest substreak so that means we need to have a count as well for each i we checjk if its a square of the previous stored one 
#     ## for every i we can have 

#     res = set()
#     maxLen = 0
#     # print(nums)
#     for i in range(len(nums)):
#         # isres = [nums[i]]
#         # print(isres, 'im inres')
#         loclen = 0
#         for j in range(i+1, len(nums)):
#             if nums[j] == nums[i]**2:
#                 res.update([nums[i],nums[j]])
#                 # print('in here',nums[i], nums[j], res)

#                 loclen +=1
        
#         # if loclen > maxLen:
#         #     res.append(isres)
#         #     maxLen = loclen
    
#     # print(res)
#     retRes = [i for i in nums1 if i in res]
#     retRes = set(retRes)
#     lenr = len(retRes)
#     # print(retRes)
#     return lenr if lenr > 0 else -1



############################### other solution ################################




nums = [4,3,6,16,8,2]
# nums = [2,3,5,6,7]
print(longestSquareStreak(nums))