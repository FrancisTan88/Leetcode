class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

lst = [1,2,3,4,5]
node = ListNode()
head = node
for i in lst:
    curr_node = ListNode(i)
    node.next = curr_node
    node = node.next
head = head.next
while head:
    print(head.val)
    head = head.next
    

