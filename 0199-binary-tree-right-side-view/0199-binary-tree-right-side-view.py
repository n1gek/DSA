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

            for x in range(n):
                current = stack.pop()
                if x == n - 1:
                    res.append(current.val)
                
                if current.left:
                    stack.appendleft(current.left)
                if current.right:
                    stack.appendleft(current.right)

        return res



        