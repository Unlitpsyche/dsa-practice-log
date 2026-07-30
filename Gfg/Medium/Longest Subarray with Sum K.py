#Given an array arr[] containing integers and an integer k, your task is to find the length of the longest subarray where the sum of its elements is equal to the given value k. If there is no subarray with sum equal to k, return 0.
#Examples:
#Input: arr[] = [10, 5, 2, 7, 1, -10], k = 15
#Output: 6
#Explanation: Subarrays with sum = 15 are [5, 2, 7, 1], [10, 5] and [10, 5, 2, 7, 1, -10]. The length of the longest subarray with a sum of 15 is 6.
class Solution:
    def longestSubarray(self, arr, k):  
        ans = 0
        total = 0
        profit = {}
        for i in range(len(arr)):
            total += arr[i]
            if total == k:
                ans = i + 1
            if (total-k) in profit:
                ans = max(ans, i - profit[total-k])
            if total not in profit:
                profit[total] = i
                
        return ans