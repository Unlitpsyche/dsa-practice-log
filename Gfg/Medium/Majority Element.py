#Given an array arr[]. Find the majority element in the array. If no majority element exists, return -1.
#Note: A majority element in an array is an element that appears strictly more than arr.size()/2 times in the array.
#Examples:
#Input: arr[] = [1, 1, 2, 1, 3, 5, 1]
#Output: 1
#Explanation: Since, 1 is present more than 7/2 times, so it is the majority element.
class Solution:
    def majorityElement(self, arr):
        freq = {}
        n = len(arr)
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        for num in freq:
            if freq[num] > n//2:
                return num
        return -1