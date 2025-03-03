class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def append(self, data):
    new_node = Node(data)
    if not self.head:
      self.head = new_node
      return
    current = self.head
    while current.next:
      current = current.next
    current.next = new_node

  def prepend(self, data):
    new_node = Node(data)
    curr_head = self.head
    self.head = new_node
    self.head.next = curr_head

  def insert_after(self, prev_data, data):
    new_node = Node(data)
    current = self.head
    while current:
      if current.data == prev_data:
        new_node.next = current.next
        current.next = new_node
        return
      current = current.next
    print(f"Node with data {prev_data} not found.")

  def delete(self, data):
    if not self.head:
      return
    
    if self.head.data == data:
      self.head = self.head.next
      return
    current = self.head
    while current.next:
      if current.next.data == data:
        current.next = current.next.next
        return
      current = current.next
    print(f"Node with data {data} not found.")

  def print_list(self):
    current = self.head
    while current:
      print(current.data, end="-> ")
      current = current.next
    print("None")

llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.print_list()
llist.prepend(0)
llist.print_list()
llist.insert_after(2, 2.5)
llist.print_list()
llist.delete(2)
llist.print_list()
llist.delete(5)
