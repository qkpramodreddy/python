def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
nums = [64, 5, 34, 25, 5, 22, 11, 90, 12]
print(nums)
insertion_sort(nums)
print(nums)

      
nums = [5, 2, 4, 1]
print(nums)
insertion_sort(nums)
print(nums)
nums =  [12, 11, 13, 5, 6]
print(nums)
insertion_sort(nums)
print(nums)
