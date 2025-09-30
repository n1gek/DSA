# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        que = deque([root])
        res = []
        leftToRight = True

        while que:
            n = len(que)
            level = []

            for i in range(n):
                if leftToRight:
                    current = que.pop()
                    level.append(current.val)

                    if current.left:
                        que.appendleft(current.left)
                    if current.right:
                        que.appendleft(current.right)
                
                else:
                    current = que.popleft()
                    level.append(current.val)

                    if current.right:
                        que.append(current.right)
                    if current.left:
                        que.append(current.left)

            res.append(level)
            leftToRight = not leftToRight
        
        return res