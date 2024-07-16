"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?

"""

def isSubsequence( s, t):
    # slen = len(s)
    # tlen = len(t)
    # print(s,t,slen,tlen)

    # if slen ==0:
    #     return True
    # if tlen ==0 and slen >0:
    #     return False
    # '''
    # out: bool True if subsequence s is in string t
    # rule1: each letter in s needs to be in t
    # rule 2: sequence should be maintained s.t. each subsequent letter in s should be increasing index in t
    # if both conditions are met then its a subsequence return true else return false
    # '''
  


    # retBool = False
    # ind = 0
    # tdict ={ i: t1 for i,t1 in enumerate(t) }
    # print(tdict, 'ts dictionary')
    # for i in s:
    #     if i in t:
    #         nind = t.find(i)
    #         # nind = tdict
    #         if nind >= ind:
    #             print(ind, nind, 'in true block')
    #             ind = nind
    #             retBool = True
    #         else:
    #             print('why here', nind, ind,i)
    #             retBool = False
    #             break

    #     else:
    #         print('come')
    #         retBool = False
    #         break
    #         print(retBool)
    # # print(ret)        
    # return retBool
    sind, tind = 0,0

    while sind <len(s) and tind <(len(t)):
        # print(s,t,s[sind] , t[tind])

        #check if current characters match
        if s[sind] == t[tind]:
            # print(sind,tind,s[sind] , t[tind],'before inside if')

            # if the characters match then update sind and tind
            sind +=1
            # tind +=1
            # print(sind,tind,s[sind] , t[tind],'after inside if')

        # In any case increment tind
        tind +=1
    return sind == len(s)


# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false

# s = "abc"
# t = "ahbgdc"

# s = "axc"
# t = "ahbgdc"
s ="aaaaaa"
t ="bbaaaa"

ans = isSubsequence( s, t)
print(f'final ans {ans}')
