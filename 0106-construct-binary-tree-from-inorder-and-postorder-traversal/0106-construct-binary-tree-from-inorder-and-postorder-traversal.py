# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        post_index = len(postorder) - 1
        hashmap = {}
        for i, val in enumerate(inorder):
            hashmap[val] = i

        def helper(left, right):
            nonlocal post_index
            if left > right:
                return None
            
            root_val = postorder[post_index]
            root = TreeNode(root_val)
            post_index -= 1

            idx = hashmap[root_val] #4

            root.right = helper(idx + 1, right)
            root.left = helper(left, idx - 1 )

            return root
        
        return helper(0, len(inorder) - 1)





        