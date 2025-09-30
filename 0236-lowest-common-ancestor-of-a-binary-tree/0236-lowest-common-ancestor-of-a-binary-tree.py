# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def helper(current):
            if not current:
                return None
            
            if p.val == current.val or q.val == current.val:
                return current 
            
            left = helper(current.left)
            right = helper(current.right)

            if left and right:
                return current # they are on different subtrees
            
            return left or right
        
        return helper(root)




        