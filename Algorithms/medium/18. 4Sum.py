"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]


"""

def fourSum( nums, target):
    nums = sorted(nums)
    res = []
    
    # for i, a in enumerate(nums):
    #     for

    if len(nums) < 4:
        return 'not found'
    # if len

    for i in range(len(nums)-3):
        if i>0 and nums[i] == nums[i-1]:
            continue
        a = nums[i]
        print('im a', a)
        for j in range(i+1, len(nums)-2):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            b = nums[j]
            print('im b', b)
            
            l,r = j+1, len(nums)-1
            while l < r:

                fourSum = a+b+nums[l]+nums[r]

                if fourSum > target:
                    r = r-1
                elif fourSum < target:
                    l = l+1
                else:
                    # res.append([a,b,nums[l], nums[r]])

                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
    return res

# def fourSum(nums, target):
#     nums.sort()
#     res = []

#     for i in range(len(nums) - 3):
#         if i > 0 and nums[i] == nums[i - 1]:
#             continue
#         for j in range(i + 1, len(nums) - 2):
#             if j > i + 1 and nums[j] == nums[j - 1]:
#                 continue
#             l, r = j + 1, len(nums) - 1
#             while l < r:
#                 four_sum = nums[i] + nums[j] + nums[l] + nums[r]
#                 if four_sum < target:
#                     l += 1
#                 elif four_sum > target:
#                     r -= 1
#                 else:
#                     res.append([nums[i], nums[j], nums[l], nums[r]])
#                     while l < r and nums[l] == nums[l + 1]:
#                         l += 1
#                     while l < r and nums[r] == nums[r - 1]:
#                         r -= 1
#                     l += 1
#                     r -= 1

#     return res
    


    """
    
    """


# nums = [1,0,-1,0,-2,2]
# target = 0

nums = [2,2,2,2]
target = 8

resultant = fourSum(nums, target)

print(resultant)