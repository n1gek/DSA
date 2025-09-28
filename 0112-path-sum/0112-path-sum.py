# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def helper(root, current_sum):
            if not root:
                return False
            
            current_sum += root.val
            if current_sum == targetSum and not root.left and not root.right:
                return True 
            

            left_sum = helper(root.left, current_sum)
            right_sum = helper(root.right, current_sum)

            return left_sum or right_sum
        
        return helper(root, 0)
            