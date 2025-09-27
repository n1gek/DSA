# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        if not root.right and not root.left:
            return True
            
        if not root.left or not root.right:
            return False
        
        def invertTree(node):
            if not node:
                return None
            
            node.left, node.right = node.right, node.left
            invertTree(node.left)
            invertTree(node.right)

            return node
        
        
        
        def checkSymmetry(a, b):
            if not a and not b:
                return True
            
            if not a or not b:
                return False
            
            if a.val != b.val:
                return False
            
            return checkSymmetry(a.left, b.left) and checkSymmetry(a.right, b.right)
        
        return checkSymmetry(root.left, invertTree(root.right))