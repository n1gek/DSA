# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # use a stack and traverse to the leftmost node
        # at the leftmost node, add it to the stack
        # increement the counter
        # pop the node on top
        # add its children to the stack
        # use inorder left = root - right traversal

        stack = []
        count = 0

        def pushLeft(node):
            curr = node
            while curr:
                stack.append(curr)
                curr = curr.left
        pushLeft(root)
        
        
        while stack:
            node = stack.pop()
            count += 1

            if count == k:
                return node.val
            

            if node.right:
                curr = node.right
                pushLeft(curr)

            





        