class Solution:
  def simplifyPath(self, path: str) -> str:
    stack = []
    for portion in path.split('/'):
      if portion == "..":
        if stack:
          stack.pop()
      elif portion == "." or not portion:
        continue
      else:
        stack.append(portion)
    return "/"+"/".join(stack)

obj = Solution()

s1 = "/home/"
s2 = "/home//foo/"
s3 = "/home/user/Documents/../Pictures"
s4 = "/../"
s5 = "/.../a/../b/c/../d/./"

s_test = [s1, s2, s3, s4, s5]

counter = 1

for s in s_test:
  print(f"Test Case No: {counter}")
  print(s)
  ans = obj.simplifyPath(s)
  print(ans)
  counter += 1
