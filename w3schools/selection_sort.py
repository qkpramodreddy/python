def selection_sort(nums: list):
  for i in range(len(nums)):
    small = nums[i]
    min_index = i
    for j in range(i+1,len(nums)):
      curr = nums[j]
      if curr < small:
        min_index = j
        small = curr
    curr = nums[i]
    nums[i] = small
    nums[min_index] = curr

def selection_sort_1(nums: list):
  n = len(nums)
  for i in range(n):
    min_index = i
    for j in range(i+1, n):
      if nums[j] < nums[min_index]:
        min_index = j
    
    #curr = nums[i]
    #nums[i] = nums[min_index]
    #nums[min_index] = curr

    nums[i], nums[min_index] = nums[min_index], nums[i]

nums = [64, 5, 34, 25, 5, 22, 11, 90, 12]
print(nums)
selection_sort(nums)
print(nums)

nums = [64, 5, 34, 25, 5, 22, 11, 90, 12]
print(nums)
selection_sort_1(nums)
print(nums)

nums = [1, 2, 0, 5, 3] 
print(nums)
selection_sort_1(nums)
print(nums)
