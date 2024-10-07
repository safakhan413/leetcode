# 49. Group Anagrams
# Medium
# Topics
# Companies
# Given an array of strings strs, group the 
# anagrams
#  together. You can return the answer in any order.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]

def groupAnagrams(strs) :
    anagrams_dict = {}
    for i in strs:
        k = ''.join(sorted(i))
        # if k not in anagrams_dict.keys():
        anagrams_dict[k] = anagrams_dict.get(k, [])
        anagrams_dict[k].append(i)
    # print(list(anagrams_dict.values()))
    return list(anagrams_dict.values())

strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(strs)

