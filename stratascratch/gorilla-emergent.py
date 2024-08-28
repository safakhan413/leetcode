def version_compare( version1, version2 ) :
    #### Algo to compare v1 and v2

    # if v1 < v2 output -1
    # v1 == v2 out 0
    # v1> v2 out 1

    # input:
    # v1 and v2 come as strings separated by .
    # they are split as major.minor.patch.build.compilation
    # each f these values can be 1 or 2 digits max is99 

    ### steps:
    '''
    split each v1 and v2 on .
    then for each value in the list compare the values if the first is equal till you find non equal

    to make them equa whichever length is smaller add 0 to rest of teh elements
    
    '''
    l1 = version1.split('.')
    l2 = version2.split('.')
    
    len1, len2 = len(l1),len(l2)
    print(l1,l2, len1, len2)
    
    #equalize lengths to compare if unequal
    if len1 < len2:
        l1 = l1+ ['0']*(len2-len1)
    elif len2 < len1:
        # diff = len2-len1
        l2 = l2+ ['0']*(len1-len2)
    # else:
        ## they are equal lengths
    result = 0
    for i in range(len(l1)):
        if l1[i] == l2[i]:
            # result = ''
            continue
        print(type(l1[i]) ,type(l2[i]))
        if l1[i] > l2[i]:
            result = 1
            return result
        elif l1[i] < l2[i]:
            result = -1
            return result
    return result
        # else:
        #     return 0

    # print('after', l1, len(l1))





# ---------------------------------
# Input parameters: (str("2"), str("2.0"))
# 2 2.0
# Result: (None,)
# Expected: (0,)
# ---------------------------------
# Input parameters: (str("2"), str("2.0.0"))
# 2 2.0.0
# Result: (None,)
# Expected: (0,)
# ---------------------------------
# Input parameters: (str("2"), str("2.0.0.0"))
# 2 2.0.0.0
# Result: (None,)
# Expected: (0,)
# ---------------------------------
# Input parameters: (str("2"), str("2.0.0.0.0"))
# 2 2.0.0.0.0
# Result: (None,)
# Expected: (0,)
# ---------------------------------
# Input parameters: (str("2"), str("2.0.0.0.1"))
# 2 2.0.0.0.1
# Result: (None,)
# Expected: (-1,)
# ---------------------------------
# Input parameters: (str("2"), str("2.1"))
# 2 2.1
# Result: (None,)
# Expected: (-1,)
# ---------------------------------
# Input parameters: (str("2.1.0"), str("2.0.1"))
# 2.1.0 2.0.1
# Result: (None,)
# Expected: (1,)



# v1 = '2.1.0'
# v2 = '2.0.0.0.1'

v1 = '2'
v2 = '2.0.0.0.1'


v1 = '2.0'
v2 = '2.0'
result = version_compare( v1, v2 ) 
print(result)