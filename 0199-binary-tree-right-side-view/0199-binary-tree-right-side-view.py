# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = deque([root])
        res = []

        while stack:
            n = len(stack)

            for i in range(n):
                curr = stack.popleft()
                if i == n -1:
                    res.append(curr.val)
                
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
        
        return res



    