# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        self.res = []
        def helper(root, curString):
            if not root:
                return 
            
            curString += str(root.val)
            
            if not root.left and not root.right:
                self.res.append(int(curString))
                return 
            
            left = helper(root.left, curString)
            right = helper(root.right, curString)
        
        helper(root, "")
        
        return sum(self.res)


        