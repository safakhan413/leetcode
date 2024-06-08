"""Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
 

Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false
 """
from collections import deque



def rotateString( s, goal):
    print(s,goal)
    # splitStr = s.split("")
    goalsChar = deque(goal)
    x = deque(s)
    rotated = 0
    for i in range(len(s)):
        x.rotate(-1)
        rotated +=1
        print('out',list(x))
        if list(x) == list(goalsChar):
            # rotated +=1
            print('in',list(x))

            print(rotated)
            return True
    return False
        
        # print(i)

    # x.rotate(-1)
    # print(list(x), splitStr)


# s="abcde"
# goal = "cdeab"

s = "abcde"
goal = "abced"

boolval = rotateString(s,goal)
print(boolval)