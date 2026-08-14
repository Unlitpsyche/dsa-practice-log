#Given the root of a binary tree, find the maximum depth of the tree.
#Note: The maximum depth or height of the tree is the number of edges in the tree from the root to the deepest node.
''' Structure of Binary Tree Node
class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def height(self, root):
        def check(node):
            if not node:
                return -1
            left = check(node.left)
            right = check(node.right)
            return 1 + max(left, right)
        return check(root)