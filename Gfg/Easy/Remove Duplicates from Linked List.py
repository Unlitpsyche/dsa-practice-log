#Given a head of an unsorted linked list. Remove duplicate elements from this unsorted Linked List. When a value appears in multiple nodes, the node which appeared first should be kept, all other duplicates are to be removed.
''' Structure of linked list Node
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''
class Solution:
    def removeDuplicates(self, head):
        if head is None:
            return None
        seen = set()
        current = head
        previous = None
        while current:
            if current.data in seen:
                previous.next = current.next
            else:
                seen.add(current.data)
                previous = current
            current = current.next
        return head