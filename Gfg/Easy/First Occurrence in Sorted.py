#Given a sorted array arr[] and an integer k, find the position(0-based indexing) at which k is present in the array using binary search. If k doesn't exist in arr[] return -1. 
#Note: If multiple occurrences are there, please return the smallest index.
#Examples:
#Input: arr[] = [1, 2, 3, 4, 5], k = 4
#utput: 3
#Explanation: 4 appears at index 3.
class Solution:
    def firstSearch(self, arr, k):
        ans = -1
        left, right = 0, len(arr)-1
        while left <= right:
            mid = (left+right)//2
            if arr[mid] == k:
                ans = mid
                right = mid - 1
            elif arr[mid] < k:
                left = mid + 1
            else:
                right = mid - 1
        return ans