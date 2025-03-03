class Node:
  def __init__(self, key, val):
    self.key = key
    self.val = val
    self.next = None
    self.prev= None

class LRUCache
  def (self, capacity):
    self.capacity = capacity
    self.dic = {}
    self.head = Node(-1,-1)
    self.tail = Node(-1, -1)
    self.head.next = self.tail
    self.tail.prev = self.head



