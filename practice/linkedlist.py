class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_ll(head):
    while head:
        print(head.val)
        head = head.next

lst = [1,2,3,4,5]
node = ListNode()
head = node
# print(head, node)
for n in lst:
    curr = ListNode(n)
    node.next = curr
    node = node.next
head = head.next
ret_head = head
print(ret_head, head)
while head:
    if head.val == 3:
        head.next = head.next.next
    head = head.next
print(ret_head, head)
print_ll(ret_head)
