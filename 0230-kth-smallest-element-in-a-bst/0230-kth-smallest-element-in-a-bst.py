from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # looking like we can use a bfs and sort the list 
        stack = deque([root])
        values = []
        while stack:
            current = stack.popleft()
            values.append(current.val)
        
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        
        values.sort()
        return values[k-1]
