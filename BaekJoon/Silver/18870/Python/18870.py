import sys

n = int(sys.stdin.readline())
nums = [num for num in map(int, sys.stdin.readline().split())]
sorted_nums = sorted(nums)
memo = {}
memo[sorted_nums[0]] = 0
if n > 1:
    memo[sorted_nums[1]] = 0 if sorted_nums[0] == sorted_nums[1] else 1
for i in range(2, n):
    if sorted_nums[i-1] == sorted_nums[i]:
        memo[sorted_nums[i]] = memo[sorted_nums[i-2]]
        if sorted_nums[i] != sorted_nums[i-2]:
            memo[sorted_nums[i]] += 1
    else:
        memo[sorted_nums[i]] = memo[sorted_nums[i-1]] + 1
for num in nums:
    print(memo[num], end=' ')
print('\n', end='')