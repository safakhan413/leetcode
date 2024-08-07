l1 = [1,2,4,1,5,6,4,8] 

## write  a function that gives indices of duplicate numbers in this list

## list of list where each sublist has indexes of duplicate numbers
from collections import Counter
def idx_dup_num(l1):
    print(dict(Counter(l1)))
    
    dic_count = dict(Counter(l1))
    
    print(dic_count.keys() if dic_count)

idx_dup_num(l1)


##design exercises

## base class shape with an area method
# two child classes Rectangle and Circle implement area method over here
# continue to build on top of it 

# def decorator_typeCheck(function):
#     def wrapper():
        



import math
class Shape:
    # def __init__(self):
    #     pass
    
    def area(self, **args):
        pass

class Rectangle(Shape):
    # def __init__(self, length, width):
    #     self.length = length
    #     self.width = width
    #     print("This is Rectangle class")
    
    def area(self,  length, width):
        area = length * width
        print(f"Rectangle area: {area}")
        return area
        
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        print("This is Circle class" )
    
    def area(self):
        area = self.radius**2 * math.pi
        print(f"Circle area: {area}")
        return area
        
rectangle1= Rectangle()
l = [(2,4), (5,6)] # two diff rectangle but loop over them
rectangle1.area(l)

# static method and a class method

# circle1= Circle(2)
# circle1.area()

## we want to limit these into integers
# exception if values not integer

# we want to write decorator that will take care of both rectangle and circle and get an exception if value is not integer

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")

# write a string "my name is safa and today's date is August 7"
str1 = "my name is safa and today's date is August 77"


# remove the white spaces from the string

def removeSpaces(str1):
    # str1 = str.strip()
    str1 = str1.replace(" ", "")
    print(str1)
    return str1
    
str1 = removeSpaces(str1)

#  write a program that prints the characters that show up more than once in the string
from collections import Counter

def printDuplicatedChars(str1):
    print(dict(Counter(str1)))
    count_dict = dict(Counter(str1))
    for key,val in count_dict.items():
        if val >=2:
            print(key) 
    
# printDuplicatedChars(str1)

# split the string in half and have the second ha;f have all upper case

def splitHalfcastUpper(str1):
    len_s = len(str1)
    print(len_s)
    # if 37? one side will have more than the other depending on how you split them up
    # for even case
    new_str = ""
    if len_s%2==0:
        halfIndex = len_s //2
        print(halfIndex)
        new_str = str1[:halfIndex+1] + str1[halfIndex+1:].upper()
        print(new_str)
        
    ### for even and odd cases
    

# splitHalfcastUpper(str1)

l1 = [i for i in range(1,21)]
print(l1)
## using this list add 2 to every odd number and 1 to every even number in the list

def add_twoOdd_oneEven(l1):
    l2 = []
    for i in l1:
        if i%2==0:
            l2.append(i+1)
        else:
            l2.append(i+2)
    print(l2)
    return l2
    
add_twoOdd_oneEven(l1)

# using the same list remove 2nd to last number

SecondToLast = l1[-2]
l1.remove(SecondToLast)




