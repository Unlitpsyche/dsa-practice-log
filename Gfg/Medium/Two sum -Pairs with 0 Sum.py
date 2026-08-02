#Given an integer array arr, return all the unique pairs [arr[i], arr[j]] such that i != j and arr[i] + arr[j] == 0.
#Note: The pairs must be returned in sorted order, the solution array should also be sorted, and the answer must not contain any duplicate pairs.
#Examples:
#Input: arr = [-1, 0, 1, 2, -1, -4]
#Output: [[-1, 1]]
#Explanation: arr[0] + arr[2] = (-1)+ 1 = 0.
#arr[2] + arr[4] = 1 + (-1) = 0.
#The distinct pair are [-1,1].
class Solution:
    def getPairs(self, arr):
        ans = set()
        pairs = set()
        for num in arr:
            if -num in ans:
                pairs.add((min(num,-num), max(num,-num)))  #Helps store in order
            ans.add(num)
            
        return [list(pair) for pair in sorted(pairs)]