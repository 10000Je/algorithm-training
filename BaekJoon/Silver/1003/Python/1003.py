import sys

t = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for i in range(t)]
n = max(nums)
memo = [(0,0) for i in range(n+1)]
if n >= 0:
    memo[0] = (1, 0)
if n >= 1:
    memo[1] = (0, 1)
for i in range(2, n+1):
    memo[i] = (memo[i-1][0] + memo[i-2][0], memo[i-1][1] + memo[i-2][1])

for num in nums:
    print(memo[num][0], memo[num][1], sep=' ')