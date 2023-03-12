from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    """
    method1: bfs
    time: O(2n) = O(n)
    space: O(n), given that we use an array to store all nodes
    """
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root: return root
        
        nodes = [root]
        idx = 0
        while nodes[idx]:
            nodes.append(nodes[idx].left)
            nodes.append(nodes[idx].right)
            idx += 1
        
        idx = 0
        exp = 0
        nums_level = 2**exp
        while nodes[idx]:
            nums_level -= 1
            if nodes[idx+1] and nums_level != 0:
                nodes[idx].next = nodes[idx+1]
            if nums_level == 0:
                exp += 1
                nums_level = 2**exp
            idx += 1
        return nodes[0]

    """
    method1: dfs
    time: O(n)(best solution).
    space: O(1), given that the system stack is not counted as extra space according to the problem.
    """
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(root):
            if not root:
                return
            if root.left:
                root.left.next = root.right
                if root.next:
                    root.right.next = root.next.left
            dfs(root.left)
            dfs(root.right)
        head = root
        dfs(root)
        return head