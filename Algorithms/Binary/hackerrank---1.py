def find_substring(s):
    for i in range(1, len(s) + 1):
        substring = s[:i]

        repeats = len(s) // len(substring)
        print(repeats,s,substring )
        print(substring * repeats)
        if substring * repeats == s:
            return (substring, repeats)

def findSmallestRepeatedSubsequence(primary, secondary):
    # Write your code here
    '''
    Algo
    handling case 1 and case 2 separately
    Case 1: find length of s and see if it is a multiple of p.
    If it is then for pos [0:step] check if string is a match. Step is length and you have to do it for however multiple s is of p
     If it is then s is repeated copy of primary
     find the smallest repeated string:



    '''
    lenP = len(p)
    lenS = len(s)
    # print(lenP,lenS)
    mulVal = 0
    if lenS%lenP == 0:
        ## find the multiplevalue
        mulVal = lenS/lenP
    # print(mulVal)
    boolVal = False
    if mulVal !=0:
        preVal = 0
        for i in range(0,lenS+1,lenP):
            # print(i, p[0:lenP])
            if p[0:lenP] == s[i:i+lenP]:
                boolVal = True
    if boolVal == True:
        x,y = find_substring(p)
        LenSub = len(x)
        return LenSub
    else:
        return (-1*lenS)
        # print(LenSub)





p = 'ATCATC'
s = 'ATCATCATCATC'

print(findSmallestRepeatedSubsequence(p,s))

