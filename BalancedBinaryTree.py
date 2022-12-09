# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(root):
            if not root:
                return 0

            left_nodes = check(root.left)
            right_nodes = check(root.right)

            if left_nodes == -1 or right_nodes == -1:
                return -1
            if abs(left_nodes - right_nodes) >= 2:
                return -1
            return 1 + max(left_nodes, right_nodes)
        return check(root) != -1