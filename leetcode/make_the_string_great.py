class Solution:
  def makeGood(self, s: str) -> str:
    stack = []
    for c in s:
      if not stack:
        stack.append(c)
      elif c.islower():
        if stack:
          if c.upper() == stack[-1]:
            stack.pop()
          else:
            stack.append(c)
      elif c.isupper():
        if stack:
          if c.lower() == stack[-1]:
            stack.pop()
          else:
            stack.append(c)



    return "".join(stack)


def main():
  obj = Solution()

  s1 = "leEeetcode"
  s2 = "abBAcC"
  s3 = "s"
  s4 = "Ppaa"
  test_cases = [s1, s2, s3, s4]
  for s in test_cases:
    print(s)
    ans = obj.makeGood(s)
    print(ans)


if __name__ == "__main__":
  main()
