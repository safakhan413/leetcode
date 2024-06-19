def wordPattern( pattern, s):
    print(pattern,s)
    a = [char for char in pattern]
    b = s.split()
    set1 = set(a)
    set2 = set(b)
    ## check if there is one on one mapping, if not return false
    # for i in set1:
    print(set1, set2)
    if len(set1) != len(set2):
        return False
    elif (len(b) != len(a)):
        return False
    else:

        # now we have to check that there in only 1-1 mapping in string
        # return True
        # for i in pattern:
        #     for j in s.split():
        #         print(i,j)
        dict1 = {}
        for i in range(len(a)):
            print(a, '######')
            # check if the dicai already has value and if its equal to the new bi or not. if not then return false else true
            if a[i] in dict1:
                # print(dict1[a[i]],b[i], 'first f')
                # dict1[a[i]] = b[i]
                if dict1[a[i]] != b[i]:
                    return False
            else:
                # print(dict1[a[i]],b[i], 'second if')
                # if dict1[a[i]] != b[i]:
                #     return False
                if b[i] in dict1.values():
                    return False
                dict1[a[i]] = b[i]
        return True



    # print(a)
    # set1 = {}
    # print(set1, set2)

# pattern = "abba"
# s = "dog cat cat dog"


pattern ="aba"
s = "dog cat cat"
# s ="cat cat cat dog"

# pattern = "abba"
# s = "dog cat cat fish"

# pattern = "aaaa"
# s = "dog cat cat dog"

print(wordPattern( pattern, s))