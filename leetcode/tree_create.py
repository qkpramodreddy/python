from collections import deque 
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def preorder_dfs(node):
  if not node:
    return
  print(node.val)
  preorder_dfs(node.left)
  preorder_dfs(node.right)
  return

def inorder_dfs(node):
  if not node:
    return
  inorder_dfs(node.left)
  print(node.val)
  inorder_dfs(node.right)
  return

def postorder_dfs(node):
  if not node:
    return
  postorder_dfs(node.left)
  postorder_dfs(node.right)
  print(node.val)
  return


  


def build_complete_tree(arr: list[int], i: int, n: int) -> TreeNode:
  root = None
  if i < n and arr[i] is not None:
    root = TreeNode(arr[i])
    root.left = build_tree(arr, 2 * i + 1, n)
    root.right = build_tree(arr, 2 * i + 2, n)
  return root

def build_tree1(arr: list[int]) -> TreeNode:

  if len(arr) == 0:
    return None

  nodes = []
  
  val = arr.pop(0)
  
  root = TreeNode(val)
  nodes.append(root)

  while len(arr) > 0:
    curr = nodes.pop(0)

    left_val = arr.pop(0)
    if left_val is not None:
      curr.left = TreeNode(left_val)
      nodes.append(curr.left)

    if len(arr) > 0:
      right_val = arr.pop(0)
      if right_val is not None:
        curr.right = TreeNode(right_val)
        nodes.append(curr.right)

  return root

def build_tree(arr: list[int]) -> TreeNode:
    """
    >>> arr = [1, 2, 3, None, 4, None, None, 5, 6, None, 7]
    >>> build_tree(arr)
    (1)
      (2)
        (4)
          (5)
            (7)
          (6)
      (3)
    """
    if len(arr) == 0:
        return None

    nodes = []

    val = arr.pop(0)
    root = TreeNode(val)
    nodes.append(root)

    while len(arr) > 0:
        curr = nodes.pop(0)

        left_val = arr.pop(0)
        if left_val is not None:
            curr.left = TreeNode(left_val)
            nodes.append(curr.left)

        if len(arr) > 0:
            right_val = arr.pop(0)
            if right_val is not None:
                curr.right = TreeNode(right_val)
                nodes.append(curr.right)

    return root


def array_to_binary_tree(lst):
    if not lst:
        return
    node = root = TreeNode(lst[0])
    queue = deque()
    for i, value in enumerate(lst[1:]):
        if value is not None:  # A node to create?
            queue.append(TreeNode(value))
            if i % 2:  # At odd iterations we attach it as a right child
                node.right = queue[-1]
            else:  # At even iterations we attach it as a left child
                node.left = queue[-1]
        if i % 2 and queue:  # After odd iterations we grab a next parent
            node = queue.popleft()

    return root  

if __name__ == "__main__":

  arr = [1, 2, 3, None, 4, None, None, 5, 6, None, 7]

  root = build_tree1(arr)
  #root = array_to_binary_tree(arr)
  
  print("preorder")
  preorder_dfs(root)
  print("inorder")
  inorder_dfs(root)
  print("postorder")
  postorder_dfs(root)
