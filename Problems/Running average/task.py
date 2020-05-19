nums = [int(x) for x in input()]
print([(nums[y] + nums[y + 1]) / 2 for y in range(len(nums) - 1)])
