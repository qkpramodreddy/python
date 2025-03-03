class TreeNode:
  def __init__(self, val, left, right):
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


if __name__ == "__main__":
  six = TreeNode(6, None, None)
  four = TreeNode(4, None, six)
  three = TreeNode(3, None, None)
  one = TreeNode(1, three, four)
  five = TreeNode(5, None, None)
  two = TreeNode(2, None, five)
  zero = TreeNode(0, one, two)
  print("preorder")
  preorder_dfs(zero)
  print("inorder")
  inorder_dfs(zero)
  print("postorder")
  postorder_dfs(zero)
  


