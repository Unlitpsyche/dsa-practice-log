#Given an array arr[] that contains positive and negative integers (may contain 0 as well). Find the maximum product that we can get in a subarray of arr[].
#Examples
#Input: arr[] = [-2, 6, -3, -10, 0, 2]
#Output: 180
#Explanation: The subarray with maximum product is [6, -3, -10] with product = 6 * (-3) * (-10) = 180.
class Solution:
	def maxProduct(self,arr):
	    maxprod = arr[0]
	    minprod = arr[0]
	    ans = arr[0]
	    for i in range(1, len(arr)):
    	    if arr[i] < 0:
    	        maxprod, minprod = minprod, maxprod
	        maxprod = max(arr[i], maxprod * arr[i])
	        minprod = min(arr[i], minprod * arr[i])
	        
	        ans = max(ans, maxprod)
    	        
    	return ans