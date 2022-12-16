# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        def count(root, nums):
            if not root:
                return nums
            else:
                nums += 1
                n1 = count(root.left, nums)
                n2 = count(root.right, nums)
                return max(n1, n2)
        if not root:
            return 0
        nums = 1
        left_tree = count(root.left, nums)
        right_tree = count(root.right, nums)
        return max(left_tree, right_tree)