class Solution:
  def twoSum(self, nums: list[int], target: int) -> list[int]:
    nums_dict = {}
    for i, num in enumerate(nums):
      print(i, num)
      c = target - num
      if c in nums_dict:
        return [nums_dict[c], i]
      nums_dict[num] = i
    return []

  def threeSum(self, nums: list[int]) -> list[list[int]]:
    nums.sort()
    print(nums)
    for i in range(len(nums)):
      a = self.twoSum(nums[i+1:], -nums[i])
      if len(a) > 0:
        print(a)
        print(nums[i],a[0],a[1])


          
        

p1 = Solution()

b = p1.twoSum([2,7,11,15], 9)
print(b)

a = p1.threeSum([-1,0,1,2,-1,-4])
print(a)

