from typing import List

class Solution:
  def min_start_value(self, nums):
    total = 0
    start_value = 0
    for num in nums:
      total += num 
      start_value = min(total, start_value)
      print(start_value)
    start_value = (start_value * -1) + 1
    return start_value

nums = [-3, 2, -3, 4, 2]

p1 = Solution()
a = p1.min_start_value(nums)
print(a)
