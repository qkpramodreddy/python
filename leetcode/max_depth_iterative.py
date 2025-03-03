from collections import deque 
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def maxDepth(self, root: TreeNode) -> int:
    if not root:
      return 0
    stack = [(root, 1)]
    ans = 0

    while stack:
      node, depth = stack.pop()
      ans = max(ans, depth)
      print(node.val)
      if node.left:
        stack.append((node.left, depth+1))
      if node.right:
        stack.append((node.right, depth+1))
    return ans



def build_tree(arr: list[int]) -> TreeNode:
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

if __name__ == "__main__":
  arr = [1, 2, 3, None, 4, None, None, 5, 6, None, 7]

  root = build_tree(arr)  
  a = Solution()
  ans = a.maxDepth(root)
  print(ans)
