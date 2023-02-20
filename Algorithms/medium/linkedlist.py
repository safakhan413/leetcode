# pseudo code for finding common node between two lists. 
# return value and address of the node

'''Algo
output: common node btw l1 and l2
input:l1 and l2

#values may be common or not common so based on pointer
# may not be the same number of preceding nodes in l1 and l2 e.g. prec in l1 may be more than that of l2
Steps:
2 loops:
    base condition:
    l1.head = l2.head then return node.head, node.value
    
    conditions in the loop and what loops will you use:

loop through l1 and l2 using two loops:
while l1.next is not None:
    while l2.next is not None:
        l1.next != l2.next
        continue
        return l1.next, l1.next.value

'''

#pass keyword

def add(a,b):
    return a+b

def add(a,c,b):
    return a+b+c

s ='abcd  42'
# x = ''.join(map(s))
print(x)
lambda i: i*i

filter and map
method overloading and overriding
decorator programmaticqally
user defined data types
multiple params passed to python how? variable args



# print(add(10,20))