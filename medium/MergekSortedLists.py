from heapq import heappop, heappush
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    """
    method: min heap
    time: O(nlogk)
    space: O(n)
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []
        for i in range(len(lists)):
            if lists[i]:
                heappush(minheap, (lists[i].val, i))
        dummy = ListNode()
        head = dummy
        while minheap:
            value, row = heappop(minheap)
            dummy.next = ListNode(value)
            dummy = dummy.next
            if lists[row].next:
                lists[row] = lists[row].next
                heappush(minheap, (lists[row].val, row))
        return head.next

    """
    method: compare heads of k lists for each time
    time: O(n*k)
    space: O(n)
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        while any(lists) == True:
            row = -1
            minimum = 10001
            for i in range(len(lists)):
                if lists[i] != None and lists[i].val < minimum:
                    minimum = lists[i].val
                    row = i
            if minimum != 10001:
                nxt = lists[row].next
                lists[row].next = None
                dummy.next = lists[row]
                dummy = dummy.next
                lists[row] = nxt
        return head.next


