#Given an array of integers arr[], the task is to find the first equilibrium point in the array.
#The equilibrium point in an array is an index (0-based indexing) such that the sum of all elements before that index is the same as the sum of elements after it. Return -1 if no such point exists. 
#Examples:
#Input: arr[] = [1, 2, 0, 3]
#Output: 2 
#Explanation: The sum of left of index 2 is 1 + 2 = 3 and sum on right of index 2 is 3.
class Solution:
    def findEquilibrium(self, arr):
        total = sum(arr)
        left = 0
        
        for i in range(len(arr)):
            total -= arr[i]
            
            if total == left:
                return i
            
            left += arr[i]
        return -1