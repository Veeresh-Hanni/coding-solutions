# Validate Binary Search Tree

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given the `root` of a binary tree,  *determine if it is a valid binary search tree (BST)*.

A  **valid BST**  is defined as follows:

- The left subtree of a node contains only nodes with keys strictly less than the node's key.
- The right subtree of a node contains only nodes with keys strictly greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

 

 **Example 1:** 

```
Input: root = [2,1,3]
Output: true

```

 **Example 2:** 

```
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

```

 

 **Constraints:** 

- The number of nodes in the tree is in the range [1, 104].
- -231 <= Node.val <= 231 - 1

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 20.8 MB (beats 74.01%)  
**Submitted:** 2026-08-04T06:45:32.101Z  

```py
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
```

---

[View on LeetCode](https://leetcode.com/problems/validate-binary-search-tree/)