from itertools import combinations
import math

def threeSumClosest(nums, target):
    '''
    Algo:
    - inputs are nums and target. Find 3 ints in nums 
    - output:return the sum that is closest to target
    Steps:
        1st attempt:
        step1: make a set of 3 from list. Use combinations from itertools
        2. use a for loop to sum each combination 
        3. take an absolute abs
        4. initialize mindiff as +inf
        5. if abs is less than mindif then set mindiff to abs
        6. keep doing for all and return mindiff eventually


    '''
    # print("hi i'm here")
    # print(nums)
    # minDiff = math.inf
    # comb = combinations(nums,3)
    # minSum = -math.inf
    # # print(list(comb))
    # for i in list(comb):
    #     print("why not here")
    #     newSum = sum(i)
    #     print(i,newSum)
    #     newdiff = abs(target-newSum)
    #     print('im new diff:', newdiff)
    #     if newdiff < minDiff:
    #         minDiff = newdiff
    #         minSum = newSum
    # print('min sum is: ',minSum )
    # return minSum
    s=float('inf')
    t=len(nums)
    nums.sort()
    for x in range(t-2):
        i=x+1
        j=t-1
        # print(nums)
        while i<j:
            s1=nums[x]+nums[i]+nums[j]
            # print(x,i,j,'here')
            if s1==target:
                return target
            if abs(target-s)>abs(target-s1):
                # print('im s1', abs(target-s), abs(target-s1))

                #print(x,i,j,'-------',s1)
                s=s1 ##to find lowest sum
            # print('final s1', s1)
            #since its a sorted ARRAY, IF S1 < target that means the calculated minsum is greater than target and so left ptr needs to advance to include bigger values, reverse holds in else condition
            if s1<target:
                i+=1
            else:
                j-=1
    return s


nums = [-1,2,1,-4]
target = 1


threeSumClosest(nums, target)

# minDiff = math.inf
#         comb = combinations(nums,3)
#         minSum = -math.inf
#         for i in list(comb):
#             newSum = sum(i)
#             newdiff = abs(target-newSum)
#             if newdiff < minDiff:
#                 minDiff = newdiff
#                 minSum = newSum
#         return minSum