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

        stack = deque([root])
        res = []
        left = True

        while stack:
            level = []

            for i in range(len(stack)):
                if left:
                    curr = stack.pop()
                    level.append(curr.val)

                    if curr.left:
                        stack.appendleft(curr.left)
                    if curr.right:
                        stack.appendleft(curr.right)
                    
                else:
                    curr = stack.popleft()
                    level.append(curr.val)

                    if curr.right:
                        stack.append(curr.right)
                    if curr.left:
                        stack.append(curr.left)


        

            left = not left #true
            print(level)
            res.append(level)

        
        return res
        

