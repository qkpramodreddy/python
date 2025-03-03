def insertion_sort(nums: list):
  n = len(nums)
  for i in range(1, n):
    print(nums)
    for j in range(0, i):
      if nums[j] > nums[i]:
        nums[i], nums[j] = nums[j], nums[i]
      print(i, j)
      print(nums)
      print("-------")


nums = [3, 1, 4, 2, -1 , 10, 5, 6, 3, 10]


print(nums)
insertion_sort(nums)
print(nums)

