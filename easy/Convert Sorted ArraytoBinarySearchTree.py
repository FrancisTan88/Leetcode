from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def insert(nums, l, r):
            if l > r:
                return None
            middle = (l+r) // 2
            root = TreeNode(nums[middle])
            root.left = insert(nums, l, middle-1)
            root.right = insert(nums, middle+1, r)
            return root
        return insert(nums, 0, len(nums)-1)