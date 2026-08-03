#Given an array arr[] of positive integers and an integer k. Find the maximum value for each contiguous subarray of size k.
#Return an array of maximum values corresponding to each contiguous subarray.
#Examples:
#Input: arr[] = [1, 2, 3, 1, 4, 5, 2, 3, 6], k = 3
#Output: [3, 3, 4, 5, 5, 5, 6]
#Explanation: 
#1st contiguous subarray [1, 2, 3], max = 3
#2nd contiguous subarray [2, 3, 1], max = 3
#3rd contiguous subarray [3, 1, 4], max = 4
#4th contiguous subarray [1, 4, 5], max = 5
#5th contiguous subarray [4, 5, 2], max = 5
#6th contiguous subarray [5, 2, 3], max = 5
#7th contiguous subarray [2, 3, 6], max = 6
from collections import deque

class Solution:
    def maxOfSubarrays(self, arr, k):
        dq = deque()
        ans = []
        for i in range(len(arr)):
            # Remove indices outside the window
            while dq and dq[0] <= i - k:
                dq.popleft()
            # Remove smaller elements
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()
            dq.append(i)
            # Record maximum once the first window is complete
            if i >= k - 1:
                ans.append(arr[dq[0]])

        return ans