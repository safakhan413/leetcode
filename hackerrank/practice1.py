# def smallest(arr):
#     '''Algo
#
#     Output: smallest numebr from teh array
#     Input: array of int
#
#     Steps:
#     1. one variable to keep track. min
#     2. compare each elem of array with min.
#     3. If the new elem is smaller than min tehn make it the new min
#     '''
#     small = float('inf')
#     for i in arr:
#         if i < small:
#             small = i
#     # print(small)
#     return small
#
#
# def second_smallest(arr):
#     '''algo
#
#     Output: smallest two numbers
#
#     steps:
#     1. call smallest araa
#     2. find in the
#
#     '''
#     s1 = float('inf')
#     s2 = float('inf')
#
#     for i in arr:
#         if i < s1:
#             s2 = s1
#             s1 = i
#         elif i < s2:
#             s2 = i
#
#     return s2


def third_smallest(arr):
    s1 = float('inf')
    s2 = float('inf')
    s3 = float('inf')
    for i in arr:
        if i < s1:
            s2 = s1
            s1 = i
        elif i < s2:
            s3 = s2
            s2 = i
    return s3


a = [1,2,-9,0,7]

print(third_smallest(a))

#     pass

# def isPrime(N):
#     '''
#     Output: boolean value
#
#     '''
#
#     # if N == 2:
#     #     return True
#
#     for i in range(2, N // 2):
#         if (N % i == 0):
#             return False
#     return True
#     # break
#
#     # N needs n bits, n = log(N), N = 2^n
#     # O(N), O(2^n)
#
#
# a = 49
# print(isPrime(a))