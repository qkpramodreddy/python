class Solution:
  def removeDuplicates(self, s):
    stack = []
    for c in s:
      if stack and stack[-1] == c:
        stack.pop()
      else:
        stack.append(c)
    return "".join(stack)

obj = Solution()

s1 = "arjun reddy patlolla"
s2 = "swathi reddy patlolla"
s3 = "pramod reddy patlolla"
s4 = "narasimha reddy patlolla"
s5 = "sanjana reddy patlolla"
s6 = "prashanth reddy patlolla"
s7 = "preethi reddy patlolla"
s8 = "praveen reddy patlolla"

s = [s1, s2, s3, s4, s5, s6, s7, s8]
for s in s:
  ans = obj.removeDuplicates(s)
  print(ans)
