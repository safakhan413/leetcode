# 55. Jump Game
# Medium
# Topics
# Companies
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
# 
# 
def canJump(nums):
    '''
    Algo:
    
    Objective: see if len(nums) - 1 can be reached, return true if you can reach last, false otherwise

    Steps:
        start with first index
    
    '''
    # js is short for jumpstart

    # js = nums[0]
    # jump = 0
    # i = 0
    # while i in range(0,js):
    #     i=i + js
    #     if nums[i] > jump:
    #         jump = max(jump, nums[i])
    #         js = jump
    #     # if 
    #     print(i, jump, 'im js', js)

    max_reach = 0  # Initialize the furthest reachable index
    for i in range(len(nums)):
        if i > max_reach:
            print('compared i and max_reach', i, max_reach)
            # Current index is not reachable
            return False
        # Update the furthest reachable index
        max_reach = max(max_reach, i + nums[i])
        # Debugging output to trace computation values
        print(f"Index: {i}, Num: {nums[i]}, Max Reach: {max_reach}")
        if max_reach >= len(nums) - 1:
            print('see last ind reachable', max_reach)

            # Can reach or pass the last index
            return True
    # After iterating, check if the last index is reachable
    return max_reach >= len(nums) - 1


        # nextInd = js+i
    # i=1
    # while i in range(1,11):
    #     print("Hello world", i)
        


        # js = numsjs + i
        # jump = 
        # maxJ = max(jump, )
    print(nums)

# nums = [2,3,1,1,4]
nums = [3,2,1,0,4]
canJump(nums)