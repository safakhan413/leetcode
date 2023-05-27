from collections import Counter, OrderedDict
def isAnagram(s, t):
#    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
    
    # if s == t[:]

    '''
    algo:
    out: true if each letter in word 1 is used excatly once in word2
    input: s,t
    steps:
    

    '''
    x = dict(Counter(s))
    y = dict(Counter(t))
    xord = sorted(x.items())
    yord = sorted(y.items())
    print(xord, yord)
    if xord == yord:
        return True
    else:
        return False

    # print(),sorted(y.items()))


s = "anagram"
t = "nagaram"

print(isAnagram(s,t))