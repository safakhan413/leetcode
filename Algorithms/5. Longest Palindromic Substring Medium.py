class Solution:
    def longestPalindrome(self, s: str) -> str:
        ## if 1 or 2 letters
        # return elem[0]
        # palindorme can ony be between two matching chars
        # get two matching chars positions and take them as candidate for palindromes
        # for each elem see if reverse of sting is equal to str
        # if yes then thats a palindrome. add it to arrayb
        # find longets elem of arrayB and retunr that
        # print(s)
        # if len(s) == 1 or len(s)==2:
        #     return s[0]
        if len(s) <= 1000:
            if len(s) == 1:
                return s
            elif len(s) == 2:
                if s[0] == s[1]:
                    return s
                else:
                    return s[0]
            else:

                # for ind,val in enumerate(s):
                #     print(ind,val)
                palinList = list()
                for i in range(0, len(s)):
                    for j in range(i + 1, len(s)):
                        if s[i] == s[j]:
                            palinList.append(s[i:j + 1])
                            # print(palinList)
                    # else:
                    #     return s[0]
                newpalin = list()
                for i in palinList:
                    if i == i[::-1]:
                        newpalin.append(i)
                        # print('im ne palin', newpalin)

            # return max(newpalin, key=len)
            if len(newpalin) > 0:
                return max(newpalin, key=len)
            else:
                return s[0]


