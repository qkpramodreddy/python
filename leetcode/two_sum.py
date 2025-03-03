class Solution:
  
  def two_sum(sum, nums, target):
    
    hashmap = {}
    for i in range(len(nums)):
      print(i)
      print(nums[i])
      complement = target - nums[i] 
      if complement in hashmap:
        return([i, hashmap[complement]])
      hashmap[nums[i]] = i
    return[]

nums = [2,7,11,15] 
target = 9

p1 = Solution()

ans = p1.two_sum(nums, target)
print(ans)
