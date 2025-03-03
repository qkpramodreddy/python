import sys
class Solution:
  def romanToInt(self, s: str) -> int:
    conversion_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s_int = 0
    s_length = len(s)
    for c in range(s_length):
      if c ==  s_length - 1:
          s_int += conversion_dict[s[c]]
      else:
        if conversion_dict[s[c]] >= conversion_dict[s[c+1]]:
          s_int += conversion_dict[s[c]]
        else:
          s_int -= conversion_dict[s[c]]
    return s_int

p = Solution()
s = sys.argv[1]
s_int = p.romanToInt(s)
print(s, s_int)
