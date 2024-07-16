"""
Given an integer array nums, return the length of the longest strictly increasing 
subsequence
.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

"""

def lengthOfLIS(nums):
    # """
    # Output:Given a list of nums give max LENGTH (longest) of increasing subsequnece
    # Lets do bruteforce first:
    # get all possible increasing subsequences in an array as tuples
    # find the max length of the tuple
    # input: Array of nums

    # Steps:
    # For each elem in nums, 
    # find max len subsequence
    # check an inreasing subsequence and add it to another list

    
    # """
    # print(nums)
    # if len(nums) == 1:
    #     return 1
    # lis = []
    # for i, num in enumerate(nums):
    #     lise = []
    #     lise.append(nums[i])
    #     print( 'im next i and num[i] \n  \n',i, nums[i])
    #     for j in range(i, len(nums)):
    #         print(nums[i], nums[j])
    #         # if lise[-1] > nums[j] and nums[j] > nums[i]: # i.e. the last added j or last element is bigger than the next jth element then remove it and put smaller elemnt instead
    #         #     print('i came here')

    #         #     lise.remove(lise[-1])
    #         #     lise.append(nums[j])
    #         lastind = -1
    #         while lise[lastind] > nums[j] and nums[j] > nums[i]:
    #             print('im lise-1',lise[lastind], nums[j], lise[lastind] > nums[j], nums[j] > nums[i], lise)

    #             lise.remove(lise[lastind])

    #             lastind -=1
    #             lise.append(nums[j])
    #             print('im removed', lise)
    #             continue
    #         if nums[j]> lise[-1]:
    #             print('im when j is bigger than i', nums[j], nums[i])

    #             lise.append(nums[j])
    #             print("new lise", lise)
    #         # elif 
    #     lis.append(lise)
    #     print(lis, 'final list')
    #     maxLen1 = len(max(lis, key= lambda x: len(x)))
    #     print(f'max len {maxLen1}')
    # return maxLen1
        # return maxLen
        # return max(lis, key= lambda x: len(x))

    #     print(i,num)
    #     a = i
    #     j = i +1
    #     # LISE = []
    #     # LISE
    #     if j < len(nums):
    #        LISE = []
    #        LISE.append(num)
    #        print(nums[a] , nums[j], 'im a and j')
    #        if nums[a] < nums[j]:
    #            LISE.append(nums[j])
    #            a = j
    #            j += 1
    #     LIS.append(LISE)
    # print(LIS)


        # LIS.

                
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         # pass
    #         # check if 
    if not nums:
        return 0

    # Create dp array with all elements initialized to 1
    dp = [1] * len(nums)
    max_len = 1  # At least one number in the sequence

    # Loop through each number in the array
    for i in range(len(nums)):
        # Compare with all previous numbers
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
                max_len = max(max_len, dp[i])
                
    return max_len
        
nums = [10,9,2,5,3,7,101,18]
# nums = [0,1,0,3,2,3]
# lengthOfLIS(nums)
maxlen = lengthOfLIS(nums)
print(maxlen, 'im ,max len')
