#Given two sorted arrays a[] and b[], where each array may contain duplicate elements , the task is to return the elements in the union of the two arrays in sorted order.
#Union of two arrays can be defined as the set containing distinct common elements that are present in either of the arrays.
#Examples:
#Input: a[] = [1, 2, 3, 4, 5], b[] = [1, 2, 3, 6, 7]
#Output: [1, 2, 3, 4, 5, 6, 7]
#BRUTE FORCE(Time Limit exceeded)
class Solution:
    def findUnion(self, a, b):
        present = set()
        for i in range(len(a)):
            present.add(a[i])
            for j in range(len(b)):
                if b[j] not in present:
                    present.add(b[j])
        return sorted(present)

#Preferred MEthod
class Solution:
    def findUnion(self, a, b):
        i = 0
        j = 0
        ans = []
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                if not ans or ans[-1] != a[i]:
                    ans.append(a[i])
                i += 1
            elif a[i] > b[j]:
                if not ans or ans[-1] != b[j]:
                    ans.append(b[j])
                j += 1
            else:
                if not ans or ans[-1] != a[i]:
                    ans.append(a[i])
                i += 1
                j += 1
        while i < len(a):
            if not ans or ans[-1] != a[i]:
                ans.append(a[i])
            i += 1
        while j < len(b):
            if not ans or ans[-1] != b[j]:
                ans.append(b[j])
            j += 1
        return ans