def longestCommonPrefix(strs):
    # print(a)
    '''Algo
    Get smallest word length
    from index 0 to lenth of smllest word 
    run loop of each word

    '''
    pref = ''        
    # find min and max words among strs
    minWord = min(strs)
    maxWord = max(strs)

    # for iteration
    i = 0
    N = min(len(minWord), len(maxWord))
    
    while i < N:
        # if chars are equal
        if minWord[i] == maxWord[i]:
            # add this char to the answer
            pref += minWord[i]
        else:
            # if not, break
            break
        i += 1

    return pref
        # for i in range(lenShort):

        
            # print(word)
        # for char in word:



strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))
