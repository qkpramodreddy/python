def min_array(nums):
  least = nums[0]
  for num in nums[1:]:
    if num < least:
      least = num
  print(least)

min_array([ 7,12,9,11,3 ])

    
