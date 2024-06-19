## I have a txt file to read and, count number of capital letters in the file

##


class Animal():
    def __init__(self, numberOfLegs, sound ):
        self.numberOfLegs = numberOfLegs
        self.sound = sound
    
animal1 = Animal(4, 'bark')

import pandas as pd

df1 = pd.read_csv('fine.csv')


pd.concat(df1, df2 , axis=0)


## write a query for 10 students whose name start with a

# select first_name
# From Students As s
# Where s.first_name
# limit 10;

#course Id and student id
select count(c.id)
from student As s
INNER JOIN course as c
ON s.course_id = c.id
Group_by c.id




# def countCaps(filename='default.txt'):
#     #'*.txt'
#     # if filename == 'default.txt':


#     dict1 = {'a': 1, "b": 2}



#     lambda x: x+1

#     capFile = open(filename)

#     countCapitalLetters = 0
#     for line in capFile:
#         ### split each line in letters
#         ## check each letter to see if its upper()
#         # if upper then add 1 to the count
#         charList = [char for char in line]

#         for character in charList:
#             if character == character.upper():
#                 countCapitalLetters = countCapitalLetters +1
    
#     capFile.close()

#     return countCapitalLetters
    
