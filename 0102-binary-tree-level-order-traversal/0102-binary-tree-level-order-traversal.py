# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        que = deque([root])
        res = []

        while que:
            level = []
            n = len(que)

            for x in range(n):
                current = que.pop()
                level.append(current.val)

                if current.left:
                    que.appendleft(current.left)
                if current.right:
                    que.appendleft(current.right)
            res.append(level)
        
        return res

        