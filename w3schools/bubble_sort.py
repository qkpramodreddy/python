def bubble_sort(nums):

  n = len(nums)
  for i in range(n-1):
    for j in range(n-i-1):
      if nums[j] > nums[j+1]:
        nums[j], nums[j+1] = nums[j+1], nums[j]

a = [ 7,12,9,11,3 ]
bubble_sort(a)
print(a)
