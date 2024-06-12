"""
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""
def lengthOfLongestSubstring(s):
    # dict1 = {}
    # newS = ""
    # for i in s:
    #     dict1[i] = dict1.get(i,0)+1
    #     if i in dict1.keys():

    #     newS = 

    # for i in range(len(s)-1):
    #     for j in range(i+1, len(s)):
    #         print(s[i],s[j])
    # dict1 = {}
    # maxlen = 0
    # newS=""
    # for i in s:
    #     if i not in dict1:
    #         newS = newS+i
    #         dict1[i] = dict1.get(i,0)+1
    #     else:
    #         print(newS)
            
    #         if len(newS) > maxlen:
    #             maxlen = len(newS)
    #             newS=""
    #             # dict1={}
    # print(maxlen)

#may be use while loop instead
    # i=0
    # while i < len(s):
    #     if s[i] not in dict1:
    #         newS = newS+s[i]
    #         print(newS, dict1, 'first if')
    #         dict1[s[i]] = dict1.get(s[i],0)+1
    #         i = i+1
    #         if len(newS) > maxlen:
    #             maxlen = len(newS)
    #             newS=""
    #     else:
    #         i = i + 1
    #         dict1= {}
    #         print(newS)
 
        
    # print(maxlen)
    # dict1 = {}
    # maxlen = 0
    # newS = ""
    
    # i = 0
    # j = 0

    # while j < len(s):
    #     if s[j] not in dict1:
    #         newS += s[j]
    #         dict1[s[j]] = j
    #         print(dict1)
    #         j += 1
    #         maxlen = max(maxlen, len(newS))
    #     else:
    #         # When a repeating character is found, remove characters until the duplicate is removed
    #         i = dict1[s[j]] + 1
    #         newS = s[i:j]
    #         dict1 = {char: idx for idx, char in enumerate(newS, start=i)}
    #         j += 1
    
    # print(maxlen)
    # return maxlen
    # charSet = set()
    # res, l = 0, 0
    

    # for r in range(len(s)):
    #     while s[r] in charSet:
    #         # print(s[r], r,s[l], charSet, 'inside while')
    #         charSet.remove(s[l])
    #         print(s[r], r,l,s[l], charSet, 'inside while')

    #         l += 1
    #     charSet.add(s[r])
    #     res = max(res, r - l + 1)
    #     print(charSet,r, l, res, 'outside while loop')

    # return res

    n = len(s)
    char_set = set()
    maxlen = 0
    left = 0
    
    for right in range(n):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
            print(f"After removing: left={left}, right={right}, char_set={char_set}")
        
        char_set.add(s[right])
        maxlen = max(maxlen, right - left + 1)
        print(f"After adding: left={left}, right={right}, char_set={char_set}, maxlen={maxlen}")
    
    print(f"Final maxlen: {maxlen}")
    return maxlen

s = "abcabcbb"
# s = "pwwkew"
    
l1 = lengthOfLongestSubstring(s)
print(l1)