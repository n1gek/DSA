"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        def getNextChild(node):
            while node:
                if node.left:
                    return node.left
                if node.right:
                    return node.right
                node = node.next
            
            return None

        
        def helper(node):
            if not node:
                return None

            if node.left:
                if node.right:
                    node.left.next = node.right
                else:
                    node.left.next = getNextChild(node.next)
            
            if node.right:
                node.right.next = getNextChild(node.next)
            
            helper(node.right)
            helper(node.left)

            return node
        return helper(root)
