from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def bst(root, lst):
            if not root:
                return lst
            lst = bst(root.left, lst)
            lst.append(root.val)
            lst = bst(root.right, lst)
            return lst
        return bst(root, [])[k - 1]
