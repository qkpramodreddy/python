class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
    
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)

head = one
one.next = two
two.prev = one
two.next = three
three.prev = two
three.next = None

print(two.prev.val)
print(two.val)
print(two.next.val)
