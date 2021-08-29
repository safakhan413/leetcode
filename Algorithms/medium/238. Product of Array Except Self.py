def productExceptSelf(nums):
    '''
    Algo:
    Output: return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
    Output: nums array
    Restratints: No division operator and has to be O(n) time
    Steps:
    1. have a new array answers. store the nums[i] value in temp.
    2. before multiplication put 1 in nums[i]
    3. if v ==0
    '''
    product = 1
    prodWith0 = 1
    answer = [None]*len(nums)

    # checkIf0 = nums.index(0) if 0 in list else -1
    try:
        checkIf0 = nums.index(0)
    except ValueError:
        
        checkIf0 = -1
    print(checkIf0)
    # if checkIf0 == -1:
    #     for i, v in enumerate(nums):
    if checkIf0 != -1:
        nums[checkIf0] = 1
    for i, v in enumerate(nums):
        if checkIf0 == -1:
            product = product * v
            prodWith0 = 'False'
        else:
            product = 0
            prodWith0 = prodWith0 * v
    print(product,prodWith0)
        # if v==0:
        #     product = 0
        #     prodWith0 =
        #     # product =
        #
        #     prodWith0 = product * 1
        # else:
        #     product = product * v
    print(product,prodWith0)
    #
    if checkIf0 != -1:
        nums[checkIf0] = 0
    for i in range(0,len(nums)):
        if checkIf0 == -1:
            tuple1 = divmod(product, nums[i])
            answer[i] = tuple1[0]
        else:
            if nums[i] == 0:

                answer[i] = prodWith0
            else:
                answer[i] = product
        # else:
    return answer

# nums = [1, 2, 3, 4]
nums = [-1,1,0,-3,3]
# output = [24,12,8,6]
print(productExceptSelf(nums))
