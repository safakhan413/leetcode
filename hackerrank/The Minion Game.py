from itertools import permutations
from collections import Counter
def minion_game(string):
    # finding all substrings of s
    # vowels= ['A', 'E', 'I', 'O', 'U']
    # substrings = []
    # for i in range(len(string)):
    #     for j in range(i+1, len(string)+ 1):
    #         substrings.append(string[i:j])
    # # make a dictionary of alls trings
    # subs_count = Counter(substrings)
    # kev,stu = 0,0
    #
    # for k,v in subs_count.items():
    #     if k[0] in vowels:
    #         kev += v
    #     else:
    #         stu += v
    # if kev > stu:
    #     print('kevin', kev)
    # elif stu > kev:
    #     print('Stuart', stu)
    # else:
    #     print('Draw')

    ####### More efficient solution ###################
    player1 = 0;
    player2 = 0;
    str_len = len(string)
    for i in range(str_len):
        if string[i] in "AEIOU":
            player1 += (str_len) - i
        else:
            player2 += (str_len) - i

    if player1 > player2:
        print("Kevin", player1)
    elif player1 < player2:
        print("Stuart", player2)
    elif player1 == player2:
        print("Draw")
    else:
        print("Draw")


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