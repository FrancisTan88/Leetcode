from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    '''
    time: O(n)
    space: O(n), given that the tree could be skewed. Otherwise, it would be O(h) in average cases
    '''
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, num_nodes, pos, max_pos):
            if not root:
                return num_nodes, max_pos
            num_nodes += 1
            max_pos = max(max_pos, pos)
            num_nodes, max_pos = dfs(root.left, num_nodes, 2*pos, max_pos)
            num_nodes, max_pos = dfs(root.right, num_nodes, 2*pos+1, max_pos)
            return num_nodes, max_pos
        num_nodes, max_pos = dfs(root, 0, 1, 1)
        return num_nodes == max_pos
    
    '''
    time: O(n)
    space: O(n)
    '''
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        bfs = [root]
        idx = 0
        while bfs[idx]:
            bfs.append(bfs[idx].left)
            bfs.append(bfs[idx].right)
            idx += 1
        for i in range(idx, len(bfs)):
            if bfs[i]:
                return False
        return True   