# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack =  [root]
        prev = None

        while stack:
            curr = stack.pop()

            if prev:
                prev.right = curr
                prev.left = None
            
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
            
            prev = curr