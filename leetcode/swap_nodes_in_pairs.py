class Solution:
  def swapPairs(self, head: ListNode) -> ListNode:
    if not head or not head.next:
      return head

    dummy = head.next
    prev = None
    while head and head.next:
      if prev:
        prev.next
      prev = head

      next_node = head.next.next
      head.next.next = head

      head.next = next_node
      head = next_node

    return dummy
