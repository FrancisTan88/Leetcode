# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def sum(root, targetSum, total):
            if not root:
                return
            
            total += root.val
            left_sum = sum(root.left, targetSum, total)
            right_sum = sum(root.right, targetSum, total)
            
            if left_sum or right_sum:
                return True
            if (not root.left and not root.right) and \
                total == targetSum:
                return True
            return False

        return sum(root, targetSum, 0)