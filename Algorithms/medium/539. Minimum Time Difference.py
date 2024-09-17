# Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
 

# Example 1:

# Input: timePoints = ["23:59","00:00"]
# Output: 1
# Example 2:

# Input: timePoints = ["00:00","23:59","00:00"]
# Output: 0
 

# Constraints:

# 2 <= timePoints.length <= 2 * 104
# timePoints[i] is in the format "HH:MM".
from datetime import datetime
import math 


# def convert_mins(time):
#     time_in_mins = 

def findMinDifference(timePoints):
    print(timePoints)
    minutes = []
    for time in timePoints:
        h,m = map(int, time.split(':'))
        minutes_t = h*60+m
        minutes.append(minutes_t)

    minutes.sort()
    print(minutes)
    min_diff = math.inf
    for i in range(1,len(timePoints)):

        min_diff = min(min_diff, abs(minutes[i] - minutes[i-1]),1440-minutes[-1] + minutes[0]  )
        print(min_diff)


# timePoints = ["23:59","00:00"]

timePoints = ["00:00","23:59","00:00"]
findMinDifference(timePoints)