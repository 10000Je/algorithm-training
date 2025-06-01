import sys

t = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for i in range(t)]
n = max(nums)
memo = [0 for i in range(n+1)]
if n >= 1:
    memo[1] = 1
if n >= 2:
    memo[2] = 2
if n >= 3:
    memo[3] = 4
for i in range(4, n+1):
    memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
for num in nums:
    print(memo[num])