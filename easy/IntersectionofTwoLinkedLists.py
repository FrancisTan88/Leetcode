from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # time: O(m+n), space: O(m)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        store_a = {}
        while headA:
            store_a[headA] = "whatever"
            headA = headA.next
        
        while headB:
            if headB in store_a:
                return headB
            headB = headB.next
        return None