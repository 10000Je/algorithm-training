n = int(input())
nums = [i for i in range(1, n+1)]
popped_nums = []
while nums:
    popped_nums.append(nums.pop(0))
    if nums:
        temp = nums.pop(0)
        nums.append(temp)
print(*popped_nums, sep=' ')