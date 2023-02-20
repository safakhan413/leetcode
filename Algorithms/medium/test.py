# Input: Hello How Are You
# OutPut  : olleH woH erA uoY

'''
Algorith:
# OutPut  : olleH woH erA uoY
# Input: Hello How Are You

Steps:
split the sentence into tokens
then loop through each token and reverse the string 
and add it to the final string in join or list and then join
'''

def reverseWords(s):
    tokens = s.split()
    print(tokens)
    revS =  ''
    for i in tokens:
        revS = revS+' '+ i[::-1]
    # print(revS)
    return revS

s = 'Hello How Are You'
print(reverseWords(s))

#################
