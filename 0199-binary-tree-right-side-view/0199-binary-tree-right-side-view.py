# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def helper(root, level):
            if root is None:
                return []

            if level == len(result):
                result.append(root.val)

            helper(root.right, level + 1)
            helper(root.left, level + 1)
        helper(root, 0)
        return result