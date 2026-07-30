#Given an integer array arr[] and an integer k, find and return the kth smallest element in the given array.
#Note: The kth smallest element is determined based on the sorted order of the array.
#Examples :
#Input: arr[] = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10], k = 4
#Output: 5
#Explanation: 4th smallest element in the given array is 5.
class Solution:
    def kthSmallest(self, arr, k):
        order = sorted(arr)
        for i in range(len(order)):
            if i == k-1:
                return order[i]
        return 
