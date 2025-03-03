from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0

    left = self.maxDepth(root.left)
    right = self.maxDepth(root.right)
    return max(left, right) + 1


def build_tree(arr) -> TreeNode:
  if len(arr) == 0:
    return

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

  obj = Solution()

  ans = obj.maxDepth(root)

  print(ans)

