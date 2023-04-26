# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    (best solution)
    time: O(n), where n is the number of nodes in tree.
    space: O(1)
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traverse(root, p, q):
            if not root:
                return None
            if root == p or root == q:
                return root
            left = traverse(root.left, p, q)
            right = traverse(root.right, p, q)
            if left and right:
                return root
            return left or right
        return traverse(root, p, q)
