# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # post order traversal
        def dfs(node):
            if not node:
                return True
            leftBool = dfs(node.left)
            rightBool = dfs(node.right)
            if leftBool:
                node.left = None
            if rightBool:
                node.right = None
            if not node.left and not node.right and node.val == target:
                return True
        
        dfs(root)
        if root and root.val == target:
            return None
        return root
