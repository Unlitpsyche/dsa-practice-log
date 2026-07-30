#Given an array arr[] denoting heights of n towers and a positive integer k. For each tower, you must perform exactly one of the following operations exactly once.
#Increase the height of the tower by k, Decrease the height of the tower by k
#Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.
#Examples :
#Input: k = 2, arr[] = [1, 5, 8, 10]
#Output: 5
#Explanation: The array can be modified as [1+k, 5-k, 8-k, 10-k] = [3, 3, 6, 8]. The difference between the largest and the smallest is 8-3 = 5.
class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        arr.sort()
        ans = arr[-1] - arr[0]
        small = arr[0] + k
        big = arr[-1] - k
        if small > big:
            small, big = big, small
        for i in range(1, n):
            if arr[i] - k < 0:
                continue
            minimum = min(small, arr[i] - k)
            maximum = max(big, arr[i - 1] + k)
            ans = min(ans, maximum - minimum)
        return ans