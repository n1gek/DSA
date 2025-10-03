# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(mini,node, maxi):
            if node is None:
                return True
            if not mini < node.val < maxi:
                return False
            
            return helper(mini, node.left, node.val) and helper(node.val, node.right, maxi)
            
        return helper(float("-inf"),root, float("inf"))