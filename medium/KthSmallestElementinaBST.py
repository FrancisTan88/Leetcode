from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def bst(root, k, label, find):
            if not root:
                return label, find
            label, find = bst(root.left, k, label, find)
            if find == 1:
                return label, find

            label = label + 1
            if label == k:
                find = 1
                return root.val, find

            label, find = bst(root.right, k, label, find)
            if find == 1:
                return label, find
            
            return label, find
        label, find = bst(root, k, 0, 0)
        return label