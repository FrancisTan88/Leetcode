from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    '''
    time: O(n) 
    space: O(1)
    '''
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count1 = 0
        head2 = head
        while head:
            count1 += 1
            head = head.next
        
        mid = count1 // 2 + 1
        count2 = 0
        while head2:
            count2 += 1
            if count2 == mid:
                return head2
            head2 = head2.next
        return None

    '''
    time: O(n) 
    space: O(1)
    '''
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow