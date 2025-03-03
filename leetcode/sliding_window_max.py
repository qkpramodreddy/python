from collections import deque

class Solution:
  def maxSlidingWindow(self, nums: list, k: int) -> list:
    ans = []
    queue = deque()
    counter = 0

    for i in range(len(nums)):
      while queue and nums[i] > nums[queue[-1]]:
        queue.pop()

      queue.append(i)
      print(queue) 
      if queue[0] + k == i:
        queue.popleft()
      
      counter += 1
      if counter == k:
        print(i, k)
        ans.append(nums[queue[0]])
        counter -= 1
    return ans

obj = Solution()
nums = [1, 3, -1, -3, 5, 3, 6, 7] 
k = 3
ans =  obj.maxSlidingWindow(nums, k)
print(ans)
