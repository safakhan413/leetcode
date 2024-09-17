# There is an array, named `digits`, consisting of N digits. Choose at most three digits (not necessarily adjacent) and merge them into a new integer without changing the order of the digits. What is the biggest number that can be obtained this way?

# Write a function:

# def solution(digits)

# that, given an array of N digits, returns the biggest number that can be built.

# Examples:

# Given digits = [7, 2, 3, 3, 4, 9], the function should return 749.
# Given digits = [0, 0, 5, 7], the function should return 57.
# Assume that:

# N is an integer within the range [3..50];
# each element of array, named `digits`, is an integer within the range [0..9].
# In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
from collections import deque


# def process_vals(max_list):
#     max_values[3].append(digit)
#     max_values[3].sort(reverse=True)
#     if len(max_values[3]) >3:
#         max_values[3].pop()

def solution(A):
    '''
    Algo:
        find largest integer without canging order of inetgers. AT most 3 digits.


    '''
    # stack = deque()
    # ## assumption that all integers are greater than 0
    # dig_to_add = 0
    # for i in A:
    #     if i > dig_to_add:
    #         dig_to_add = i
    #         deque.append(i)
    ## find 3 max values and check their indices, place them in same order and then get the final value
    # max_dict = {}
    # max_num = 0
    # for i, val in enumerate(A):
    #     max_num = max(max_num,val)

    # max1 = max(A)
    # A.remove(max1)
    # print(max1,A)
      
    # n = len(A)

    # max_num = 0

    # for i in range(n):
    #     max_num = max(max_num, A[i])

    # for i in range(n):
    #     for j in range(i+1, n):
    #         num = A[i]*10 + A[j]
    #         max_num = max(max_num, num)
    # for i in range(n):
    #     for j in range(i+1, n):
    #         for k in range(j+1, n):
    #             num = A[i]*100 + A[j] *10 + A[k]
    #             max_num = max(max_num, num)
    # return max_num



  n = len(A)

  max_num = 0

  for i in range(n):
      max_num = max(max_num, A[i])

  for i in range(n):
      for j in range(i+1, n):
          num = A[i]*10 + A[j]
          max_num = max(max_num, num)
          
  for i in range(n):
      for j in range(i+1, n):
          for k in range(j+1, n):
              num = A[i]*100 + A[j] *10 + A[k]
              max_num = max(max_num, num)
  return max_num
  
  #return 0



digits = [7, 2, 3, 3, 4, 9]
# digits = [0, 0, 5, 7]
print(solution(digits))