from itertools import permutations
def minion_game(string):
    # finding all substrings of s
    vowels= ['A', 'E', 'I', 'O', 'U']
    substrings = []
    for i in range(len(string)):
        for j in range(i+1, len(string)+ 1):
            substrings.append(string[i:j])
    # make a dictionary of alls trings
    subsCount = dict()
    for i in substrings:
        subsCount[i] = subsCount.get(i,0)+1
    s,k = 0,0
    for words, numTimes in subsCount.items():
        if words[0] in vowels:
            k +=numTimes
        else:
            s +=numTimes
    if k > s:
        print('kevin', k)
    else:
        # print'Stuart', s
        # print "Stuart", stusc
    # print(substrings)

minion_game('BANANA')

''' Algorithm

Output: name and score for the winner
Score calculation criteria: find all substrings of string S
S has to make words beginning with vowel
K has to make words beginning with consonants

1. put them all in a dictionary and add 1 everytime you go through string again and find tahts ubstring
2. keep 2 varibles stuart and kevin. If cosnonants add to stuart, if vowel add to kevin
3. compare the two values and print teh winner with score


'''