"""
This is the implementation of doubly linked list.
Note: In this case, the duplicates(key) are not allowed.
"""
class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None) -> None:
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        
class DoublyLinkedList:
    def __init__(self) -> None:
        self.hashmap = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hashmap[-1] = self.head
        # self.hashmap[-2] = self.tail

    def remove(self, key: int) -> None:
        if key in self.hashmap:
            ptr = self.hashmap[key]
            ptr.prev.next = ptr.next
            ptr.next.prev = ptr.prev
            self.hashmap.pop(key)
        else:
            raise TypeError("the key is not in the list")

    def insert_after(self, insert_key: int, key: int, value: int) -> None:
        curr = ListNode(key, value)
        if insert_key in self.hashmap:
            node = self.hashmap[insert_key]
            node.next.prev = curr
            curr.next = node.next
            node.next = curr
            curr.prev = node 
        # if given key is already in hm, remove the original one
        if key in self.hashmap:
            self.remove(key)
        # update the hm
        self.hashmap[key] = curr
        
    def print_ll(self) -> None:
        tmp_node = self.head.next
        while tmp_node != self.tail:
            if tmp_node.next == self.tail:
                print((tmp_node.key, tmp_node.val), end="\n")
            else:
                print((tmp_node.key, tmp_node.val), end="->")
            tmp_node = tmp_node.next

dll = DoublyLinkedList()
lst = [(-1,1,1), (1,2,2), (2,3,3), (3,4,4), (4,5,5), (3,6,6), (3,2,8), (5,5,0), (-1,0,0), (5,5,2), (5,5,3), (5,5,4), (1,-8,-4)]
for insert_k, k, v in lst:
    dll.insert_after(insert_k, k, v)
dll.print_ll()