# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # both preorder and inorder have the same index for right child
        if not preorder:
            return None
        inorderDict = {}
        for i, n in enumerate(inorder):
            inorderDict[n] = i
        def dfs(preLeft, preRight, inLeft, inRight):
            nonlocal inorderDict
            if preLeft>preRight or inLeft>inRight:
                return
            root = TreeNode()
            root.val = preorder[preLeft]
            rootPos = inorderDict[root.val]
            leftSize = rootPos - inLeft 
            root.left = dfs(preLeft+1, preLeft+leftSize, inLeft, rootPos-1)
            root.right = dfs(preLeft+1+leftSize, preRight, inorderDict[root.val]+1, inRight)
            return root
        return dfs(0, len(inorder)-1, 0, len(inorder)-1)