def threesum(nums, target):
    nums.sort()
    print(nums)

    # [-8, -6, 1, 2, 3, 5, 6, 12]
    targetSumArray = []
    currentSum = float('-inf') # 
    for i in range(len(nums)-2):
        
        left = i+1
        right = len(nums) - 1


        while left < right:
            currentSum = nums[i] + nums[left] + nums[right]
        
            if currentSum == target:
                targetSumArray.append([nums[i], nums[left], nums[right]])
                print(currentSum ,left,right)

                left +=1
                right -=1

            elif currentSum > target:
                right -=1
            elif currentSum < target:
                left +=1

    print(targetSumArray)


    

array = [12,3,1,2,5,-6,-8,6]
targetsum = 0

print(threesum(array,targetsum))
## sort the array
## I will get the e;
'''
Algorithm:
Output: Triplets that sum to target 
Input: Array and the target

Steps: I want to the sort the array 
# Left right pointer
'''
