from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    time: O(2n) = O(n)
    space: O(1)
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp_head = head
        count = 0
        while head:
            count += 1
            head = head.next

        prev_remove = count - n
        ret_head = tmp_head
        count2 = 0
        while tmp_head:
            count2 += 1
            if count2 == prev_remove:
                tmp_head.next = tmp_head.next.next
                return ret_head
            tmp_head = tmp_head.next
        return ret_head.next
    

class Solution2:
    """
    (best solution)
    time: O(n)
    space: O(1)
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = head
        right = left
        for _ in range(n):
            right = right.next
        while right:
            if not right.next:
                left.next = left.next.next
                return head
            right = right.next
            left = left.next
        return head.next 
