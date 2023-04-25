# You are given two rectangles a and b each defined by four ordered pairs denoting their corners on the x, y plane. Write a function rectangle_overlap to determine whether or not they overlap. Return True if so, and False otherwise.

# Note: If the two rectangles border one another, or share a corner like two diagonally adjacent positions on a chessboard, they are said to overlap.

# Note: The lists of ordered pairs are in no particular order. The first entry in list a could be the top left corner while the first in list b is the bottom right.

# Example:

# Input:


# a = [(-3,5), (-3,2),(0,5),(0,2)]
# b = [(-1,4), (3,4), (3,1), (-1,1)]

from operator import itemgetter

def find_left_range_rectangle(alist):
    a_lt_range = []
    for i in range(alist[0][1], alist[1][1]+1):
        # print(i)
        a_lt_range.append((alist[0][0], i))
    return a_lt_range

# def find_right_range_rectangle(alist):
#     a_lt_range = []
#     for i in range(alist[2][1], alist[3][1]+1):
#         # print(i)
#         a_lt_range.append([alist[2][0], i])
#     return a_lt_range

def find_top_range_rectangle(alist):
    a_lt_range = []
    for i in range(alist[1][0], alist[3][0]+1):
        # print(i)
        a_lt_range.append((i, alist[1][1]))
    return a_lt_range

# def find_bottom_range_rectangle(alist):
#     a_lt_range = []
#     for i in range(alist[0][0], alist[2][0]+1):
#         # print(i)
#         a_lt_range.append([i, alist[0][1]])
#     return a_lt_range








def rectangle_overlap(a, b):
    '''Algo

    output: true if the rectangles intersect, otherwise false
    input: two lists representing coordinates of the rectangles
    Steps: find top, bottom, left, right 
    left is with 2 lowest x coordinates. 
    '''
    # print(type(a[0]))
    # x = set((-3,5))
    # y = set((-3,2))
    # print(x[0], x[1])
    #find two lowest 

    alist = sorted(a, key=itemgetter(0,1))
    blist = sorted(b, key=itemgetter(0,1))

    # lt = sorted(a, key=itemgetter(0,1))
    # rt = sorted(b, key=itemgetter(0,1))
    # alist = [list(x) for x in lt]
    # blist = [list(x) for x in rt]
    # print(alist,blist)
    #left sides of recatangles both lists 
    a_lt = find_left_range_rectangle(alist)
    b_lt = find_left_range_rectangle(blist)
    #right side of rectangle both lists 
    # a_rt = find_right_range_rectangle(alist)
    # b_rt = find_right_range_rectangle(blist)
    #top side of rectangle both lists 
    a_top = find_top_range_rectangle(alist)
    b_top = find_top_range_rectangle(blist)
    #bottom side of rectangle both lists 
    # a_bott = find_bottom_range_rectangle(alist)
    # b_bott = find_bottom_range_rectangle(blist)

    # Realized problem with my logic. This is a good solution but can be simplified. I just needed left and bottom or right and top to check if they overlap
    # 

    ltaset = {item[1] for item in a_lt}
    ltbset = {item[1] for item in b_lt}
    # print( 'im lt a range', ltset)
    topaset = {item[0] for item in a_top}
    topbset = {item[0] for item in b_top}
    print(ltaset,ltbset, topaset, topbset)
    print(ltaset & ltbset, topaset & topbset)

    boolVal = not(ltaset.isdisjoint(ltbset) and topaset.isdisjoint(topbset))
    return boolVal
    # print( 'im lt a range',set(itemgetter(1)(a_lt)))

    # print( 'im lt b range',rtset)


    # print(sorted(b, key=listitemgetter(0,1)))

    # print(ltlist, rtlist)






a = [(-3,5), (-3,2),(0,5),(0,2)]
b = [(-1,4), (3,4), (3,1), (-1,1)]


print(rectangle_overlap(a,b))
# dothey= rectangle_overlap(a,b)
# print(dothey)