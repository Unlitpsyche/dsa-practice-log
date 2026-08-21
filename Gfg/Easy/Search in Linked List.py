#Given a linked list with the head node and a key, the task is to check if the key is present in the linked list or not. 

'''Structure of Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def searchKey(self, head, key):
        if head is None:
            return None
        fast = head
        while fast:
            if fast.data == key:
                return True
                break
            else:
                fast = fast.next
        return False