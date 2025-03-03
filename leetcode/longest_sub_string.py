class Solution:

  def lengthOfLongestSubstring(self, s: str) -> int:
    chars = {}
    left = right = 0
    res = 0
    while right < len(s):
      r = s[right]
      if r in chars:
        chars[r] += 1
      else:
        chars[r] = 1
      while chars[r] > 1:
        l = s[left]
        chars[l] -= 1
        left += 1
      res = max(res, right - left + 1)
      right += 1
    return res

s = "abcabcbb"
p1 = Solution()
ans = p1.lengthOfLongestSubstring(s)
print(ans)
