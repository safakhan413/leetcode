from itertools import accumulate, permutations, combinations
from collections import deque

def maxProfit( prices):
    # print(list(accumulate(prices, max)))
    # get the ascending list. In the next values find max
    # ascList = list(accumulate(prices, max))
    # print(ascList)
    '''
    Algo
    output: profit such as diff between early value - later value is maximized
    input: prices list of stocks
    Sol.
    Step1: fix diff values in the list and find accumulate max
    Step2. For all of the lists get first value and the last value of resultant lists
    step3: keep track of max
    step 4 return max
    '''
######################### One cumbersome solution ##############################
    # maxProf = 0
    # for i in range(len(prices)):
    #     newList = list(accumulate(prices[i:len(prices)], max))
    #     print(len(newList))
    #     minOf = newList[0]
    #     maxOf = newList[len(newList) - 1]
    #     diff = maxOf - minOf
    #     if diff > maxProf: maxProf = diff
    #     print(newList)
    # print(maxProf)
    # return maxProf
################################################ one other solution time limit exceeded ##################################
    # min(prices)
#    find first element that is smaller than elements on the left
    '''Algo:
    Step1: 2 for loops:
    if item[i]- item[j] < 0 copntinue
    otherwise keep track of max 
    # '''
    # max = 0
    # for i in range(0, len(prices)):
    #     for j in range(i+1, len(prices)):
    #         if prices[j] - prices[i] < 0: #
    #             continue
    #         else:
    #             diff = prices[j] - prices[i]
    #             if diff > max:
    #                 max = diff
    # print(max)
    # return max
            # print(prices[i], prices[j])

##################### Last solution #######################################
    buy = prices[0]
    mx_profit = 0

    for i in range(1, len(prices)):
        profit = prices[i] - buy

        if profit > mx_profit:
            mx_profit = profit
        if buy > prices[i]:
            buy = prices[i]

    return mx_profit



# prices = [1,2]
prices = [7,9,1,5,3,6,4]
p = maxProfit(prices)
print(p)