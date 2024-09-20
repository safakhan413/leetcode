# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
# frequency
#  of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []
 

def combinationSum(candidates, target):
    print(candidates, target)

    combination_list = []

    for i in candidates:
        whole,carry = divmod(target, i)
        print(whole,carry)
        # listComb = []
        if carry == 0:
            listcomb = [i] * whole
            combination_list.append(listcomb)
            print('1st one', i, whole, carry, listcomb)

        else:
            if carry in candidates:
                listcomb = [i] * whole + [carry]
                print('2nd one', i, whole, carry, listcomb)
                combination_list.append(listcomb)
        # combination_list.append(listcomb)
    return combination_list
    
    print(combination_list)
        

candidates = [2,3,6,7]
target = 7


# candidates = [2,3,5]
# target = 8
print(combinationSum(candidates, target))