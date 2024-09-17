# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [2,3,0,1,4]
# Output: 2

def min_jumps(nums):
    n = len(nums)
    if n == 1:  # If there's only one element, no jumps are needed.
        return 0

    jumps = 0  # Number of jumps taken
    reach = 0  # The farthest point we can currently reach
    current_end = 0  # The farthest point we can reach with the current jump

    for i in range(n - 1):  # Loop through each element, except the last one
        reach = max(reach, i + nums[i])  # Update the farthest reach
        
        # When we reach the current jump's end, we must make another jump
        if i == current_end:
            jumps += 1
            current_end = reach  # Extend the jump range
            
            # If we can reach or exceed the last index, we are done
            if current_end >= n - 1:
                return jumps

    return jumps
