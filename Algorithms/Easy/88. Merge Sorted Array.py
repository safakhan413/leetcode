# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
# Example 3:

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

def merge(nums1, m, nums2, n):
    """
    Merges nums2 into nums1 in-place, assuming nums1 has enough space at the end 
    to hold the elements of nums2, as indicated by trailing zeroes.
    
    Args:
    nums1 (List[int]): The first sorted list with enough trailing space to hold nums2.
    m (int): The number of initial elements in nums1 that are part of the merge.
    nums2 (List[int]): The second sorted list.
    n (int): The number of elements in nums2 to be merged into nums1.

    Do not return anything, modify nums1 in-place instead.
    """

    # Handle edge cases
    if m == 0:  
        # If nums1 is empty (m == 0), just replace nums1 with nums2
        nums1[:] = nums2
        return
    elif n == 0:
        # If nums2 is empty (n == 0), do nothing and return
        return

    # Pointers to the end of the valid elements in nums1 and nums2
    i = m - 1  # Pointer to the last element in the valid part of nums1
    j = n - 1  # Pointer to the last element in nums2
    k = m + n - 1  # Pointer to the last position in nums1 (end of the array)

    # Merge nums1 and nums2 starting from the end of both arrays
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # If there are remaining elements in nums2, add them to nums1
    # No need to check nums1 as the remaining elements are already in place
    nums1[:j + 1] = nums2[:j + 1]

# Example usage:
nums1, m, nums2, n = [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3
merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]
