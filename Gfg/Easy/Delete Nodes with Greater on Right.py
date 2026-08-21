#Given a singly linked list, remove all nodes that have a node with a greater value anywhere to their right in the list. Return the head of the modified linked list.

'''
Structure of linked list node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

'''
class Solution:
    def compute(self,head):
        if head is None:
            return None
        record = []
        curr = head
        while curr:
            record.append(curr)
            curr = curr.next
        max_node = record[-1]
        
        for i in range(len(record)-2,-1,-1):
            if record[i].data >= max_node.data:
                record[i].next = max_node
                max_node = record[i]

        return max_node