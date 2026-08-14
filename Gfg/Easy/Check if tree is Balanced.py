#Given the root of a binary tree, determine if it is height-balanced or not.
#Note: A binary tree is considered height-balanced if the absolute difference in heights of the left and right subtrees is at most 1 for every node in the tree.
''' Structure of binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def isBalanced(self, root):
        def check(node):
            if not node:
                return 0
            left = check(node.left)
            if left == -1:
                return -1
            right = check(node.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
        return check(root) != -1