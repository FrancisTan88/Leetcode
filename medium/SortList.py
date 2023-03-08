from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    """
    time: O(nlogn)
    space: O(n)
    """
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        while head:
            ans.append(ListNode(head.val))
            head = head.next
        ans.sort(key=lambda x: x.val)
        dummy = ListNode()
        head = dummy
        for i in ans:
            dummy.next = i
            dummy = dummy.next
        return head.next