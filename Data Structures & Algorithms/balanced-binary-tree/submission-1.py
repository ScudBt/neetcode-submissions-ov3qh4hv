# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isCurrentlyBalanced = True
        def dfs(node):
            nonlocal isCurrentlyBalanced
            if not node:
                return -1
            leftDepth = dfs(node.left)
            rightDepth = dfs(node.right)
            if (abs(leftDepth - rightDepth) > 1):
                isCurrentlyBalanced = False
            return max(leftDepth, rightDepth) + 1
        dfs(root)
        return isCurrentlyBalanced