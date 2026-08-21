#Given the head of a linked list and an integer x, delete the node at position x and return the updated head of the linked list.
#Note: Positions use 1-based indexing.
''' Structure of Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def deleteNode(self, head, x):
        if head is None:
            return None
        if x == 1:
            return head.next
        current = head
        for _ in range(x - 2):
            current = current.next
        current.next = current.next.next

        return head