# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root, min, max):
            if not root:
                return True
            if not min < root.val < max:
                return False
            if root.left and not valid(root.left, min, root.val):
                return False
            if root.right and not valid(root.right, root.val, max):
                return False
            return True
        return valid(root, -1001, 1001)