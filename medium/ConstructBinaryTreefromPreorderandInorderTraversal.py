from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    '''
    time: O(n)
    space: O(n)
    '''
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(left, right, preorder, inorder, hashmap, idx_pre):
            if left > right:
                return None, idx_pre
            root = TreeNode(preorder[idx_pre])
            idx_inorder = hashmap[str(preorder[idx_pre])]
            idx_pre += 1
            root.left, idx_pre = build(left, idx_inorder-1, preorder, inorder, hashmap, idx_pre)
            root.right, idx_pre = build(idx_inorder+1, right, preorder, inorder, hashmap, idx_pre)
            return root, idx_pre
        hashmap = {}
        for i, v in enumerate(inorder):
            hashmap[str(v)] = i
        return build(0, len(inorder)-1, preorder, inorder, hashmap, 0)[0]