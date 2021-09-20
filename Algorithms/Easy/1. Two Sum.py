def twoSum(nums, target):
    '''

    :param nums:
    :param target:
    :return:
    Algo:

    Output: return indices of two int that add up to target
    Input: list of numbers,  a target value
    Algo:
    1. target - all values then find that value
    2. use dictionary to find the value

    '''
############################# easiest brute force solution ###########################
    # for i in range(0, len(nums)):
    #     for j in range (i+1, len(nums)+1):
    #         if nums[i] + nums[j] == target:
    #             return [i,j]
    # return None
################################# Solution with dictionary #####################################################
    dic = {}
    for i in range(len(nums)):
        if target - nums[i] in dic.keys():
            return [i, dic[target - nums[i]]]
        dic[nums[i]] = i


# nums = [2,7,11,15]
# target = 9
nums = [3,3]
target = 6
(twoSum(nums, target))