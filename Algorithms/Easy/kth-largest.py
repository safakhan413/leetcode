# import heapq

# def find_largest_elements_heap(nums, k):
#     # Create a min-heap with the first k elements
#     min_heap = nums[:k]
#     heapq.heapify(min_heap)
    
#     # Iterate through the remaining elements
#     for num in nums[k:]:
#         if num > min_heap[0]:
#             heapq.heappop(min_heap)
#             heapq.heappush(min_heap, num)
    
#     # The min-heap now contains the k largest elements
#     return sorted(min_heap, reverse=True)

# # Example usage
# nums = [3, 2, 1, 5, 6, 4]
# k = 3
# print(find_largest_elements_heap(nums, k))  # Output: [6, 5, 4]

def find_largest_elements(nums, k):
    # Initialize three variables to hold the largest, second largest, and third largest values
    first = second = third = float('-inf')

    for num in nums:
        if num > first:
            third = second
            second = first
            first = num
        elif num > second:
            third = second
            second = num
        elif num > third:
            third = num

    # return [first, second, third][:k]
    return [first, second, third]


# Example usage
nums = [3, 2, 1, 5, 6, 4]
k = 3
print(find_largest_elements(nums, k))  # Output: [6, 5, 4]
