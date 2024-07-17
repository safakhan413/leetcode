"""
There is a forest with an unknown number of rabbits. We asked n rabbits "How many rabbits have the same color as you?"
 and collected the answers in an integer array answers where answers[i] is the answer of the ith rabbit.

Given the array answers, return the minimum number of rabbits that could be in the forest.

 

Example 1:

Input: answers = [1,1,2]
Output: 5
Explanation:
The two rabbits that answered "1" could both be the same color, say red.
The rabbit that answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.
Example 2:

Input: answers = [10,10,10]
Output: 11


"""
from collections import Counter
def numRabbits(answers):
    print(answers)
    """
    Out: minimum number of rabbits that could be in teh forest
    input: answers that you got from rabbits of which color they are
    algo:
    step1:
    rule 1. if two answers are same then those rabbits are same colors and they are talking of each other so whatever they are saying add 1 to it for the rabbit who is speaking
    rule 2. if there are unique numbers add those +1 for the speaking rabbit because that rabbit is speaking about rabbits that havent been questioned
     
    #    could be the same colors so consider them 2 rabbits (number of times answered), min could be answer.length and we add from there, if answers are different then add those answers as whole otherwise skip,
    
    """

    # To satisfy rule 1, find duplicates in numbers
    anset = set(answers)
    count = Counter(answers)
    print(count)
    print(anset, 'im anset')
    minRabbits = 0
    counterforgt1 = 0
    for i in anset:
        if i == 0:
            minRabbits += count[i]
            print(minRabbits, 'im in 0')
        if count[i] > 1:
            if counterforgt1 == 0 and i !=0:
                minRabbits = minRabbits + i
                print(minRabbits, i, 'im in inner >1')

                counterforgt1 = 1
            else:
                minRabbits += 1
            print(minRabbits, 'im in >1')

        elif count[i] == 1:
            minRabbits += i +1
            print(minRabbits, 'im in ==1')

        # elif count[]

    print(minRabbits)
    return minRabbits
    # for i in answers:
    #     if i in anset:


# answers = [1,1,2]

answers =[1,0,1,0,0]

min_r = numRabbits(answers)
print(min_r, 'min rabbits')