import sys
import math

# n = int(input())
'''
Algo:
Output: contra or cons
Input: num of inequalities and inequalities
Steps:
1. add all diff in dict with priorities 
2. add all diff in a list
3. go through teh list and 
'''
# n = 2
import fileinput

# for line in fileinput.input():

adj_list = dict()
set1 = set()
n = 0
for line in fileinput.input(files=('codingame_test')):
    row = line.rstrip()
    k,v = row.split('>')
    k = k.rstrip(' ')
    v = v.lstrip(' ')
    set1.add(k)
    set1.add(v)

    if k in adj_list:
        # append the new number to the existing array at this slot
        adj_list[k].append(v)
    else:
        # create a new array in this slot
        adj_list[k] = [v]
for n in set1:
    if n not in adj_list.keys():
        adj_list[n] = []
    # print(n)
print(adj_list)
print(set1)
color = {}
parent = {}

for u in adj_list.keys():
    color[u] = 'W'
    parent[u] = None


def dfs(u, color):
    color[u] = 'G'
    print(u)
    for v in adj_list[u]:
        if color[v] == 'W':
            cycle = dfs(v, color)
            if cycle:
                return True
        elif color[v] == 'G':  # cycle is present
            print(u, v)
            return True
    color[u] = 'B'
    return False


is_cyclic = False
for u in adj_list.keys():
    if color[u] == 'W':
        is_cyclic = dfs(u, color)
        if is_cyclic:
            break
print("Is cyclic ", is_cyclic)

if is_cyclic:
    print('contradiction')
else:
    print('consistent')
