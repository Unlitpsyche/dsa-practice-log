#Given an array arr[] of integers and another integer target. Determine if there exist two distinct indices such that the sum of their elements is equal to the target.
#Examples:
#Input: arr[] = [0, -1, 2, -3, 1], target = -2
#Output: true
#Explanation: arr[3] + arr[4] = -3 + 1 = -2
class Solution:
	def twoSum(self, arr, target):
		seen = set()
		for num in arr:
		    if target-num in seen:
		        return True
		    seen.add(num)
        return False