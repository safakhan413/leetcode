from collections import OrderedDict, Counter
def merge_the_tools(string, k):
    '''Algo:
    Output: ui printed on each line. Ui are subs of ti (parts s is divided in). order matters. Each string can only contain unique letters
    Input: string of len n and k.
    Steps:1. form t substrings
    2. for each subs form a set and print a set
    '''
    lenS = len(string)
    for i in range(0,lenS,k):
        ui = ''
        for j in range(i,i+k):
            if string[j] not in ui:
                ui += string[j]
        print(ui)

s = 'AABCAAADA'
k = 3

merge_the_tools(s,k)