class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None

def sum_all(node: ListNode):

  ans = 0
  while node:
    ans += node.val
    node = node.next
  return ans

def get_sum(head):
  if not head:
    return 0
  return head.val + get_sum(head.next)
    
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)

head = one
one.next = two
two.next = three
three.next = None

print(head.val)
print(head.next.val)
print(head.next.next.val)

ans = sum_all(one)

print(ans)

ans = get_sum(one)

print(ans)



