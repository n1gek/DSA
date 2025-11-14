# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        stack = deque([(root)])
        res = []

        while stack:
            n = len(stack)
            ll = []

            for _ in range(n):
                curr= stack.popleft()
                ll .append(curr.val)

                if curr.left:
                    stack.append((curr.left))
                if curr.right:
                    stack.append((curr.right))
            res.append(sum(ll) / n)
        
        return res

        




