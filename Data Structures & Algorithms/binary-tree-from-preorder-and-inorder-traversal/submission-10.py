# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map values to their indices for O(1) lookup
        inorder_map = {val: i for i, val in enumerate(inorder)}
        
        # This pointer tracks the current root in the preorder list
        self.pre_idx = 0
        
        def dfs(in_left, in_right):
            # If the range is empty, there is no node to create
            if in_left > in_right:
                return None
            
            # 1. Pick the current root value from preorder and increment pointer
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1
            
            # 2. Find where this root sits in the inorder list
            pivot = inorder_map[root_val]
            
            # 3. Recursively build the left and right subtrees
            # Everything to the left of the pivot in 'inorder' is the left subtree
            root.left = dfs(in_left, pivot - 1)
            
            # Everything to the right of the pivot in 'inorder' is the right subtree
            root.right = dfs(pivot + 1, in_right)
            
            return root
            
        return dfs(0, len(inorder) - 1)