#Given the head of a singly linked list. A cycle exists if the last node points back to a previous node, forming a loop. Remove the loop from the linked list if it exists.
#Internally, the driver code uses a variable x (1-based indexing) to represent the position of the node to which the last node is connected.
#The driver code will print "true" if the linked list is correctly modified, otherwise it will print "false".
''' Structure of Linked List Node
class Node:
    def __init__(self,val):
        self.next=None
        self.data=val
'''

class Solution:
    def removeLoop(self, head):
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
            
            if slow == fast:
                while slow != head:
                    prev = slow
                    slow = slow.next
                    head = head.next
                prev.next = None