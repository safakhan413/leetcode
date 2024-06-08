from itertools import groupby
from itertools import accumulate

def smallerNumbersThanCurrent(nums):
    # Sort the numbers while keeping their original indices
    # sorted_nums = sorted((num, i) for i, num in enumerate(nums))
    # print(sorted_nums)
    # # print(list(groupby(sorted_nums, key=lambda x: x[0])))
    
    # # Initialize a list to store the result
    # result = [0] * len(nums)
    
    # # Variable to keep track of the count of numbers before the current number
    # count = 0
    
    # # Group by value in the sorted list
    # for num, group in groupby(sorted_nums, key=lambda x: x[0]):
    #     print('im groot', list(group))
    #     # Get all indices that have the current num
    #     indices = [x[1] for x in group]
        
    #     print('im indices', indices)

    #     # Assign the count to the result for all indices of the current num
    #     for index in indices:
    #         result[index] = count
        
    #     # Update the count to include the current group size
    #     count += len(indices)
    
    # return result
    result = [0] * len(nums)
    sorted_with_indexes = sorted((num,i) for i, num in enumerate(nums))
    print(sorted_with_indexes) 
    grp = groupby(sorted_with_indexes, key = lambda x: x[0])
    dict1 = {}
    acc = 0
    for k,group in grp:
        group_list = list(group)
        print(k, group_list, len(group_list))

        for num, index in group_list:
            result[index] = acc
            print('index, result[index], acc',index,  result[index], acc)
        acc += len(group_list)
    
    return result

# Example usage
nums = [8, 1, 2, 2, 3]
print(smallerNumbersThanCurrent(nums))  # Output: [4, 0, 1, 1, 3]