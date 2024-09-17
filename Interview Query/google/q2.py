# You begin with an array filled with N zeros and you want to obtain an array A.

# In one move, you can choose an arbitrary interval and increase all the elements within that interval by 1. For example, you can transform [0, 0, 0, 0, 0] into [0, 1, 1, 1, 0] in a single move. However, you need three moves to obtain [1, 0, 1, 2, 2]. One possible sequence of moves is: [0, 0, 0, 0, 0] → [0, 0, 1, 1, 1] → [0, 0, 1, 2, 2] → [1, 0, 1, 2, 2], where → denotes a single move.

# What is the minimum number of moves needed to obtain A, starting from a zero-filled array?

# Write a function:

# int solution(vector<int> &A);

# that, given an array A of length N, returns as an integer the minimum number of moves needed to transform a zero-filled array into A.

# Examples:

# Given A = [2, 1, 3], the function should return 4. For example, the following sequence of moves leads to the solution: [0, 0, 0] → [1, 1, 1] → [2, 1, 1] → [2, 1, 2] → [2, 1, 3].
# Given A = [2, 2, 0, 0, 1], the function should return 3. The following sequence of moves leads to the solution: [0, 0, 0, 0, 0] → [1, 1, 0, 0, 0] → [2, 2, 0, 0, 0] → [2, 2, 0, 0, 1].
# Given A = [5, 4, 2, 4, 1], the function should return 7. One possible optimal sequence of moves is: [0, 0, 0, 0, 0] → [1, 1, 1, 1, 1] → [2, 2, 2, 2, 1] → [3, 3, 2, 2, 1] → [4, 4, 2, 2, 1] → [5, 4, 2, 2, 1] → [5, 4, 2, 3, 1] → [5, 4, 2, 4, 1].
# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [0..1,000,000,000];
# we guarantee that the answer will not exceed 1,000,000,000.
import sys

def solution(A):
  sys.stderr.write(
      'Tip: Use sys.stderr.write() to write debug messages on the output tab.\n'
  )
  
  '''
  Algorithm:
  out -> num of moves for transofrmation
  input -> all elements are 0 in input array A. Each element's initial state was 0
  OBSERVATION: Since the value is only increasing and not decreasing, minimum number of moves would be the max valeu in the
  array
  
  We are judging locally i.e. we need to see which previosu elements are smaller than the new current element
  that is bigegr as this will gives us a new sequence to change for the moves
  
  so for instance in A = [5, 4, 2, 4, 1], after 2 (idx=3) if you want to change to 4 at index 4, then it will be considered a separate sequence so 2 more moves would be required after 5 moves to change the first element. 
  Basically the smaller elements are what break the sequences apart.
  
  '''
  n = len(A)

  if n==0:
      return 0

  moves = 0

  prev = 0

  for current in A:
      #print(f'current: {current}, prev: {prev}')
      if current > prev:
          #print(f'current: {current}, prev: {prev}, moves: {moves}')
          moves += (current-prev)
      prev = current

  return moves