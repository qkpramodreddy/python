class Solution:
  def is_valid(self, s):
    stack = []
    matching = {'{':'}', '[':']', '(':')'}

    for c in s:
      if c in matching:
        stack.append(c)
      else:
        if not stack:
          return False
        previous_opening = stack.pop()
        if matching[previous_opening] != c:
          return False
    return not stack
        
#s = "({})"
s = "()I"
obj = Solution()
ans = obj.is_valid(s)

print(ans)
