#Given an array arr[] with non-negative integers representing the height of blocks. If the width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 
#Examples:
#Input: arr[] = [3, 0, 1, 0, 4, 0, 2]
#Output: 10
#Explanation: Total water trapped = 0 + 3 + 2 + 3 + 0 + 2 + 0 = 10 units.
class Solution:
    def maxWater(self, arr):
        left = 0
        right = len(arr) - 1
        leftMax = 0
        rightMax = 0
        water = 0
        while left <= right:
            if arr[left] <= arr[right]:
                if arr[left] >= leftMax:
                    leftMax = arr[left]
                else:
                    water += leftMax - arr[left]
                left += 1
            else:
                if arr[right] >= rightMax:
                    rightMax = arr[right]
                else:
                    water += rightMax - arr[right]
                right -= 1
        return water