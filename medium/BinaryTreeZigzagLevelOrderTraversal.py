from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    time: O(2n) = O(n), where n is the number of nodes in tree.
    space: O(n), where n is the number of nodes in tree.
    """
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        idx = 0
        lvl = 1
        ans = [[root]]
        while idx < len(ans) and ans[idx]:
            curr_lvl = []
            for i in range(len(ans[idx]) - 1, -1, -1):
                if lvl % 2:
                    if ans[idx][i].right:
                        curr_lvl.append(ans[idx][i].right)
                    if ans[idx][i].left:
                        curr_lvl.append(ans[idx][i].left)
                else:
                    if ans[idx][i].left:
                        curr_lvl.append(ans[idx][i].left)
                    if ans[idx][i].right:
                        curr_lvl.append(ans[idx][i].right)
            ans.append(curr_lvl)
            lvl += 1
            idx += 1
        ans.pop()
        for i in range(len(ans)):
            for j in range(len(ans[i])):
                ans[i][j] = ans[i][j].val
        return ans


class Solution2:
    """
    (best solution)
    time: O(n), where n is the number of nodes in tree.
    space: O(n)
    Note: "popleft" and "appendleft" takes only O(1) in deque(double ended queue)
    """
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        queue = deque([root])
        ans = []
        lvl = 1
        while queue:
            lvl_vals = []
            for _ in range(len(queue)):
                node = queue.popleft()
                lvl_vals.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(lvl_vals[::lvl])
            lvl *= -1
        return ans
