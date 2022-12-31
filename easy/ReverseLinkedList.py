from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    """
    method: iterative
    time: O(n)
    space: O(1)
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = None
        while head:
            nxt = head.next
            head.next = ans
            ans = head
            head = nxt
        return ans 

    """
    method: recursion
    time: O(n)
    space: O(n)
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def do(head, ans):
            if not head:
                return ans
            nxt = head.next
            head.next = ans
            ans = head
            return do(nxt, ans)
        return do(head, None)