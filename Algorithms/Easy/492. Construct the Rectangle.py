"""
A web developer needs to know how to design a web page's size. So, given a specific rectangular web page’s area,
your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:

The area of the rectangular web page you designed must equal to the given target area.
The width W should not be larger than the length L, which means L >= W.
The difference between length L and width W should be as small as possible.
Return an array [L, W] where L and W are the length and width of the web page you designed in sequence.

 

Example 1:

Input: area = 4
Output: [2,2]
Explanation: The target area is 4, and all the possible ways to construct it are [1,4], [2,2], [4,1]. 
But according to requirement 2, [1,4] is illegal; according to requirement 3,  [4,1] is not optimal compared to [2,2]. So the length L is 2, and the width W is 2.
Example 2:

Input: area = 37
Output: [37,1]
Example 3:

Input: area = 122122
Output: [427,286]
 

Constraints:

1 <= area <= 10^7


"""
# def constructRectangle(area):

#     """
#     Square Root Start: Start checking from the integer part of the square root of the area. This is because the factors of a number that are closest to each other are around its square root.
#     Decrease Width: Decrease the width until you find a factor that divides the area evenly.
#     Calculate Length: Once you find such a width, calculate the corresponding length.
#     Return Result: Return the length and width as required.
#     """
#     import math
    
#     # Start from the square root of the area and move downwards
#     width = int(math.sqrt(area))
    
#     while area % width != 0:
#         width -= 1
    
#     length = area // width
#     return [length, width]

def constructRectangle(area):
    print(area)
    # find all possible factors
    factorList = []
    diff = []
    minDist = float('inf')
    for i in range(1,area+1):
        if area%i ==0:
            factor1 = i
            factor2 = area//i
            if factor1 >= factor2:
                    factorList.append((factor1, factor2, factor1-factor2))

    min_tuple = min(factorList, key=lambda x: x[2])
    return list(min_tuple[:2])
  


area =   122122
constructRectangle(area)
