#Given the head of a linked list and an integer k, return the kth node from the end of the linked list. If k is greater than the number of nodes in the list, return -1.
#Examples :
#Input: k = 2

#Output: 8
#Explanation: 
#The 2nd node from end is 8.
""" Structure of Linked List Node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
"""

class Solution:
    def getKthFromLast(self, head, k):
        fast = head
        slow = head
        
        for i in range(k):
            if fast is None:
                return -1
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
            
        return slow.data