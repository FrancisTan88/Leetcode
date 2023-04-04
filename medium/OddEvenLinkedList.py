from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    """
    method: two pointers
    time: O(n)
    space: O(1)
    """
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next: 
            return head
        
        h1, h2 = head, head.next
        l, r = h1, h2
        while l.next.next:
            l.next = r.next
            l = l.next
            if l.next:
                r.next = l.next
                r = r.next
            else:
                r.next = None
                break
        l.next = h2
        return h1