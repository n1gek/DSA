# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        res = []
        que = deque([root])

        while que:
            total = 0
            n = len(que)
            length = 0

            for x in range(n):
                current = que.pop()
                total += current.val
                length += 1

                if current.left:
                    que.appendleft(current.left)
                if current.right:
                    que.appendleft(current.right)
            
            avg = total / length
            res.append(avg)
        
        return res

