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
class Solution:
    def mergeSortedArrays(self, nums1, nums2):
        # Initialize pointers for nums1 and nums2
        i, j = 0, 0
        merged = []

        # Merge the two arrays
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        # Append remaining elements from nums1
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1

        # Append remaining elements from nums2
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1

        return merged

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # size_nums1 = len(nums1)
        # size_nums2 = len(nums2)
        # nums1.extend(nums2)
        # print(nums1, size_nums1, size_nums2)

        # r = len(nums1)-1
        # l = 0
        # nums1.insert(1,4)
        # a = nums1.pop(0)
        # print(nums1,a)

        # while l < r:
        #     if nums1[l] < nums1[r]:
        #         l +=1
        #     else: # in case nums[l] >nums[r] then swap
        #         # swap(nums1, l,r)
        #         print(nums1, 'befre swapp')
        #         nums1[l], nums1[r]= nums1[r], nums1[l]
        #         print(nums1, 'after swap')
        #         r -=1
        # ## now we have sorted nums1, what we need to check is size

        # if len(nums1) %2 ==0:
        #     median_indices = [len(nums1)//2-1, len(nums1)//2]
        #     median = (nums1[median_indices[0]] + nums1[median_indices[1]]) /2
        #     return median
        # else:
        #     median = nums1[len(nums1)//2]
        #     print('odd median', median)
        #     return median
        #     print('median indices', median_indices, median)

        merged = self.mergeSortedArrays(nums1, nums2)
    
        # Calculate the size of the merged array
        n = len(merged)
        
        # Find the median
        if n % 2 == 0:
            median = (merged[n // 2 - 1] + merged[n // 2]) / 2
        else:
            median = merged[n // 2]
        
        return median