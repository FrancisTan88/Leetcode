class Node:
    def __init__(self, key=0, val=0, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = nxt

class LRUCache:
    def __init__(self, capacity: int):
        self.hashmap = {}
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        node = self.hashmap[key]
        if node == self.head.next:
            return node.val
        
        # remove
        node.prev.next = node.next
        node.next.prev = node.prev

        # insert after head
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head

        return node.val

    def put(self, key: int, value: int) -> None:
        new_node = Node(key, value)
        if key in self.hashmap:
            node = self.hashmap[key]
            # remove
            node.prev.next = node.next
            node.next.prev = node.prev

        # insert after head
        self.head.next.prev = new_node
        new_node.next = self.head.next
        self.head.next = new_node
        new_node.prev = self.head
        
        # update hm
        self.hashmap[key] = new_node

        # check capacity
        if len(self.hashmap) > self.capacity:
            # remove before tail
            k = self.tail.prev.key
            self.tail.prev.prev.next = self.tail
            self.tail.prev = self.tail.prev.prev
            self.hashmap.pop(k)
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)