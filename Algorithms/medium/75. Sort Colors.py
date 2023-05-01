def sortColors(nums):
    # Ducth national flag approach
    # 1. relies on three partitions

    print(nums)
    low, mid, high = 0, 0, len(nums)-1
    while mid <= high:
        if nums[mid] == 0:
            print('im the case where mid is 0, before incrementing low and mid pointers', nums[low], nums[mid], '\n', nums )
            nums[low], nums[mid] = nums[mid], nums[low]
            print('im the case where mid is 0, after incrementing low and mid pointers', nums[low], nums[mid], '\n', nums )
            low += 1
            mid += 1

        elif nums[mid] == 1:
            print('im the case where mid is 1, before incrementing low and mid pointers', nums[mid], '\n', nums )

            mid += 1
        else:
            print('im the case where mid is 2, before incrementing  mid and high pointers', nums[mid], nums[high] ,  '\n', nums)

            nums[mid], nums[high] = nums[high], nums[mid]

            high -= 1
nums = [2,0,2,1,1,0]
sortColors(nums)
