"""
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

 

Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
"""

def numRescueBoats(people, limit):
    print(people, limit)
    stp = sorted(people)
    print(stp)

    left = 0
    right = len(people)- 1
    numboats = 0
    while left <= right:
        sum = stp[left] + stp[right]
        if sum >= limit:
            print('vame to >= ', stp[left], stp[right], sum, left, right, numboats)

            numboats +=1
            right -=1
        elif sum < limit:
            left +=1 
    print(numboats)
    return numboats


# people = [3,2,2,1]
# limit = 3

# people = [1,2]
# limit = 3

people = [2,4]
limit = 5

# people = [3,5,3,4]
# limit = 5
numRescueBoats(people, limit)