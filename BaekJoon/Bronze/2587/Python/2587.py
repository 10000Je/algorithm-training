nums = [int(input()) for _ in range(5)]
nums.sort()
print(sum(nums)//len(nums))
print(nums[2])