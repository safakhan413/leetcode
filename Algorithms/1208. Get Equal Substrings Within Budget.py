def equalSubstring( s, t, maxCost):
    print(s,t,maxCost)
    # print(ord(s)-ord(t))
    # for i in s and j in t:
    #     print(i,j)
    # a = [ord(i)-ord(j) for i in s for j in t ]
    # print(a)
    # a = []
    maxLen = 0
    # for i in s:
    #     for j in t:
    #         a.append(ord(i)-ord(j))
    for i in range(0, len(s)):
        # a.append(ord(s[i])- ord(t[i]))
        cost = ord(s[i])- ord(t[i])
        # diff = maxCost + cost
        print(cost, maxCost)
        if maxCost >= 0 and maxCost >= -1 * cost:
            maxCost = maxCost + cost 
            maxLen += 1 
        else:
            break    
    print( maxLen)
    return maxLen


if __name__=='__main__':
    # s = 'abcd'
    # t = 'bcdf'
    s = 'abcd'
    t = 'cdef'
    maxCost = 3
    equalSubstring(s,t,maxCost)

    # print('in main main block')