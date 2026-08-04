# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = float('-inf')  # Track preceeding node value
        
        def inorder(node):
            if not node:
                return True
            
            # 1. Left subtree validation
            if not inorder(node.left):
                return False
            
            # 2. Root node validation (Current node should be strictly greater than prev)
            if node.val <= self.prev:
                return False
            self.prev = node.val  # Update prev to current node value
            
            # 3. Right subtree validation
            return inorder(node.right)
            
        return inorder(root)