"""You are given an integer array height of length n. There are n vertical lines drawn
 such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container"""

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, 
# the max area of water (blue section) the container can contain is 49
import matplotlib
def maxArea(height):
    # import matplotlib.pyplot as plt
    # import seaborn as sns
    # import numpy as np
    # ax = sns.barplot(x=np.arange(len(height)), y=height)
    # ax.bar_label(ax.containers[0])
    # plt.axis('off')
    # plt.show()

    # l = 0
    # area = 0
    max_area = 0
    left = 0
    right = len(height) - 1
    
    while left < right:
        # Calculate the current area
        current_area = min(height[left], height[right]) * (right - left)
        
        # Update max_area if current_area is greater
        if current_area > max_area:
            max_area = current_area
        
        # Move the pointer towards the center for potentially larger area
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area
            # print(area, 'im the area')







height = [1,8,6,2,5,4,8,3,7]
area = maxArea(height)
print(area)
