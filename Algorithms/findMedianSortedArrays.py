# import main
import math

class Solution:
    def findMedianSortedArrays(self, x, y) -> float:
        # 1. smaller array is X
        # 2. bigger array is Y
        # 3. start with smaller array. start, end, calculate partition start+end/2 xright
        # 4. partition y such that xlen+yen/2-xlen yright
        # 5. if condition is met return
        # 6. call the function with new prameter xpartition, y partition
        # try with recursion
        # print('hi', nums1, nums2)
        # xLen = min(len(nums1), len(nums2))
        # if xLen == len(nums1): x = nums1

        # if len(nums1) > len(nums2):
        #     x, y = nums2, nums1
        x, y = (x, y) if len(x) <= len(y) else (y, x)
        print('X is:', x)
        print('Y is: ', y)

        maxLeftX = 0
        minRightY = 0
        maxLeftY = 0
        minRightX = 0
        start = 0
        end = len(x)
        xpart, maxLeftX,minRightX = self.calculateXPartition(x,start, end)
        maxLeftY,minRightY = self.calculateYPartition(y,len(x), len(y), xpart)
        # maxLeftX = x[(xPart-1)]
        # minRightX=x[(xPart+1)]
        total_len_even = (len(x) + len(y)) % 2 == 0

        while not(maxLeftX <= minRightY and minRightX >= maxLeftY):
            if maxLeftX > minRightY:
                end = end - 1
                xpart, maxLeftX, minRightX = self.calculateXPartition(x, start, end)
                maxLeftY, minRightY = self.calculateYPartition(y, len(x), len(y), xpart)
                print('maxleftx minrightx is: ', maxLeftX, minRightX)
                print('maxlefty minrighty is: ', maxLeftY, minRightY)
                print('move left', xpart)
            else:
                start = start + 1
                xpart, maxLeftX, minRightX = self.calculateXPartition(x, start, end)
                maxLeftY, minRightY = self.calculateYPartition(y, len(x), len(y), xpart)
                print('maxleftx minrightx is: ', maxLeftX, minRightX)
                print('maxlefty minrighty is: ', maxLeftY, minRightY)
                print('move right', xpart)
        median = (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0 if total_len_even else float(max(maxLeftX, maxLeftY))
        return median

    def calculateXPartition(self, x, start, end):
        xpart = math.floor(start + end/2)
        maxLeftX = float('-inf') if xpart == 0 else x[(xpart-1)]
        minRightX=float('inf') if xpart == len(x) else x[(xpart)]
        return xpart, maxLeftX,minRightX
    def calculateYPartition(self,x,start,end, posx):
        ypart = math.floor((start + end+1)/2) - posx
        maxLeftY = float('-inf') if ypart == 0 else x[(ypart-1)]
        minRightY=float('inf') if ypart == len(x) else x[(ypart)]
        return maxLeftY,minRightY

######################### main method #######################
    def main(self):
        nums1 = [1, 3, 8, 9, 15]
        nums2 = [7, 11, 18, 19, 21, 25]
        # print('self is',  Solution())
        median = self.findMedianSortedArrays(nums1, nums2)
        print("median is: ", median)

if __name__ == "__main__":
    Solution().main()
