# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Method1: recursive(postorder traversal)
"""
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def check(root):
            if not root:
                return 0
            left_nodes = check(root.left)
            right_nodes = check(root.right)
            if (left_nodes == 0 and right_nodes != 0) or \
                (left_nodes != 0 and right_nodes == 0):
                return 1 + max(left_nodes, right_nodes)
            return 1 + min(left_nodes, right_nodes)
        return check(root)