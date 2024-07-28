# #not an interview question but a practice one
# Q3: Write a program that will find all such numbers which are divisible by 7 but are 
# not a multiple of 5, between 2000 and 2100 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def divby7Notmulti5():
    x=''
    y = []
    for i in range(2000,2101):
        if i%7 == 0 and i%5 !=0:
            # x= ",".join(i)
            y.append(str(i))
    x= ','.join(y)
    print(x)
divby7Notmulti5()


- Given two sets S and T, each of size n, and a number x, 
describe an algorithm to answer whether there exists a pair of elements,
one from S and one from T, that add up to x.

S = [1,3,4]
T = [2,5,6]
x = 8

S+T = [1,3,4,2,5,6]
       l         r -> 7 < 8
         l       r -> 9 > 7
         l     r   -> 8 = 8.
        
S = [1, 2, 4]
T = [50, 100, 200]
x = 54
S+T = [1,2,4,50,100,200]
       l            r  -> 201 > 54
         l          r  -> 202 > 54
           l        r  -> 204 > 54 
# This counterexample is wrong, the algorithm works correctly here!!


- Write a function that takes a list of integers as input 
and returns the smallest positive integer that does not exist in the list.

f([3,4,5]) -> 1
f([-10, -1, 0, 1, 30]) -> 2
f([-1,-2,-3]) -> 1

f([1,2]) -> 3

def minPos(l):
	# l is list of integers
  if len(l) ==0:
  	return None
	for i, x in enumerate(l):
  	if l[i] <=0:
    	l.pop(l[i])
      
      ## all elements in l that are less than or equal to 0 will be popped so I get a list of ony [1,30]
      
    ### I get an l with only 1,30
  if len(l)>0:

    #smallPos = -1
    minOfL = min(l)
    if minOfL == 1:
      #smallPos = minOfL + 1  # <- will smallPos ever be anything other than 2
      return 2
    else
      return 1
  else:

    return 1

      
- Suppose you're creating a platform for selling cars. There are following requirements:
    1) Car has a manufacturer, model, year, version, price and VIN
    2) VIN number is unique per car
    3) Car can have optional accessories identified by name and price
To do:
    1) Design a minimal database schema/django models structure to solve this. Describe tables, relationships and constraints.
    2) Write a query in SQL that will return a list of all accessories priced above 1000 for the specified vehicle VIN.


Car Table: Columns 
SQLAlchemy or some other library to interface with the database

class Car:

	def __init__(self, manufacturer, model, year, version, price and VIN):
  	self.manufacturer= manufacturer
    self.model = model
    self.year = year
    self.version = version 
    self.price = price # int or numeric
    self.VIN = VIN
    
  
  def createCar
  
  
  SQL:
  
  select a.name, a.price
  from accessories a 
  JOIN Car c ON a.VIN_id = c.VIN
  WHERE a.price >1000
  AND c.VIN = '123'
      
      
      
      
      
      



