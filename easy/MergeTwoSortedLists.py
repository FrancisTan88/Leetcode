from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    '''
    time: O(n+m) 
    space: O(n+m)
    '''
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        head = node
        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    node.next = ListNode(list1.val)
                    list1 = list1.next
                else:
                    node.next = ListNode(list2.val)
                    list2 = list2.next
            elif list1:
                node.next = ListNode(list1.val)
                list1 = list1.next
            else:
                node.next = ListNode(list2.val)
                list2 = list2.next
            node = node.next
        head = head.next 
        return head

    '''
    time: O(n+m) 
    space: O(1)
    '''
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        head = node
        while list1 and list2:
            if list1.val <= list2.val:
                nxt = list1.next
                list1.next = None
                node.next = list1
                list1 = nxt
            else:
                nxt = list2.next
                list2.next = None
                node.next = list2
                list2 = nxt
            node = node.next
        while list1:
            nxt = list1.next
            list1.next = None
            node.next = list1
            list1 = nxt
            node = node.next
        while list2:
            nxt = list2.next
            list2.next = None
            node.next = list2
            list2 = nxt
            node = node.next
        return head.next