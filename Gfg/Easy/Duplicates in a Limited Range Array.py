#Given an array arr[] of size n, containing elements from the range 1 to n, and each element appears at most twice, return an array of all the integers that appears twice.
#Note: You can return the elements in any order but the driver code will print them in sorted order.
#Examples:
#Input: arr[] = [2, 3, 1, 2, 3]
#Output: [2, 3] 
#METHOD 1[BRUTE FORCE] EXCEEDED TIME COMPLEXITY
# class Solution:
#     def findDuplicates(self, arr):
#         record = []
#         for i in range(len(arr)):
#             count = 0
#             for j in range(i+1, len(arr)):
#                 if arr[i] == arr[j]:
#                     count += 1
#             if count == 1:
#                 record.append(arr[i])
#         return record

#METHOD 2[HASH MAP]
class Solution:
    def findDuplicates(self, arr):
        freq = {}
        record = []
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        for key in freq:
            if freq[key] == 2:
                record.append(key)
        return record