def maxProduct(nums):

    # dp = []
    # dp.append(nums[0])
    # current_largest_product = nums[0]
    # sign_dict = dict()
    # for i in range(1,len(nums)):
    #     print(dp, dp[i - 1], nums[i], max(nums[i] * dp[i-1], nums[i]), nums[i])
    #     if dp[i-1] <0:
    #         sign_dict[i] = '-'
    #     else:
    #         sign_dict = '+'
    #     dp.append( max(nums[i] * dp[i-1], nums[i]))
    #     print('after appending', dp)
    #
    #     if dp[i] > current_largest_product:
    #         current_largest_product = dp[i]
    #         print('current_largest_product', current_largest_product)
    #
    # return  current_largest_product
    positive, negative = nums[0], nums[0]
    result = nums[0]
    for num in nums[1:]:
        positive, negative = max(num, positive * num, negative * num), min(num,
                                                                           positive * num, negative * num)
        result = max(result, positive)
    return result


# nums = [2,3,-2,4]
nums = [-2,3,-4]
print(maxProduct(nums))