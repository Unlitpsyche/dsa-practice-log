#You are given two arrays a[] and b[], return the Union of both the arrays in any order.
#The Union of two arrays is a collection of all distinct elements present in either of the arrays. If an element appears more than once in one or both arrays, it should be included only once in the result.
#Note that, You can return the Union in any order but the driver code will print the result in sorted order only.
#Examples:
#Input: a[] = [1, 2, 3, 2, 1], b[] = [3, 2, 2, 3, 3, 2]
#Output: [1, 2, 3]
class Solution:    
    def findUnion(self, a, b):
        seen = set()
        ans = []
        for i in a:
            if i not in seen:
                ans.append(i)
                seen.add(i)
                
        for i in b:
            if i not in seen:
                ans.append(i)
                seen.add(i)
        
        return ans