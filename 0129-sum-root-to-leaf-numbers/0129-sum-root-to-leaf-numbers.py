# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        res = []

        def helper(node, curr):
            if not node:
                return
            
            curr += str(node.val)
            
            if not node.left and not node.right:
                res.append(int(curr))
                return
            
            left = helper(node.left, curr)
            right = helper(node.right, curr)

        
        curr = ""

        helper(root, curr)
        total = 0
        for num in res:
            total += num
        print(res)

        return total

            
            
            

         