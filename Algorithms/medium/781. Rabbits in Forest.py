"""
There is a forest with an unknown number of rabbits. We asked n rabbits "How many rabbits have the same color as you?"
 and collected the answers in an integer array answers where answers[i] is the answer of the ith rabbit.

Given the array answers, return the minimum number of rabbits that could be in the forest.

 

Example 1:

Input: answers = [1,1,2]
Output: 5
Explanation:
The two rabbits that answered "1" could both be the same color, say red.
The rabbit that answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.
Example 2:

Input: answers = [10,10,10]
Output: 11


"""
from collections import Counter
def numRabbits(answers):
    print(answers)
    """
    Out: minimum number of rabbits that could be in teh forest
    input: answers that you got from rabbits of which color they are
    algo:
    step1:
    rule 1. if two answers are same then those rabbits are same colors and they are talking of each other so whatever they are saying add 1 to it for the rabbit who is speaking
    rule 2. if there are unique numbers add those +1 for the speaking rabbit because that rabbit is speaking about rabbits that havent been questioned
     
    #    could be the same colors so consider them 2 rabbits (number of times answered), min could be answer.length and we add from there, if answers are different then add those answers as whole otherwise skip,
    
    """

#     et’s calculate each step for [2,2,2,2,4,3]:

# For key = 2:

# Group Size: 2 + 1 = 3
# Frequency: 4
# Number of Groups Needed: ceil(4 / 3) = 2
# Rabbits Needed: 3 * 2 = 6
# python
# Copy code
# res += (2 + 1) * ceil(4 / (2 + 1))  # res += 3 * 2
# # res = 6
# For key = 4:

# Group Size: 4 + 1 = 5
# Frequency: 1
# Number of Groups Needed: ceil(1 / 5) = 1
# Rabbits Needed: 5 * 1 = 5
# python
# Copy code
# res += (4 + 1) * ceil(1 / (4 + 1))  # res += 5 * 1
# # res = 6 + 5 = 11
# For key = 3:

# Group Size: 3 + 1 = 4
# Frequency: 1
# Number of Groups Needed: ceil(1 / 4) = 1
# Rabbits Needed: 4 * 1 = 4
# python
# Copy code
# res += (3 + 1) * ceil(1 / (3 + 1))  # res += 4 * 1
# # res = 11 + 4 = 15
# 4. Return the Result
# python
# Copy code
# return res  # The total minimum number of rabbits
# # res = 15
# The function returns 15, which is the minimum number of rabbits that satisfies all the given answers.

# Visual Representation
# Here’s a visual table summarizing the calculations:

# Answer	Group Size	Frequency	Number of Groups	Total Rabbits Needed
# 2	3	4	2	6
# 4	5	1	1	5
# 3	4	1	1	4
# Total	-	-	-	15
# Why This Approach Works
# Group Calculation:

# If a rabbit says "2", they expect a total of 2 + 1 = 3 rabbits of the same color. We must ensure we have complete groups, so we use ceil to handle any remainder.
# Handling Remainders:

# Using ceil(value / (key + 1)) ensures that even if there are leftover rabbits, they are included in an extra group.
# Summing Up Rabbits:

# For each answer, the number of required rabbits is the number of groups multiplied by the group size. This approach covers all possibilities and ensures the minimum count.
# Alternative Simple Solution
# Here is a more simplified alternative solution without ceil, but it’s generally less readable and involves integer operations:

# python
# Copy code
# from typing import List
# from collections import Counter

# class Solution:
#     def numRabbits(self, answers: List[int]) -> int:
#         count = Counter(answers)  # Count occurrences of each answer
#         res = 0  # Initialize the result variable to accumulate the total number of rabbits
        
#         for key, value in count.items():
#             group_size = key + 1  # The size of each group for the current answer
#             num_groups = (value + group_size - 1) // group_size  # Integer division to round up
#             res += num_groups * group_size  # Add the total number of rabbits for this answer
            
#         return res  # Return the total minimum number of rabbits
# Why This Alternative Works
# Rounding Up Without ceil:
# (value + group_size - 1) // group_size achieves the same rounding-up effect as ceil(value / group_size).
# This method is a bit more manual but avoids importing math.ceil.
# Dry Run of the Alternative Solution
# Using the same example [2, 2, 2, 2, 4, 3]:

# Count Occurrences:

# {2: 4, 4: 1, 3: 1}
# Calculate Rabbits:

# For key = 2, group_size = 3:
# num_groups = (4 + 3 - 1) // 3 = 6 // 3 = 2
# rabbits_needed = 2 * 3 = 6
# For key = 4, group_size = 5:
# num_groups = (1 + 5 - 1) // 5 = 5 // 5 = 1
# rabbits_needed = 1 * 5 = 5
# For key = 3, group_size = 4:
# num_groups = (1 + 4 - 1) // 4 = 4 // 4 = 1
# rabbits_needed = 1 * 4 = 4
# Total rabbits needed: 6 + 5 + 4 = 15
    import math
    maps = Counter(answers)
    res = 0
    for key,value in maps.items():
        res+=(key+1)*math.ceil(value/(key+1))
    return res

        # elif count[]

    print(minRabbits)
    return minRabbits
    # for i in answers:
    #     if i in anset:


# answers = [1,1,2]

answers =[1,0,1,0,0]

min_r = numRabbits(answers)
print(min_r, 'min rabbits')