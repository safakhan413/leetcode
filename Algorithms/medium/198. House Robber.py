"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

"""

    # if len(nums) == 0:
    #     return 0
    # if len(nums) ==1:
    #     return nums[0]
    # print(nums)
    # sumEv = 0
    # sumOd = 0
    # for i in range(0,len(nums)):
    #     if i%2==0:
    #         sumEv = sumEv+nums[i]
    #     else:
    #         sumOd = sumOd + nums[i]
    # return max(sumEv, sumOd)

def rob(nums):
    if len(nums) == 0:
        return 0
    if len(nums) ==1:
        return nums[0]
    if len(nums) ==2:
        return max(nums[0], nums[1])
    # steps: to be defined 2 to length//2
    Dadsteps = []
    for i in range(2,len(nums)):
        stepList0 = []
        for j in range(0, len(nums), i):
            stepList0.append(j)
        stepList1 = []
        for k in range(1,len(nums), i ):
            stepList1.append(k)
        Dadsteps.append(stepList0)
        print( 'adding0 above', Dadsteps)
        Dadsteps.append(stepList1)
        print( 'adding1 above', Dadsteps)
    print(Dadsteps)

    sumG = 0
    for a in Dadsteps:
        sumLocal = 0
        for b in a:
            # print(a,b, 'im new abs')
            sumLocal = sumLocal + nums[b]
            if sumLocal > sumG:
                sumG = sumLocal
    print('ims umG', sumG)
    return sumG
    # print(nums)
    # sumEv = 0
    # sumOd = 0
    # dict1 = {}
    # for i in range(0,len(nums)):
    #     dict1[i] = nums[i]
    #     print(dict1)
    
    # j = dict(sorted(dict1.items(), key= lambda item: item[1], reverse=True))
    # print(j, nums, '"im j" with nums')
    # sumG = 0
    # # for x in range(0,len(nums)):
    # #     if 0<x<len(nums)-1 and 
    # # while j.keys():
    # #     print(j.)
    # # prevKey
    # # nextKey 

    # keys = list(my_dict.keys())

    # for i, v in enumerate(keys):
    #     prevKey = keys[i-1] if i > 0 else None
    #     nextKey = keys[i+1] if i< len(keys) -1 else None
    #     if key 

    # for key in j:
    #     print(key)
    #     prevkey = 
    #     if key


    # print(dict1, 'dict1')
    # y = 
    #     if i%2==0:
    #         sumEv = sumEv+nums[i]
    #     else:
    #         sumOd = sumOd + nums[i]
    # return max(sumEv, sumOd)

# nums = [2,7,9,3,1]
# nums = [2,1,1,2]
# nums= [1,2,3,1]
nums = [4,1,2,7,5,3,1]
# nums = [1,1]

sumR = rob(nums)
print(sumR, 'finality')


# x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# y ={k: v for k, v in sorted(x.items(), key=lambda item: item[0])}
# print(y)
# # {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}