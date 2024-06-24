"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

"""

def findMedianSortedArrays(nums1, nums2) :
    print(nums1, nums2)
    """
    Algo:

    Information both arrays are sorted so combining them should be easy with one for loop

    buttt size could be m,n so not uniform so potential problems could be related to index

    first combine then get the middle tow elements if size is even otherwise the middle val is median

    

    """


nums1 = [1,3]
nums2 = [2]
median = findMedianSortedArrays(nums1, nums2)
print(median)