class Solution:
    def maxSubarraySum(self, arr):
        largest = arr[0]
        curr_sum = arr[0]
        for i in range(1, len(arr)):
            curr_sum = max(arr[i], curr_sum + arr[i])
            largest = max(largest,curr_sum)
        return largest