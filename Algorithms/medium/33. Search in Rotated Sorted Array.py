# """There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) 
# such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1
# """

def find_rotation_index(arr):
    low, high = 0, len(arr) - 1

    # If the array is not rotated at all
    if arr[low] <= arr[high]:
        return 0

    while low <= high:
        mid = (low + high) // 2
        print('we are the mids', mid)

        # Check if mid is the pivot
        if mid < high and arr[mid] > arr[mid + 1]:
            return mid + 1
        if mid > low and arr[mid] < arr[mid - 1]: # for instance mid has 0 and mid-1 is 7 then return mid
            return mid

        # Determine which half is sorted
        if arr[low] <= arr[mid]: # in our example if 4 is less than 7 
            print('low', low)
            low = mid + 1

        else:
            high = mid - 1
            print('high', high)


    return -1  # This line should not be reached if the input array is rotated

def binarySearch(nums, target):
    print(nums,target)

    if len(nums) ==0:
        return -1
    # print(len(nums)
    if len(nums) ==1: 
        if nums[0]== target:
            print('whby not sucess')
            return 0
        else:
            return -1

    
    # else: 

    #     return -1



    low, high = 0, len(nums)-1
    while low <= high:
        mid = (low+high)//2

        if nums[mid] == target:
            return mid
        elif  nums[mid] >= target: # if mid element is greater than target then target should be in the left half
            high = mid-1
            # print('im high', high)
        elif  nums[mid] <= target:
            low = mid+1
            # print('im low',mid,  low)

    else: 
        return -1





def search( nums, target):
    """
    input: a sorted array nums rotated along an unknown index, target
    output: index of target on O(logn)
    
    Algo:
    choose a mid with lenarray//2 e.g. if 4 then element at 2, if 5 then also 2 so floor math.floor

    if target is found i.e. mid == target, 
    return index
    ## see if target is greater than mid abd if next element of mid is also grater than mid then go right
    else if target > elem[mid] and value[mid + 1] > elelm[mid]:
        then nums 


    """

    x= find_rotation_index(nums)
    print('rotation index', x)

    y = binarySearch(nums[x:], target)
    print('im y', y)
    if y != -1:
        return y+x
    else:
        return binarySearch(nums[:x], target)
    # print(nums[x:]+nums[:x])
    # sorted_array = nums[x:]
    # if len(nums) == 1 and nums[0] :
    #     nums[0] ==


nums = [4,5,6,7,0,1,2]
target = 5
a = search(nums, target)
print(a)


# def binary_search(array, target):
#     lower = 0
#     upper = len(array)
#     while lower < upper:   # use < instead of <=
#         x = lower + (upper - lower) // 2
#         val = array[x]
#         if target == val:
#             return x
#         elif target > val:
#             if lower == x:   # these two are the actual lines
#                 break        # you're looking for
#             lower = x
#         elif target < val:
#             upper = x



# l = [4,5,6,7,0,1,2]
# c = binary_search(l,0)
# print(c)

# def findPointRotation(l):
#     print(l)
#     low = 0
#     high = len(l)-1

#     mid = (high+low)//2

#     if l[mid] > l[mid+1]:
#         pointR = mid + 1
#     elif l[mid] < l[mid+1]:

#     print(mid, l[mid])

# l = [4,5,6,7,0,1,2]
# findPointRotation(l)

# def find_rotation_index(arr):
#     low, high = 0, len(arr) - 1

#     # If the array is not rotated at all
#     if arr[low] <= arr[high]:
#         return 0

#     while low <= high:
#         mid = (low + high) // 2
#         print('we are the mids', mid)

#         # Check if mid is the pivot
#         if mid < high and arr[mid] > arr[mid + 1]:
#             return mid + 1
#         if mid > low and arr[mid] < arr[mid - 1]: # for instance mid has 0 and mid-1 is 7 then return mid
#             return mid

#         # Determine which half is sorted
#         if arr[low] <= arr[mid]: # in our example if 4 is less than 7 
#             print('low', low)
#             low = mid + 1

#         else:
#             high = mid - 1
#             print('high', high)


#     return -1  # This line should not be reached if the input array is rotated

# # Example usage
# arr = [4, 5, 6, 7, 8, 0, 1, 2]
# rotation_index = find_rotation_index(arr)
# print(f"The array was rotated at index: {rotation_index}")


