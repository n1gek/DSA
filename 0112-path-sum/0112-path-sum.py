# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def helper(node, curr):
            if not node:
                return False

            curr += node.val

            if curr == targetSum and not node.left and not node.right:
                return True
            
            left = helper(node.left, curr)
            right = helper(node.right, curr)

            return right or left
        
        return helper(root, 0)
