from collections import Counter
def containsDuplicate(nums):

    ############### 1st solution not so efficient memory and runtime wise
    # dic = Counter(nums)
    # init = 1
    # for k,v in dic.items():
    #     print(k,v)
    #     if v > init:
    #         init = v
    # if init > 1:
    #     return True
    # else: return False
    ############### 2nd solution time limit exceeded ################
  #   '''
  # Step1: go through the loop and put distinct in another array. check the new elem encountered before in teh arry. if yes done.
  #   '''
  #   distArr = list()
  #
  #   for i in nums:
  #       if i not in distArr:
  #           distArr.append(i)
  #       else:
  #           return True
  #   return False
    a = Counter(nums)
    nonDist = [k for k, v in a.items() if v > 1]
    if len(nonDist) > 0:
        return True
    else: return  False
    # print([k for k, v in a.items() if v > 1])

# nums = [1,2,3,1]
nums = [2,14,18,22,22]
val = containsDuplicate(nums)
print(val)